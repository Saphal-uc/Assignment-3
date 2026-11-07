
"""Tests for practitioner lookup in PractitionerService."""

import pytest

from smartcare.data_store import SmartCareDataStore
from smartcare.services import PatientService, PractitionerService

def setup_practitioner():
    """Create a store and register one practitioner."""
    data_store = SmartCareDataStore()
    service = PractitionerService(data_store)

    practitioner = service.register_practitioner(
        "D1",
        "Taylor Example",
        "General",
    )

    return data_store, service, practitioner


def test_find_practitioner_returns_stored_object():
    """Return the actual registered practitioner."""
    data_store, service, practitioner = setup_practitioner()

    result = service.find_practitioner("D1")

    assert result is practitioner
    assert data_store.find_practitioner("D1") is practitioner


def test_find_practitioner_unknown_id_raises_lookup_error():
    """Raise LookupError when the ID does not exist."""
    _, service, _ = setup_practitioner()

    with pytest.raises(LookupError):
        service.find_practitioner("D99")


def test_find_practitioner_blank_id_raises_value_error():
    """Reject a blank practitioner ID."""
    _, service, _ = setup_practitioner()

    with pytest.raises(ValueError):
        service.find_practitioner(" ")


def test_find_practitioner_trims_id():
    """Accept an ID with surrounding spaces."""
    _, service, practitioner = setup_practitioner()

    result = service.find_practitioner(" D1 ")

    assert result is practitioner


def test_find_practitioner_is_case_sensitive():
    """Do not match an ID with different letter case."""
    _, service, _ = setup_practitioner()

    with pytest.raises(LookupError):
        service.find_practitioner("d1")


def test_find_practitioner_does_not_change_record():
    """Keep the existing practitioner record unchanged."""
    _, service, practitioner = setup_practitioner()

    service.find_practitioner("D1")

    assert practitioner.practitioner_id == "D1"
    assert practitioner.name == "Taylor Example"
    assert practitioner.specialty == "General"

@pytest.mark.parametrize("practitioner_id", ["", None])
def test_find_practitioner_rejects_empty_or_none_id(practitioner_id):
    """Reject an empty or None practitioner ID."""
    _, service, _ = setup_practitioner()

    with pytest.raises(ValueError):
        service.find_practitioner(practitioner_id)


def test_find_practitioner_repeated_lookup_returns_same_object():
    """Repeated lookups return the same registered practitioner."""
    _, service, practitioner = setup_practitioner()

    first_result = service.find_practitioner("D1")
    second_result = service.find_practitioner("D1")

    assert first_result is practitioner
    assert second_result is practitioner
    assert first_result is second_result

def setup_patient():
    """Create a store and register one patient."""
    data_store = SmartCareDataStore()
    service = PatientService(data_store)

    patient = service.register_patient("P001", "Alex Example")

    return data_store, service, patient


def test_find_patient_returns_stored_object():
    """Return the actual registered patient."""
    data_store, service, patient = setup_patient()

    result = service.find_patient("P001")

    assert result is patient
    assert data_store.find_patient("P001") is patient


def test_find_patient_unknown_id_raises_lookup_error():
    """Raise LookupError when the patient does not exist."""
    _, service, _ = setup_patient()

    with pytest.raises(LookupError):
        service.find_patient("P999")


def test_find_patient_blank_id_raises_value_error():
    """Reject a blank patient ID."""
    _, service, _ = setup_patient()

    with pytest.raises(ValueError):
        service.find_patient(" ")


def test_find_patient_trims_id():
    """Accept an ID with surrounding spaces."""
    _, service, patient = setup_patient()

    result = service.find_patient(" P001 ")

    assert result is patient


def test_find_patient_is_case_sensitive():
    """Do not match an ID with different letter case."""
    _, service, _ = setup_patient()

    with pytest.raises(LookupError):
        service.find_patient("p001")


def test_find_patient_does_not_change_record():
    """Keep the existing patient record unchanged."""
    _, service, patient = setup_patient()

    service.find_patient("P001")

    assert patient.patient_id == "P001"
    assert patient.name == "Alex Example"


from datetime import datetime

import pytest

from smartcare.data_store import SmartCareDataStore
from smartcare.domain import Appointment, AppointmentStatus
from smartcare.services import (
    AppointmentService,
    PatientService,
    PractitionerService,
)


@pytest.fixture
def cancellation_setup():
    store = SmartCareDataStore()

    patient = PatientService(store).register_patient(
        "P1", "Alex Example"
    )
    practitioner = PractitionerService(store).register_practitioner(
        "D1", "Taylor Example", "General"
    )

    service = AppointmentService(store)
    appointment = service.book_appointment(
        "A1", "P1", "D1", datetime(2026, 10, 26, 10, 0)
    )

    return store, service, appointment, patient, practitioner




@pytest.mark.parametrize(
    "appointment_id, expected_error",
    [
        ("UNKNOWN", LookupError),
        ("", ValueError),
        ("   ", ValueError),
        (None, ValueError),
    ],
)
def test_cancel_rejects_invalid_or_unknown_id(
    cancellation_setup, appointment_id, expected_error
):
    store, service, appointment, _, _ = cancellation_setup

    with pytest.raises(expected_error):
        service.cancel_appointment(appointment_id)

    assert appointment.status is AppointmentStatus.SCHEDULED
    assert store.list_appointments() == [appointment]


