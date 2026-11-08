from datetime import datetime, timezone

import pytest

from smartcare.data_store import SmartCareDataStore
from smartcare.domain import (
    Appointment,
    AppointmentStatus,
    Patient,
    Practitioner,
)
from smartcare.services import (
    AppointmentService,
    PatientService,
    PractitionerService,
)


@pytest.fixture
def domain_appointment():
    return Appointment(
        "A1",
        Patient("P1", "Alex Example"),
        Practitioner("D1", "Taylor Example", "General"),
        datetime(2026, 11, 10, 9, 0),
    )


def appointment_state(appointment):
    return (
        appointment.appointment_id,
        appointment.patient,
        appointment.practitioner,
        appointment.date_time,
        appointment.status,
    )


def store_snapshot(store):
    return [
        (appointment, appointment_state(appointment))
        for appointment in store.list_appointments()
    ]


def assert_store_matches_snapshot(store, snapshot):
    current = store.list_appointments()
    assert len(current) == len(snapshot)
    for actual, (expected, expected_state) in zip(current, snapshot, strict=True):
        assert actual is expected
        assert appointment_state(actual) == expected_state


def test_domain_reschedule_changes_only_time(domain_appointment):
    appointment = domain_appointment
    patient = appointment.patient
    practitioner = appointment.practitioner
    new_time = datetime(2026, 11, 10, 11, 0)

    result = appointment.reschedule(new_time)

    assert result is None
    assert appointment.appointment_id == "A1"
    assert appointment.patient is patient
    assert appointment.practitioner is practitioner
    assert appointment.date_time == new_time
    assert appointment.status is AppointmentStatus.SCHEDULED


def test_domain_reschedule_same_time_is_a_no_op(domain_appointment):
    appointment = domain_appointment
    before = appointment_state(appointment)

    result = appointment.reschedule(appointment.date_time)

    assert result is None
    assert appointment_state(appointment) == before


@pytest.mark.parametrize(
    "new_date_time",
    [
        None,
        "2026-11-10 11:00",
        123,
        datetime(2026, 11, 10, 11, 0, tzinfo=timezone.utc),
        datetime(2026, 11, 10, 11, 0, 1),
        datetime(2026, 11, 10, 11, 0, 0, 1),
    ],
)
def test_domain_reschedule_invalid_datetime_does_not_mutate(
    domain_appointment,
    new_date_time,
):
    appointment = domain_appointment
    before = appointment_state(appointment)

    with pytest.raises(ValueError):
        appointment.reschedule(new_date_time)

    assert appointment_state(appointment) == before


@pytest.mark.parametrize(
    "status",
    [AppointmentStatus.CANCELLED, AppointmentStatus.COMPLETED],
)
@pytest.mark.parametrize("same_time", [True, False])
def test_domain_reschedule_rejects_non_scheduled_without_mutation(
    status,
    same_time,
):
    original_time = datetime(2026, 11, 10, 9, 0)
    appointment = Appointment(
        "A1",
        Patient("P1", "Alex Example"),
        Practitioner("D1", "Taylor Example", "General"),
        original_time,
        status,
    )
    before = appointment_state(appointment)
    new_date_time = (
        original_time if same_time else datetime(2026, 11, 10, 11, 0)
    )

    with pytest.raises(ValueError):
        appointment.reschedule(new_date_time)

    assert appointment_state(appointment) == before


@pytest.fixture
def rescheduling_setup():
    store = SmartCareDataStore()
    patient = PatientService(store).register_patient("P1", "Alex Example")
    practitioner_service = PractitionerService(store)
    practitioner = practitioner_service.register_practitioner(
        "D1", "Taylor Example", "General"
    )
    other_practitioner = practitioner_service.register_practitioner(
        "D2", "Morgan Example", "General"
    )
    service = AppointmentService(store)
    appointment = service.book_appointment(
        "A1", "P1", "D1", datetime(2026, 11, 10, 9, 0)
    )
    return (
        store,
        service,
        patient,
        practitioner,
        other_practitioner,
        appointment,
    )


def test_reschedule_preserves_identity_updates_lookup_listing_and_releases_old_slot(
    rescheduling_setup,
):
    store, service, patient, practitioner, _, appointment = rescheduling_setup
    middle = service.book_appointment(
        "A2", "P1", "D1", datetime(2026, 11, 10, 10, 0)
    )

    moved = service.reschedule_appointment(
        "A1", datetime(2026, 11, 10, 11, 0)
    )

    assert moved is appointment
    assert appointment.appointment_id == "A1"
    assert appointment.patient is patient
    assert appointment.practitioner is practitioner
    assert appointment.date_time == datetime(2026, 11, 10, 11, 0)
    assert appointment.status is AppointmentStatus.SCHEDULED
    assert service.find_appointment("A1") is appointment
    assert store.find_appointment("A1") is appointment
    assert service.list_practitioner_appointments("D1") == [
        middle,
        appointment,
    ]

    released_slot = service.book_appointment(
        "A3", "P1", "D1", datetime(2026, 11, 10, 9, 0)
    )
    assert service.list_practitioner_appointments("D1") == [
        released_slot,
        middle,
        appointment,
    ]


