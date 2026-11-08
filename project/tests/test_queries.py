from datetime import datetime

import pytest

from smartcare.domain import (
    Appointment,
    AppointmentStatus,
    Patient,
    Practitioner,
)
from smartcare.queries import (
    appointment_sort_key,
    select_appointments,
)


@pytest.fixture
def query_setup():
    """Create patients, practitioners and appointments for query tests."""

    patient = Patient("P1", "Alex")
    practitioner1 = Practitioner("D1", "Dr Smith", "GP")
    practitioner2 = Practitioner("D2", "Dr Lee", "GP")

    a1 = Appointment(
        "A1", patient, practitioner1, datetime(2026, 11, 5, 10, 0)
    )
    a2 = Appointment(
        "A2", patient, practitioner1, datetime(2026, 11, 5, 9, 0)
    )
    a3 = Appointment(
        "A3", patient, practitioner2, datetime(2026, 11, 5, 8, 0)
    )

    a4 = Appointment(
        "A4",
        patient,
        practitioner1,
        datetime(2026, 11, 5, 11, 0),
        AppointmentStatus.COMPLETED,
    )

    a5 = Appointment(
        "A5", patient, practitioner1, datetime(2026, 11, 5, 12, 0)
    )
    a5.cancel()

    return [a1, a2, a3, a4, a5]


def test_appointment_sort_key(query_setup):
    """Return date/time and appointment ID as the sorting key."""

    appointment = query_setup[0]

    assert appointment_sort_key(appointment) == (
        appointment.date_time,
        appointment.appointment_id,
    )


def test_select_appointments_filters_by_practitioner(query_setup):
    """Return only appointments belonging to the selected practitioner."""

    result = select_appointments(query_setup, "D1")

    assert len(result) == 4
    assert all(
        appointment.practitioner.practitioner_id == "D1"
        for appointment in result
    )


def test_select_appointments_excludes_other_practitioner(query_setup):
    """Do not include another practitioner's appointments."""

    result = select_appointments(query_setup, "D1")

    assert all(
        appointment.practitioner.practitioner_id != "D2"
        for appointment in result
    )


def test_select_appointments_without_status_includes_all_statuses(
    query_setup,
):
    """Include scheduled, completed and cancelled appointments by default."""

    result = select_appointments(query_setup, "D1")

    statuses = {appointment.status for appointment in result}

    assert statuses == {
        AppointmentStatus.SCHEDULED,
        AppointmentStatus.COMPLETED,
        AppointmentStatus.CANCELLED,
    }


@pytest.mark.parametrize(
    "status",
    [
        AppointmentStatus.SCHEDULED,
        AppointmentStatus.COMPLETED,
        AppointmentStatus.CANCELLED,
    ],
)
def test_select_appointments_filters_by_status(query_setup, status):
    """Return only appointments matching the requested status."""

    result = select_appointments(query_setup, "D1", status)

    assert all(appointment.status is status for appointment in result)


def test_select_appointments_no_matches_returns_empty_list(query_setup):
    """Return an empty list when no appointments match."""

    result = select_appointments(query_setup, "D99")

    assert result == []


def test_select_appointments_sorted_by_date_time(query_setup):
    """Sort appointments from earliest to latest."""

    result = select_appointments(query_setup, "D1")

    times = [appointment.date_time for appointment in result]

    assert times == sorted(times)


def test_select_appointments_tie_breaks_by_appointment_id():
    """Sort appointments with equal times by appointment ID."""

    patient = Patient("P1", "Alex")
    practitioner = Practitioner("D1", "Dr Smith", "GP")
    when = datetime(2026, 11, 5, 10, 0)

    a3 = Appointment("A3", patient, practitioner, when)
    a1 = Appointment("A1", patient, practitioner, when)
    a2 = Appointment("A2", patient, practitioner, when)

    result = select_appointments([a3, a1, a2], "D1")

    assert [appointment.appointment_id for appointment in result] == [
        "A1", "A2", "A3"
    ]


def test_select_appointments_does_not_change_source_list(query_setup):
    """Keep the original appointment list order unchanged."""

    original = list(query_setup)

    select_appointments(query_setup, "D1")

    assert query_setup == original


def test_select_appointments_returns_new_list(query_setup):
    """Return a different list without replacing appointment objects."""

    result = select_appointments(query_setup, "D1")

    assert result is not query_setup

    for appointment in result:
        assert appointment in query_setup


def test_select_appointments_empty_input_returns_new_list():
    """Return a new empty list for empty input."""

    appointments = []

    result = select_appointments(appointments, "D1")

    assert result == []
    assert result is not appointments


def test_select_appointments_does_not_change_appointment_objects(
    query_setup,
):
    """Preserve appointment IDs, dates and statuses."""

    original = [
        (
            appointment.appointment_id,
            appointment.date_time,
            appointment.status,
        )
        for appointment in query_setup
    ]

    select_appointments(query_setup, "D1")

    after = [
        (
            appointment.appointment_id,
            appointment.date_time,
            appointment.status,
        )
        for appointment in query_setup
    ]

    assert after == original