def test_repeated_cancellation_is_rejected(cancellation_setup):
    """Repeated cancellation preserves all appointment details."""
    store, service, appointment, patient, practitioner = cancellation_setup
    original_id = appointment.appointment_id
    original_time = appointment.date_time

    service.cancel_appointment(original_id)

    with pytest.raises(ValueError):
        service.cancel_appointment(original_id)

    assert appointment.status is AppointmentStatus.CANCELLED
    assert appointment.appointment_id == original_id
    assert appointment.patient is patient
    assert appointment.practitioner is practitioner
    assert appointment.date_time == original_time
    assert service.find_appointment(original_id) is appointment
    assert store.list_appointments() == [appointment]


def test_completed_appointment_cannot_be_cancelled(cancellation_setup):
    """Rejected cancellation preserves a completed appointment."""
    store, service, _, patient, practitioner = cancellation_setup
    original_time = datetime(2026, 10, 26, 11, 0)

    completed = Appointment(
        "A2",
        patient,
        practitioner,
        original_time,
        AppointmentStatus.COMPLETED,
    )
    store.add_appointment(completed)
    before = store.list_appointments()

    with pytest.raises(ValueError):
        service.cancel_appointment("A2")

    assert completed.status is AppointmentStatus.COMPLETED
    assert completed.appointment_id == "A2"
    assert completed.patient is patient
    assert completed.practitioner is practitioner
    assert completed.date_time == original_time
    assert service.find_appointment("A2") is completed
    assert store.list_appointments() == before

def test_cancel_retains_same_appointment(cancellation_setup):
    """Cancellation changes only status and retains the same record."""
    store, service, appointment, patient, practitioner = cancellation_setup

    # Arrange: remember the original identity and time.
    original_id = appointment.appointment_id
    original_time = appointment.date_time

    # Act: cancel through the service.
    result = service.cancel_appointment(original_id)

    # Assert: status changes, but all other details remain.
    assert result is appointment
    assert appointment.status is AppointmentStatus.CANCELLED
    assert appointment.appointment_id == original_id
    assert appointment.patient is patient
    assert appointment.practitioner is practitioner
    assert appointment.date_time == original_time

    # The same appointment remains stored and retrievable.
    assert service.find_appointment(original_id) is appointment
    assert store.list_appointments() == [appointment]


def test_cancelled_appointment_slot_can_be_reused(cancellation_setup):
    """Verify a cancelled appointment no longer blocks its time slot."""
    store, service, original, patient, practitioner = cancellation_setup

    # Arrange: cancel the existing appointment.
    service.cancel_appointment("A1")

    # Act: book another appointment at the same time.
    replacement = service.book_appointment(
        "A2",
        "P1",
        "D1",
        original.date_time,
    )

    # Assert: the original remains cancelled.
    assert original.status is AppointmentStatus.CANCELLED

    # Assert: the replacement is successfully scheduled.
    assert replacement.status is AppointmentStatus.SCHEDULED

    # Assert: both appointments remain in the store.
    assert service.find_appointment("A1") is original
    assert service.find_appointment("A2") is replacement
    assert store.list_appointments() == [original, replacement]

def test_cancel_does_not_change_other_appointment(cancellation_setup):
    """Cancelling A1 leaves A2 unchanged."""
    store, service, first, patient, practitioner = cancellation_setup

    # Arrange: book A2 at a different time.
    second_time = datetime(2026, 10, 26, 11, 0)
    second = service.book_appointment(
        "A2", "P1", "D1", second_time
    )

    # Act: cancel only A1.
    service.cancel_appointment("A1")

    # Assert: A1 is cancelled.
    assert first.status is AppointmentStatus.CANCELLED

    # A2 keeps its original status and details.
    assert second.status is AppointmentStatus.SCHEDULED
    assert second.appointment_id == "A2"
    assert second.patient is patient
    assert second.practitioner is practitioner
    assert second.date_time == second_time
    assert service.find_appointment("A2") is second

    # Both records remain stored.
    assert store.list_appointments() == [first, second]

def test_rejected_booking_conflict_preserves_existing_appointment(cancellation_setup):
    """Verify a rejected booking does not modify the existing appointment."""

    store, service, original, patient, practitioner = cancellation_setup

    # Arrange: capture the original appointment state.
    original_status = original.status
    original_date_time = original.date_time
    original_count = len(store.list_appointments())

    # Act and assert: conflicting booking must be rejected.
    with pytest.raises(ValueError):
        service.book_appointment(
            "A2",
            "P1",
            "D1",
            original.date_time,
        )

    # Assert: original appointment remains unchanged.
    assert original.status is original_status
    assert original.date_time == original_date_time
    assert service.find_appointment("A1") is original

    # Assert: rejected appointment was not stored.
    assert len(store.list_appointments()) == original_count
    assert store.find_appointment("A2") is None

