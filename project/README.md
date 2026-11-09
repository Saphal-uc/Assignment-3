# SmartCare Appointment System

Requirements baseline: SmartCare A3 2026 revision 2. Python 3.13 and pytest 8.3.5 verified. Runtime uses only the standard library.

From this directory, using a Python environment with the development dependency installed:

```sh
python main.py
python -m pytest
```

If needed in your approved environment: `python -m pip install -r requirements-dev.txt`.

The demo registers synthetic records and books/finds an appointment. All supplied tests pass. Data exists only in this session and is lost on exit; FR-10 restart persistence is retired. Use synthetic information only.

`domain.py` contains the entities, status and guarded cancellation. `data_store.py` holds three dictionaries through add/find/list methods. The three services share that object. Supplied registration, booking, appointment lookup and conflict checking work. IDs are trimmed, non-blank and case-sensitive. Properties provide read-only identity/appointment state; changes go through domain methods. No special architecture terminology is required.

Stage 6 completed service patient/practitioner lookup and appointment cancellation. Stage 7 added Domain and Service tests for validation and boundary cases. Stage 8 fixed defects, added regression tests and completed refactoring. Stage 9 completed pure queries, the named sort key, service listing and the interactive menu. Stage 10 (PG) added appointment rescheduling in `domain.py` and `services.py`, with new tests in `test_rescheduling.py`.

Service booking accepts IDs and a `datetime` (local, minute precision). Console parser accepts exactly `YYYY-MM-DD HH:MM`. Store lookups return None when absent; service lookups raise LookupError. Invalid values, duplicates, conflicts and illegal transitions raise ValueError. Lists are new containers holding the stored objects. No age, duration, patient-conflict or past-date rules apply.

Stage 10 only allows SCHEDULED appointments to be rescheduled. The new time must be valid and must not conflict with another SCHEDULED appointment for the same practitioner. The original appointment ID, patient and practitioner stay unchanged. CANCELLED and COMPLETED appointments cannot be rescheduled.

Stage 10 rescheduling tests can be run from `project/`:

```sh
python -m pytest -q tests/test_rescheduling.py
```

The Stage 10 tests passed: 33 passed. The full test suite passed: 139 passed.