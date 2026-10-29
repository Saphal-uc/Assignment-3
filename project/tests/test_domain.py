from datetime import datetime, timezone

import pytest

from smartcare.domain import Appointment, AppointmentStatus, Patient, Practitioner


# Patient Domain Tests

def test_valid_patient() -> None:
    """Verify valid patient construction and trimmed fields."""
    patient = Patient(" P1 ", " Alex ")
    assert patient.patient_id == "P1"
    assert patient.name == "Alex"

@pytest.mark.parametrize("patient_id", ["", "   ", None, 123])
def test_invalid_patient_id(patient_id) -> None:
    """Verify invalid patient IDs are rejected."""
    with pytest.raises(ValueError):
        Patient(patient_id, "Alex")

@pytest.mark.parametrize("name", ["", "   ", None, 123])
def test_invalid_patient_name(name) -> None:
    """Verify invalid patient names are rejected."""
    with pytest.raises(ValueError):
        Patient("P1", name)

def test_patient_id_read_only() -> None:
    """Verify patient ID cannot be changed."""
    patient = Patient("P1", "Alex")
    with pytest.raises(AttributeError):
        patient.patient_id = "P2"
    assert patient.patient_id == "P1"

# Practitioner Domain Tests

def test_valid_practitioner() -> None:
    """Verify valid practitioner construction and trimmed fields."""
    practitioner = Practitioner(" DR1 ", " Dr Smith ", " GP ")
    assert practitioner.practitioner_id == "DR1"
    assert practitioner.name == "Dr Smith"
    assert practitioner.specialty == "GP"

@pytest.mark.parametrize("practitioner_id", ["", "   ", None, 123])
def test_invalid_practitioner_id(practitioner_id) -> None:
    """Verify invalid practitioner IDs are rejected."""
    with pytest.raises(ValueError):
        Practitioner(practitioner_id, "Dr Smith", "GP")

@pytest.mark.parametrize("name", ["", "   ", None, 123])
def test_invalid_practitioner_name(name) -> None:
    """Verify invalid practitioner names are rejected."""
    with pytest.raises(ValueError):
        Practitioner("DR1", name, "GP")

@pytest.mark.parametrize("specialty", ["", "   ", None, 123])
def test_invalid_practitioner_specialty(specialty) -> None:
    """Verify invalid practitioner specialties are rejected."""
    with pytest.raises(ValueError):
        Practitioner("DR1", "Dr Smith", specialty)

def test_practitioner_id_read_only() -> None:
    """Verify practitioner ID cannot be changed."""
    practitioner = Practitioner("DR1", "Dr Smith", "GP")
    with pytest.raises(AttributeError):
        practitioner.practitioner_id = "DR2"
    assert practitioner.practitioner_id == "DR1"

# Appointment Domain Tests

def test_valid_appointment() -> None:
    """Verify valid appointment construction and initial status."""
    patient = Patient("P1", "Alex")
    practitioner = Practitioner("DR1", "Dr Smith", "GP")
    date_time = datetime(2026, 10, 28, 10, 0, 0, 0)
    appointment = Appointment("A1", patient, practitioner, date_time)
    assert appointment.appointment_id == "A1"
    assert appointment.patient is patient
    assert appointment.practitioner is practitioner
    assert appointment.date_time == date_time
    assert appointment.status is AppointmentStatus.SCHEDULED

@pytest.mark.parametrize("appointment_id", ["", "   ", None, 123])
def test_invalid_appointment_id(appointment_id) -> None:
    """Verify invalid appointment IDs are rejected."""
    patient = Patient("P1", "Alex")
    practitioner = Practitioner("DR1", "Dr Smith", "GP")
    date_time = datetime(2026, 10, 28, 10, 0)
    with pytest.raises(ValueError):
        Appointment(appointment_id, patient, practitioner, date_time)

def test_invalid_appointment_patient() -> None:
    """Verify appointment requires a Patient object."""
    practitioner = Practitioner("DR1", "Dr Smith", "GP")
    date_time = datetime(2026, 10, 28, 10, 0)
    with pytest.raises(ValueError):
        Appointment("A1", None, practitioner, date_time)