def test_reschedule_to_same_time_is_a_no_op(rescheduling_setup):
    store, service, _, _, _, appointment = rescheduling_setup
    before = appointment_state(appointment)

    result = service.reschedule_appointment("A1", appointment.date_time)

    assert result is appointment
    assert appointment_state(appointment) == before
    assert store.list_appointments() == [appointment]


def test_reschedule_allows_time_used_by_another_practitioner(
    rescheduling_setup,
):
    store, service, patient, _, other_practitioner, appointment = (
        rescheduling_setup
    )
    other = Appointment(
        "A2",
        patient,
        other_practitioner,
        datetime(2026, 11, 10, 11, 0),
    )
    store.add_appointment(other)

    assert service.reschedule_appointment(
        "A1", datetime(2026, 11, 10, 11, 0)
    ) is appointment
    assert appointment.date_time == other.date_time


@pytest.mark.parametrize(
    "blocker_status",
    [AppointmentStatus.CANCELLED, AppointmentStatus.COMPLETED],
)
def test_reschedule_ignores_non_scheduled_appointments_at_destination(
    rescheduling_setup,
    blocker_status,
):
    store, service, patient, practitioner, _, appointment = rescheduling_setup
    blocker = Appointment(
        "A2",
        patient,
        practitioner,
        datetime(2026, 11, 10, 11, 0),
        blocker_status,
    )
    store.add_appointment(blocker)

    assert service.reschedule_appointment(
        "A1", datetime(2026, 11, 10, 11, 0)
    ) is appointment
    assert appointment.date_time == blocker.date_time


def test_reschedule_conflict_excludes_only_target_and_does_not_mutate(
    rescheduling_setup,
):
    store, service, _, practitioner, _, appointment = rescheduling_setup
    blocker = Appointment(
        "A2",
        appointment.patient,
        practitioner,
        datetime(2026, 11, 10, 11, 0),
    )
    store.add_appointment(blocker)
    before = store_snapshot(store)

    with pytest.raises(ValueError):
        service.reschedule_appointment("A1", blocker.date_time)

    assert_store_matches_snapshot(store, before)


@pytest.mark.parametrize(
    "appointment_id, error",
    [
        ("UNKNOWN", LookupError),
        ("", ValueError),
        ("   ", ValueError),
        (None, ValueError),
        (123, ValueError),
    ],
)
def test_reschedule_rejects_invalid_or_unknown_ids_without_mutation(
    rescheduling_setup,
    appointment_id,
    error,
):
    store, service, _, _, _, _ = rescheduling_setup
    before = store_snapshot(store)

    with pytest.raises(error):
        service.reschedule_appointment(
            appointment_id, datetime(2026, 11, 10, 11, 0)
        )

    assert_store_matches_snapshot(store, before)


@pytest.mark.parametrize(
    "new_date_time",
    [
        None,
        "2026-11-10 11:00",
        123,
        datetime(2026, 11, 10, 11, 0, tzinfo=timezone.utc),
        datetime(2026, 11, 10, 11, 0, 1),
        datetime(2026, 11, 10, 11, 0, 0, 1),
    ],
)
def test_reschedule_rejects_invalid_datetimes_without_mutation(
    rescheduling_setup,
    new_date_time,
):
    store, service, _, _, _, _ = rescheduling_setup
    before = store_snapshot(store)

    with pytest.raises(ValueError):
        service.reschedule_appointment("A1", new_date_time)

    assert_store_matches_snapshot(store, before)


@pytest.mark.parametrize(
    "status",
    [AppointmentStatus.CANCELLED, AppointmentStatus.COMPLETED],
)
@pytest.mark.parametrize("same_time", [True, False])
def test_non_scheduled_appointment_cannot_be_rescheduled(
    rescheduling_setup,
    status,
    same_time,
):
    store, service, patient, practitioner, _, scheduled = rescheduling_setup
    date_time = scheduled.date_time
    appointment = Appointment("A2", patient, practitioner, date_time, status)
    store.add_appointment(appointment)
    requested_time = (
        date_time if same_time else datetime(2026, 11, 10, 11, 0)
    )
    before = store_snapshot(store)

    with pytest.raises(ValueError):
        service.reschedule_appointment("A2", requested_time)

    assert_store_matches_snapshot(store, before)
    assert service.find_appointment("A2") is appointment
