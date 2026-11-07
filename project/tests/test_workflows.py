from datetime import datetime

import pytest

from smartcare.data_store import SmartCareDataStore
from smartcare.domain import AppointmentStatus
from smartcare.services import (
    AppointmentService,
    PatientService,
    PractitionerService,
)


def test_booking_conflict_preserves_original_and_allows_retry() -> None:
    """A rejected booking leaves the original intact and its new ID available."""
    store = SmartCareDataStore()
    patients = PatientService(store)
    practitioners = PractitionerService(store)
    appointments = AppointmentService(store)

    patient = patients.register_patient("P1", "Alex Example")
    d1 = practitioners.register_practitioner("D1", "Taylor Example", "General")
    d2 = practitioners.register_practitioner("D2", "Morgan Example", "General")
    when = datetime(2026, 10, 1, 9, 0)

    # Book A1, then try to book the same practitioner at the same time.
    original = appointments.book_appointment("A1", "P1", "D1", when)
    with pytest.raises(ValueError):
        appointments.book_appointment("A2", "P1", "D1", when)

    # The failed request must leave A1 unchanged and must not store A2.
    assert appointments.find_appointment("A1") is original
    assert original.patient is patient
    assert original.practitioner is d1
    assert original.date_time == when
    assert original.status is AppointmentStatus.SCHEDULED
    assert store.list_appointments() == [original]
    assert store.find_appointment("A2") is None

    # Retry the same ID and time with a different practitioner.
    retry = appointments.book_appointment("A2", "P1", "D2", when)
    assert appointments.find_appointment("A2") is retry
    assert retry.patient is patient
    assert retry.practitioner is d2
    assert retry.date_time == when
    assert retry.status is AppointmentStatus.SCHEDULED

def test_cancellation_frees_slot_but_preserves_appointment_history() -> None:
    """A cancelled appointment keeps its ID, but its time slot can be reused."""
    store = SmartCareDataStore()
    patients = PatientService(store)
    practitioners = PractitionerService(store)
    appointments = AppointmentService(store)

    patients.register_patient("P1", "Alex Example")
    practitioners.register_practitioner("D1", "Taylor Example", "General")
    when = datetime(2026, 10, 1, 9, 0)

    # Book A1, then cancel it.
    original = appointments.book_appointment("A1", "P1", "D1", when)
    assert appointments.cancel_appointment("A1") is original
    assert original.status is AppointmentStatus.CANCELLED

    # The old ID still belongs to A1. It cannot be used for a new booking.
    with pytest.raises(ValueError):
        appointments.book_appointment("A1", "P1", "D1", when)

    assert appointments.find_appointment("A1") is original
    assert store.list_appointments() == [original]

    # A new ID can use the same practitioner and time.
    replacement = appointments.book_appointment("A2", "P1", "D1", when)

    # Both records remain available: A1 is cancelled and A2 is scheduled.
    assert appointments.find_appointment("A1") is original
    assert original.status is AppointmentStatus.CANCELLED
    assert appointments.find_appointment("A2") is replacement
    assert replacement.status is AppointmentStatus.SCHEDULED
    assert replacement.practitioner is original.practitioner
    assert replacement.date_time == when
    assert len(store.list_appointments()) == 2    
def test_unknown_patient_booking_can_be_retried_after_registration() -> None:
    """A failed booking must not reserve the appointment ID or time slot."""
    store = SmartCareDataStore()
    patients = PatientService(store)
    practitioners = PractitionerService(store)
    appointments = AppointmentService(store)

    practitioner = practitioners.register_practitioner(
        "D1", "Taylor Example", "General"
    )
    when = datetime(2026, 10, 1, 9, 0)

    # P1 is not registered yet, so booking A1 must fail.
    with pytest.raises(LookupError):
        appointments.book_appointment("A1", "P1", "D1", when)

    assert store.find_patient("P1") is None
    assert store.list_appointments() == []

    # Register P1 and retry the exact same booking.
    patient = patients.register_patient("P1", "Alex Example")
    booked = appointments.book_appointment("A1", "P1", "D1", when)

    assert appointments.find_appointment("A1") is booked
    assert booked.patient is patient
    assert booked.practitioner is practitioner
    assert booked.date_time == when
    assert booked.status is AppointmentStatus.SCHEDULED
    assert store.list_appointments() == [booked]    