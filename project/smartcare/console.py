"""Console helpers and a small runnable starting demonstration."""


import re
from datetime import datetime

from smartcare.data_store import SmartCareDataStore
from smartcare.domain import Appointment, AppointmentStatus
from smartcare.services import (
    AppointmentService,
    PatientService,
    PractitionerService,
)


def parse_date_time(text: str) -> datetime:
    """Parse YYYY-MM-DD HH:MM; raise ValueError for invalid input."""
    if (
        not isinstance(text, str)
        or re.fullmatch(
            '[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}', text
        ) is None
    ):
        raise ValueError('Use date/time format YYYY-MM-DD HH:MM')
    try:
        return datetime.strptime(text, '%Y-%m-%d %H:%M')
    except ValueError:
        raise ValueError(
            'Invalid calendar date/time; use YYYY-MM-DD HH:MM',
        ) from None


def format_appointment(appointment: Appointment) -> str:
    """Return readable synthetic appointment details without changing
    state.
    """
    return (
        f'{appointment.appointment_id}: '
        f'{appointment.patient.patient_id} with '
        f'{appointment.practitioner.practitioner_id}, '
        f'{appointment.date_time:%Y-%m-%d %H:%M}, {appointment.status.value}'
    )


def run_demo() -> None:
    """Demonstrate supplied registration and booking using synthetic
    records.
    """
    data_store = SmartCareDataStore()
    patients = PatientService(data_store)
    practitioners = PractitionerService(data_store)
    appointments = AppointmentService(data_store)
    patients.register_patient('P1', 'Alex Example')
    practitioners.register_practitioner(
        'DR1',
        'Taylor Example',
        'General practice',
    )
    try:
        appointments.book_appointment(
            'A1',
            'P1',
            'DR1',
            parse_date_time('2026-10-01 09:00'),
        )
        print(format_appointment(appointments.find_appointment('A1')))
    except (ValueError, LookupError) as error:
        print(f'Error: {error}')
    print('Session-only data: records are lost on exit.')

def register_patient_menu(patients) -> None:
    patient_id = input("Patient ID: ").strip()
    name = input("Patient name: ").strip()
    patients.register_patient(patient_id, name)

    print("\nPatient registered successfully.")
    print(f"patient_id: {patient_id}")
    print(f"name: {name}")

def find_patient_menu(patients) -> None:
    patient_id = input("Patient ID: ").strip()
    patient = patients.find_patient(patient_id)

    print(f"\nPatient found: {patient_id} {patient.name}")

def register_practitioner_menu(practitioners) -> None:
    practitioner_id = input("Practitioner ID: ").strip()
    name = input("Practitioner name: ").strip()
    specialty = input("Practitioner specialty: ").strip()
    practitioners.register_practitioner(practitioner_id, name, specialty)

    print("\nPractitioner registered successfully.\n")
    print(f"practitioner_id: {practitioner_id}")
    print(f"name: {name}")
    print(f"specialty: {specialty}")

def find_practitioner_menu(practitioners) -> None:
    practitioner_id = input("Practitioner ID: ").strip()
    practitioner = practitioners.find_practitioner(practitioner_id)
    print(f"\nPractitioner found: {practitioner_id}, {practitioner.name}, {practitioner.specialty}")

def book_appointment_menu(appointments) -> None:
    appointment_id = input("Appointment ID: ").strip()
    patient_id = input("Patient ID: ").strip()
    practitioner_id = input("Practitioner ID: ").strip()
    date_time_text = input("Date/time [YYYY-MM-DD HH:MM]: ").strip()
    date_time = parse_date_time(date_time_text)
    appointment = appointments.book_appointment(appointment_id, patient_id, practitioner_id, date_time)

    print("Appointment created successfully.")
    print(format_appointment(appointment))

def cancel_appointment_menu(appointments) -> None:
    appointment_id = input("Appointment ID: ").strip()
    appointment = appointments.cancel_appointment(appointment_id)

    print(f"\nAppointment canceled successfully: {appointment_id}")
    print(format_appointment(appointment))

def find_appointment_menu(appointments) -> None:
    appointment_id = input("Appointment ID: ").strip()
    appointment = appointments.find_appointment(appointment_id)

    print(f"Appointment found: {appointment_id}")
    print(format_appointment(appointment))

def list_practitioner_appointments_menu(practitioners, appointments) -> None:
    practitioner_id = input("Practitioner ID: ").strip()
    status_input = input("Status filter [scheduled/cancelled/completed, blank = all]:  ").strip().lower()

    if status_input == "":
        status = None

    elif status_input in ("scheduled", "cancelled", "completed"):
        status = AppointmentStatus(status_input)

    else:
        raise ValueError("Invalid status filter.")

    practitioner = practitioners.find_practitioner(practitioner_id)
    appointment_list = appointments.list_practitioner_appointments(practitioner_id, status)

    print(f"\nAppointments for {practitioner.name} ({practitioner_id})")
    if not appointment_list:
        print("No appointments found.")
    else:
        for appointment in appointment_list:
            print(format_appointment(appointment))

        print(f"{len(appointment_list)} appointment(s) found.")

def run_menu() -> None:
    """implement the register/find/book/cancel/list/exit menu. """
    data_store = SmartCareDataStore()
    patients = PatientService(data_store)
    practitioners = PractitionerService(data_store)
    appointments = AppointmentService(data_store)

    # Set the menu width to 62 characters
    width = 62

    print("=" * width)
    print("SMARTCARE".center(width))
    print("Interactive Console".center(width))
    print("=" * width)
    print("Session data is temporary and will be discarded when you exit.")


    while True:
        # Display the menu
        print("\nMAIN MENU")
        print("-" * width)
        print("[1] Register patient")
        print("[2] Find patient")
        print("[3] Register practitioner")
        print("[4] Find practitioner")
        print("[5] Book appointment")
        print("[6] Cancel appointment")
        print("[7] Find appointment")
        print("[8] List practitioner appointments")
        print("[0] Exit")
        print("-" * width)

        choice: str = input("Select an option: ").strip()

        try:
            if choice == "0":
                print("Exiting...")
                break

            elif choice == "1":
                register_patient_menu(patients)

            elif choice == "2":
                find_patient_menu(patients)

            elif choice == "3":
                register_practitioner_menu(practitioners)

            elif choice == "4":
                find_practitioner_menu(practitioners)

            elif choice == "5":
                book_appointment_menu(appointments)

            elif choice == "6":
                cancel_appointment_menu(appointments)

            elif choice == "7":
                find_appointment_menu(appointments)

            elif choice == "8":
                list_practitioner_appointments_menu(practitioners, appointments)

            else:
                print("Invalid input, please try again.")
                print("Choose a number from 0 to 8.")

        except (ValueError, LookupError) as error:
            print(f'Error: {error}')