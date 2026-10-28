
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


def test_cancel_retains_same_appointment(cancellation_setup):
    store, service, appointment, _, _ = cancellation_setup

    result = service.cancel_appointment("A1")

    assert result is appointment
    assert appointment.status is AppointmentStatus.CANCELLED
    assert service.find_appointment("A1") is appointment
    assert store.list_appointments() == [appointment]


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
    store, service, appointment, _, _ = cancellation_setup
    service.cancel_appointment("A1")

    with pytest.raises(ValueError):
        service.cancel_appointment("A1")

    assert appointment.status is AppointmentStatus.CANCELLED
    assert service.find_appointment("A1") is appointment
    assert store.list_appointments() == [appointment]


def test_completed_appointment_cannot_be_cancelled(cancellation_setup):
    store, service, _, patient, practitioner = cancellation_setup

    completed = Appointment(
        "A2",
        patient,
        practitioner,
        datetime(2026, 10, 26, 11, 0),
        AppointmentStatus.COMPLETED,
    )
    store.add_appointment(completed)
    before = store.list_appointments()

    with pytest.raises(ValueError):
        service.cancel_appointment("A2")

    assert completed.status is AppointmentStatus.COMPLETED
    assert service.find_appointment("A2") is completed
    assert store.list_appointments() == before