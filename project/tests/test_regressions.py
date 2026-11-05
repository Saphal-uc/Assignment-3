import pytest
from datetime import datetime

from smartcare import data_store
from smartcare.data_store import SmartCareDataStore
from smartcare.services import PatientService, PractitionerService, AppointmentService

def setup_booking():
    """Create a data store, register two patients and two practitioners."""
    data_store = SmartCareDataStore()
    patient_service = PatientService(data_store)
    practitioner_service = PractitionerService(data_store)
    appointment_service = AppointmentService(data_store)

    patient_service.register_patient("P1", "Alice")
    patient_service.register_patient("P2", "Bob")
    practitioner_service.register_practitioner("D1", "Taylor Example", "General")
    practitioner_service.register_practitioner("D2", "Tom Example", "General")
    return data_store, appointment_service

def test_f8_01_same_practitioner_conflict():
    data_store, appointment_service = setup_booking()
    date_time = datetime(2026, 11, 5, 10)
    appointment = appointment_service.book_appointment("A1", "P1", "D1", date_time)

    # Check the same practitioner at the same time with different patients
    with pytest.raises(ValueError):
        appointment_service.book_appointment("A2", "P2", "D1", date_time)
    assert len(data_store.list_appointments()) == 1
    # Check that the original appointment A1 is still the same object
    assert data_store.find_appointment("A1") is appointment

def test_f8_01_different_practitioner():
    data_store, appointment_service = setup_booking()
    date_time = datetime(2026, 11, 5, 10)
    appointment_service.book_appointment("A1", "P1", "D1", date_time)

    # Check different practitioners at the same time
    appointment_service.book_appointment("A2", "P2", "D2", date_time)
    assert len(data_store.list_appointments()) == 2