def test_invalid_appointment_practitioner() -> None:
    """Verify appointment requires a Practitioner object."""
    patient = Patient("P1", "Alex")
    date_time = datetime(2026, 10, 28, 10, 0)

    with pytest.raises(ValueError):
        Appointment("A1", patient, None, date_time)

def test_invalid_appointment_status() -> None:
    """Verify invalid appointment status is rejected."""
    patient = Patient("P1", "Alex")
    practitioner = Practitioner("DR1", "Dr Smith", "GP")
    date_time = datetime(2026, 10, 28, 10, 0)
    with pytest.raises(ValueError):
        Appointment("A1", patient, practitioner, date_time, status=None)

@pytest.mark.parametrize("date_time", [None,
    datetime(2026, 10, 28, 10, 0, tzinfo=timezone.utc),
    datetime(2026, 10, 28, 10, 0, 30),
    datetime(2026, 10, 28, 10, 0, 0, 1),
])
def test_invalid_appointment_date_time(date_time) -> None:
    """Verify invalid appointment date_time values are rejected."""
    patient = Patient("P1", "Alex")
    practitioner = Practitioner("DR1", "Dr Smith", "GP")
    with pytest.raises(ValueError):
        Appointment("A1", patient, practitioner, date_time)

def test_appointment_cancellation() -> None:
    """Verify cancellation and repeated cancellation guard."""
    patient = Patient("P1", "Alex")
    practitioner = Practitioner("DR1", "Dr Smith", "GP")
    date_time = datetime(2026, 10, 28, 10, 0)
    appointment = Appointment("A1", patient, practitioner, date_time)
    # First cancellation
    appointment.cancel()
    assert appointment.status is AppointmentStatus.CANCELLED
    # Second cancellation
    with pytest.raises(ValueError):
        appointment.cancel()
    assert appointment.status is AppointmentStatus.CANCELLED
    assert appointment.appointment_id == "A1"
    assert appointment.patient is patient
    assert appointment.practitioner is practitioner
    assert appointment.date_time == date_time

def test_completed_appointment_cancellation() -> None:
    """Verify completed appointments cannot be cancelled."""
    patient = Patient("P1", "Alex")
    practitioner = Practitioner("DR1", "Dr Smith", "GP")
    date_time = datetime(2026, 10, 28, 10, 0)
    # Create an appointment with initial COMPLETED status
    appointment = Appointment("A1", patient, practitioner, date_time, AppointmentStatus.COMPLETED)
    with pytest.raises(ValueError):
        appointment.cancel()
    # Verify appointment details remain unchanged
    assert appointment.status is AppointmentStatus.COMPLETED
    assert appointment.appointment_id == "A1"
    assert appointment.patient is patient
    assert appointment.practitioner is practitioner
    assert appointment.date_time == date_time

def test_appointment_read_only_properties() -> None:
    """Verify appointment properties cannot be changed directly."""
    patient = Patient("P1", "Alex")
    practitioner = Practitioner("DR1", "Dr Smith", "GP")
    date_time = datetime(2026, 10, 28, 10, 0)
    appointment = Appointment("A1", patient, practitioner, date_time)

    # Verify appointment ID cannot be changed
    with pytest.raises(AttributeError):
        appointment.appointment_id = "A2"

    # Verify patient cannot be changed
    with pytest.raises(AttributeError):
        appointment.patient = Patient("P2", "Sam")

    # Verify practitioner cannot be changed
    with pytest.raises(AttributeError):
        appointment.practitioner = Practitioner("DR2", "Dr Lee", "GP")

    # Verify date and time cannot be changed
    with pytest.raises(AttributeError):
        appointment.date_time = datetime(2026, 10, 29, 11, 0)

    # Verify status cannot be changed directly
    with pytest.raises(AttributeError):
        appointment.status = AppointmentStatus.CANCELLED

    # Verify appointment details remain unchanged
    assert appointment.appointment_id == "A1"
    assert appointment.patient is patient
    assert appointment.practitioner is practitioner
    assert appointment.date_time == date_time
    assert appointment.status is AppointmentStatus.SCHEDULED
