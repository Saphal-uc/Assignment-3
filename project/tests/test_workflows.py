"""Integration tests for complete SmartCare workflows."""

from datetime import datetime

import pytest

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

    patient = patient_service.register_patient("P1", "Alex Example")
    practitioner = practitioner_service.register_practitioner(
        "D1", "Taylor Example", "General"
    )

    assert patient_service.find_patient("P1") is patient
    assert practitioner_service.find_practitioner("D1") is practitioner

    appointment = appointment_service.book_appointment(
        "A1",
        "P1",
        "D1",
        datetime(2026, 11, 10, 9, 0),
    )

    assert appointment.status is AppointmentStatus.SCHEDULED
    assert appointment_service.find_appointment("A1") is appointment

    cancelled = appointment_service.cancel_appointment("A1")

    assert cancelled is appointment
    assert appointment.status is AppointmentStatus.CANCELLED
    assert appointment_service.find_appointment("A1") is appointment

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

    all_results = service.list_practitioner_appointments("D1")
    assert all_results == [first, second]

    scheduled_results = service.list_practitioner_appointments(
        "D1", AppointmentStatus.SCHEDULED
    )
    assert scheduled_results == [second]

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


def test_booking_conflict_preserves_original_and_allows_retry():
    """A rejected booking leaves the original intact and its new ID available."""

    store = SmartCareDataStore()
    patients = PatientService(store)
    practitioners = PractitionerService(store)
    appointments = AppointmentService(store)

    patient = patients.register_patient("P1", "Alex Example")
    d1 = practitioners.register_practitioner(
        "D1", "Taylor Example", "General"
    )
    d2 = practitioners.register_practitioner(
        "D2", "Morgan Example", "General"
    )

    when = datetime(2026, 10, 1, 9, 0)

    original = appointments.book_appointment("A1", "P1", "D1", when)

    with pytest.raises(ValueError):
        appointments.book_appointment("A2", "P1", "D1", when)

    assert appointments.find_appointment("A1") is original
    assert original.patient is patient
    assert original.practitioner is d1
    assert original.date_time == when
    assert original.status is AppointmentStatus.SCHEDULED
    assert store.list_appointments() == [original]
    assert store.find_appointment("A2") is None

    retry = appointments.book_appointment("A2", "P1", "D2", when)

    assert appointments.find_appointment("A2") is retry
    assert retry.patient is patient
    assert retry.practitioner is d2
    assert retry.date_time == when
    assert retry.status is AppointmentStatus.SCHEDULED


def test_cancellation_frees_slot_but_preserves_appointment_history():
    """A cancelled appointment keeps its ID, but its time slot can be reused."""

    store = SmartCareDataStore()
    patients = PatientService(store)
    practitioners = PractitionerService(store)
    appointments = AppointmentService(store)

    patients.register_patient("P1", "Alex Example")
    practitioners.register_practitioner(
        "D1", "Taylor Example", "General"
    )

    when = datetime(2026, 10, 1, 9, 0)

    original = appointments.book_appointment("A1", "P1", "D1", when)

    assert appointments.cancel_appointment("A1") is original
    assert original.status is AppointmentStatus.CANCELLED

    with pytest.raises(ValueError):
        appointments.book_appointment("A1", "P1", "D1", when)

    assert appointments.find_appointment("A1") is original
    assert store.list_appointments() == [original]

    replacement = appointments.book_appointment("A2", "P1", "D1", when)

    assert appointments.find_appointment("A1") is original
    assert original.status is AppointmentStatus.CANCELLED
    assert appointments.find_appointment("A2") is replacement
    assert replacement.status is AppointmentStatus.SCHEDULED
    assert replacement.practitioner is original.practitioner
    assert replacement.date_time == when
    assert len(store.list_appointments()) == 2


def test_unknown_patient_booking_can_be_retried_after_registration():
    """A failed booking must not reserve the appointment ID or time slot."""

    store = SmartCareDataStore()
    patients = PatientService(store)
    practitioners = PractitionerService(store)
    appointments = AppointmentService(store)

    practitioner = practitioners.register_practitioner(
        "D1", "Taylor Example", "General"
    )

    when = datetime(2026, 10, 1, 9, 0)

    with pytest.raises(LookupError):
        appointments.book_appointment("A1", "P1", "D1", when)

    assert store.find_patient("P1") is None
    assert store.list_appointments() == []

    patient = patients.register_patient("P1", "Alex Example")
    booked = appointments.book_appointment("A1", "P1", "D1", when)

    assert appointments.find_appointment("A1") is booked
    assert booked.patient is patient
    assert booked.practitioner is practitioner
    assert booked.date_time == when
    assert booked.status is AppointmentStatus.SCHEDULED
    assert store.list_appointments() == [booked]