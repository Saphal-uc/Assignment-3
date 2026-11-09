from datetime import datetime

import pytest

from smartcare.data_store import SmartCareDataStore
from smartcare.domain import AppointmentStatus
from smartcare.services import AppointmentService, PatientService, PractitionerService


def test_patient_lookup_is_separate_between_sessions():
    """A patient registered in one session must not appear in another."""
    store_a = SmartCareDataStore()
    store_b = SmartCareDataStore()
    patients_a = PatientService(store_a)
    patients_b = PatientService(store_b)

    # P1 exists only in session A.
    alex = patients_a.register_patient("P1", "Alex Example")

    with pytest.raises(LookupError):
        patients_b.find_patient("P1")

    # The failed search must not create a patient in B or change A.
    assert store_b.list_patients() == []
    assert patients_a.find_patient("P1") is alex

    # A separate session can use P1 for a different patient.
    sam = patients_b.register_patient("P1", "Sam Example")

    assert patients_b.find_patient("P1") is sam
    assert patients_a.find_patient("P1") is alex
    assert sam is not alex
    assert alex.name == "Alex Example"


def test_reschedule_then_cancel_preserves_history_when_new_slot_is_reused():
    """Reusing the moved slot must not erase the cancelled appointment."""
    store = SmartCareDataStore()
    PatientService(store).register_patient("P1", "Alex Example")
    PractitionerService(store).register_practitioner(
        "D1", "Taylor Example", "General"
    )
    service = AppointmentService(store)

    original_time = datetime(2026, 11, 10, 9, 0)
    moved_time = datetime(2026, 11, 10, 11, 0)

    # Book A1 at 09:00, move it to 11:00, then cancel it.
    original = service.book_appointment("A1", "P1", "D1", original_time)
    service.reschedule_appointment("A1", moved_time)
    service.cancel_appointment("A1")

    # A2 can now use the same practitioner at 11:00.
    replacement = service.book_appointment("A2", "P1", "D1", moved_time)

    assert service.find_appointment("A1") is original
    assert original.status is AppointmentStatus.CANCELLED
    assert original.date_time == moved_time

    assert service.find_appointment("A2") is replacement
    assert replacement.status is AppointmentStatus.SCHEDULED
    assert replacement.date_time == moved_time
    assert replacement.practitioner is original.practitioner

    # Clearing a returned history list must not delete stored records.
    history = service.list_practitioner_appointments(
        "D1", AppointmentStatus.CANCELLED
    )
    assert history == [original]
    history.clear()

    assert service.list_practitioner_appointments(
        "D1", AppointmentStatus.CANCELLED
    ) == [original]
    assert service.list_practitioner_appointments(
        "D1", AppointmentStatus.SCHEDULED
    ) == [replacement]