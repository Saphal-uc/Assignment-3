# SmartCare Clinic Appointment Booking System

## 1. Project Overview

SmartCare is a Python-based appointment booking system developed for Software Technology 1 Assignment 3.

The application supports patient and practitioner registration and lookup, appointment booking, conflict checking, cancellation, appointment history and appointment queries.

The project was developed incrementally through the applicable assignment stages.

## 2. Features and Scope

### Common UG and PG functionality

* Register and find patients.
* Register and find practitioners.
* Book appointments.
* Prevent conflicting appointments for the same practitioner.
* Cancel scheduled appointments while retaining appointment history.
* Find and list appointments.
* Filter and sort appointment results.
* Handle invalid input and recover from errors through the console interface.

### Additional PG functionality

* Reschedule eligible appointments.
* Validate rescheduling rules and appointment conflicts.
* Preserve appointment identity and participants.
* Verify that failed rescheduling does not mutate appointment data.

## 3. Technology and Dependencies

* Programming language: Python 3.14.3 (local verified environment).
* Testing framework: pytest 8.3.5
* Runtime application: Python standard library.
* Development dependency: pytest 8.3.5

## 4. Setup and Installation

From the repository root:
cd project

Install development dependencies:

```bash
python -m pip install -r requirements-dev.txt
```

Check Python:

```bash
python --version
```

## 5. Running the Application

From the project/ directory:

```bash
python main.py
```

For interactive mode:

```bash
python main.py --interactive
```

## 6. Running Automated Tests

Run the complete test suite:

```bash
python -m pytest -q
```

The latest recorded local test run used Python 3.14.3 and reported 139 passed tests in 0.13 seconds. This result must be associated with the exact tested commit.

## 7. Project Structure

project/
├── main.py
├── requirements-dev.txt
├── README.md
├── smartcare/
│   ├── __init__.py
│   ├── console.py
│   ├── data_store.py
│   ├── domain.py
│   ├── queries.py
│   └── services.py
└── tests/
    ├── test_domain.py
    ├── test_queries.py
    ├── test_regressions.py
    ├── test_rescheduling.py
    ├── test_services.py
    ├── test_starter.py
    └── test_workflows.py

## 8. Application Architecture

* domain.py: Defines the main entities, appointment status and domain rules.
* data_store.py: Maintains patient, practitioner and appointment collections during the application session.
* services.py: Coordinates registration, lookup, booking, cancellation and rescheduling operations.
* queries.py: Provides appointment selection, filtering and sorting operations.
* console.py: Handles user interaction, menus, input and error messages.
* main.py: Starts the application.

## 9. Data Handling and Limitations

The application uses in-memory, session-only data storage. Records are lost when the application exits.

Use synthetic information only. Do not enter real patient information or confidential data.

The application is an educational prototype, not a production healthcare information system.

Production authentication, role management, patient portals, notifications, billing, insurance processing and clinical AI are outside the current project scope.

## 10. Responsible AI Use

AI-assisted development tools may support brainstorming, code suggestions and testing ideas. Generated suggestions must be reviewed, tested and verified by human developers.

The group remains responsible for the final implementation, testing, documentation and release decisions.

## 11. Release and Verification

The final release label, tested commit SHA, submitted commit SHA and release evidence are recorded in the repository’s Stage 12 activities and evidence document.