"""Integration tests for complete SmartCare workflows."""

from datetime import datetime

from smartcare.console import run_menu
from smartcare.data_store import SmartCareDataStore
from smartcare.domain import AppointmentStatus
from smartcare.services import (
    AppointmentService,
    PatientService,
    PractitionerService,
)


def test_complete_appointment_workflow():
    """Register participants, book, cancel and retrieve appointments."""

    store = SmartCareDataStore()

    patient_service = PatientService(store)
    practitioner_service = PractitionerService(store)
    appointment_service = AppointmentService(store)

    # Register a patient and practitioner.
    patient = patient_service.register_patient(
        "P1", "Alex Example"
    )
    practitioner = practitioner_service.register_practitioner(
        "D1", "Taylor Example", "General"
    )

    # Verify registration and lookup.
    assert patient_service.find_patient("P1") is patient
    assert practitioner_service.find_practitioner("D1") is practitioner

    # Book an appointment.
    appointment = appointment_service.book_appointment(
        "A1",
        "P1",
        "D1",
        datetime(2026, 11, 10, 9, 0),
    )

    assert appointment.status is AppointmentStatus.SCHEDULED
    assert appointment_service.find_appointment("A1") is appointment

    # Cancel the appointment.
    cancelled = appointment_service.cancel_appointment("A1")

    assert cancelled is appointment
    assert appointment.status is AppointmentStatus.CANCELLED

    # Verify the cancelled appointment remains stored.
    assert appointment_service.find_appointment("A1") is appointment

    # Verify default listing includes cancelled appointments.
    results = appointment_service.list_practitioner_appointments("D1")

    assert results == [appointment]
    assert results[0].status is AppointmentStatus.CANCELLED

def test_workflow_lists_only_requested_status():
    """Verify appointment history can be filtered by status."""

    store = SmartCareDataStore()

    PatientService(store).register_patient("P1", "Alex Example")
    PractitionerService(store).register_practitioner(
        "D1", "Taylor Example", "General"
    )

    service = AppointmentService(store)

    first = service.book_appointment(
        "A1", "P1", "D1", datetime(2026, 11, 10, 9, 0)
    )

    second = service.book_appointment(
        "A2", "P1", "D1", datetime(2026, 11, 10, 10, 0)
    )

    service.cancel_appointment("A1")

    # All statuses should include both appointments.
    all_results = service.list_practitioner_appointments("D1")
    assert all_results == [first, second]

    # Scheduled filter should include only A2.
    scheduled_results = service.list_practitioner_appointments(
        "D1", AppointmentStatus.SCHEDULED
    )
    assert scheduled_results == [second]

    # Cancelled filter should include only A1.
    cancelled_results = service.list_practitioner_appointments(
        "D1", AppointmentStatus.CANCELLED
    )
    assert cancelled_results == [first]

def test_console_menu_exits_cleanly(monkeypatch, capsys):
    """Verify the interactive menu exits when the user enters 0."""

    monkeypatch.setattr("builtins.input", lambda prompt="": "0")

    run_menu()

    output = capsys.readouterr().out

    assert "SmartCare Clinic Menu" in output
    assert "Exiting SmartCare" in output
    assert "Session-only data will be lost" in output