@pytest.fixture
def listing_setup():
    """Create practitioners and appointments for listing tests."""
    store = SmartCareDataStore()

    patient_service = PatientService(store)
    practitioner_service = PractitionerService(store)

    patient = patient_service.register_patient("P1", "Alex Example")

    practitioner = practitioner_service.register_practitioner(
        "D1", "Taylor Example", "General"
    )

    other_practitioner = practitioner_service.register_practitioner(
        "D2", "Jordan Example", "Dental"
    )

    service = AppointmentService(store)

    scheduled = Appointment(
        "A1",
        patient,
        practitioner,
        datetime(2026, 10, 26, 9, 0),
        AppointmentStatus.SCHEDULED,
    )

    cancelled = Appointment(
        "A2",
        patient,
        practitioner,
        datetime(2026, 10, 26, 10, 0),
        AppointmentStatus.CANCELLED,
    )

    completed = Appointment(
        "A3",
        patient,
        practitioner,
        datetime(2026, 10, 26, 11, 0),
        AppointmentStatus.COMPLETED,
    )

    other_appointment = Appointment(
        "A4",
        patient,
        other_practitioner,
        datetime(2026, 10, 26, 12, 0),
        AppointmentStatus.SCHEDULED,
    )

    for appointment in (
        scheduled,
        cancelled,
        completed,
        other_appointment,
    ):
        store.add_appointment(appointment)

    return (
        store,
        service,
        practitioner,
        scheduled,
        cancelled,
        completed,
        other_appointment,
    )


def test_list_practitioner_appointments_returns_all_statuses(listing_setup):
    """Default listing includes every appointment status."""
    store, service, practitioner, scheduled, cancelled, completed, _ = (
        listing_setup
    )

    result = service.list_practitioner_appointments(
        practitioner.practitioner_id
    )

    assert result == [scheduled, cancelled, completed]
    assert result[0] is scheduled
    assert result[1] is cancelled
    assert result[2] is completed
    assert cancelled.status is AppointmentStatus.CANCELLED
    assert store.find_appointment("A2") is cancelled


def test_list_practitioner_appointments_filters_scheduled(listing_setup):
    """Return only scheduled appointments."""
    _, service, practitioner, scheduled, _, _, _ = listing_setup

    result = service.list_practitioner_appointments(
        practitioner.practitioner_id,
        AppointmentStatus.SCHEDULED,
    )

    assert result == [scheduled]


def test_list_practitioner_appointments_filters_cancelled(listing_setup):
    """Return only cancelled appointments."""
    _, service, practitioner, _, cancelled, _, _ = listing_setup

    result = service.list_practitioner_appointments(
        practitioner.practitioner_id,
        AppointmentStatus.CANCELLED,
    )

    assert result == [cancelled]


def test_list_practitioner_appointments_filters_completed(listing_setup):
    """Return only completed appointments."""
    _, service, practitioner, _, _, completed, _ = listing_setup

    result = service.list_practitioner_appointments(
        practitioner.practitioner_id,
        AppointmentStatus.COMPLETED,
    )

    assert result == [completed]


def test_list_practitioner_appointments_unknown_id_raises_lookup_error(
    listing_setup,
):
    """Raise LookupError for an unknown practitioner."""
    _, service, *_ = listing_setup

    with pytest.raises(LookupError):
        service.list_practitioner_appointments("D99")


@pytest.mark.parametrize("practitioner_id", ["", "   ", None])
def test_list_practitioner_appointments_invalid_id_raises_value_error(
    listing_setup, practitioner_id
):
    """Reject blank or invalid practitioner IDs."""
    _, service, *_ = listing_setup

    with pytest.raises(ValueError):
        service.list_practitioner_appointments(practitioner_id)


def test_list_practitioner_appointments_invalid_status_raises_value_error(
    listing_setup,
):
    """Reject a status string instead of an enum value."""
    _, service, *_ = listing_setup

    with pytest.raises(ValueError):
        service.list_practitioner_appointments("D1", "scheduled")


def test_list_practitioner_appointments_trims_practitioner_id(listing_setup):
    """Accept a practitioner ID with surrounding spaces."""
    _, service, practitioner, scheduled, cancelled, completed, _ = (
        listing_setup
    )

    result = service.list_practitioner_appointments(" D1 ")

    assert result == [scheduled, cancelled, completed]


def test_list_practitioner_appointments_returns_empty_list_for_no_matches(
    listing_setup,
):
    """Return an empty list when there are no matching appointments."""
    _, service, *_ = listing_setup

    result = service.list_practitioner_appointments(
        "D2",
        AppointmentStatus.CANCELLED,
    )

    assert result == []


def test_list_practitioner_appointments_does_not_change_records(listing_setup):
    """Listing does not modify stored appointments or their order."""
    store, service, practitioner, *_ = listing_setup

    before = store.list_appointments()
    original_statuses = [appointment.status for appointment in before]

    service.list_practitioner_appointments(practitioner.practitioner_id)

    after = store.list_appointments()

    assert after == before
    assert all(
        actual is expected for actual, expected in zip(after, before)
    )
    assert [appointment.status for appointment in after] == original_statuses
