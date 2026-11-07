# Stage 7 Testing and Verification Record

Group/tutorial: [complete]  Members/cohorts: [complete]
Requirements baseline: SmartCare A3 Requirements Baseline 2026, revision 2.
Use the same project/. Link actual evidence; keep responses concise. Blank fields are for your group. Copy rows only as needed.

All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage07/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions.

## A Tutorial Activities

### Activity 1 Requirement to test

For each requirement, propose one positive test, one negative test and the key assertion.

| Requirement | Positive test | Negative test | Key assertion |
|---|---|---|---|
| FR-01 Register patient | Register a patient with valid details and an unused patient ID. | Attempt to register another patient using an existing patient ID. | The valid patient is stored successfully, while duplicate registration raises the expected error. |
| FR-05 Prevent practitioner conflict | Book an appointment with a practitioner who has no appointment at the selected time. | Attempt to book another appointment with the same practitioner at the same time while the existing appointment is scheduled. | The conflicting booking raises `ValueError`, and the original appointment remains unchanged. |
| FR-06 Cancel appointment | Cancel an appointment with `SCHEDULED` status. | Attempt to cancel an appointment that is already cancelled or completed. | The appointment status changes to `CANCELLED`; an invalid cancellation raises `ValueError`. |
| FR-07 Retain cancelled history | Cancel an appointment and retrieve it again using its appointment ID. | Attempt to retrieve an appointment using an unknown ID. | The cancelled appointment remains stored and retrievable with its original details; an unknown ID raises `LookupError`. |
### Activity 2 Strong or weak assertion

For each, select Strong for stated behaviour or Weak/unclear and explain why. State the behaviour and limits.

**`assert True`**

Judgement: Weak/unclear.

Why: It only checks a constant value and does not verify any actual system behaviour. It can pass even when the required functionality is incorrect.

**`assert appointment is not None`**

Judgement: Weak/unclear.

Why: It only checks whether an object exists. It does not prove that the correct appointment was returned or that its details are correct.

**`assert appointment.status == AppointmentStatus.CANCELLED`**

Judgement: Strong for stated behaviour.

Why: It directly checks whether the appointment status has changed to `CANCELLED`. However, it does not check whether the other appointment details remain unchanged.

**`assert len(results) > 0`**

Judgement: Weak/unclear.

Why: It only checks that the results contain at least one item. It does not prove that the correct record is included.

**`assert data_store.find_appointment('A1') is appointment`**

Judgement: Strong for stated behaviour.

Why: It checks that the data store returns the exact same appointment object. This proves that the original appointment remains stored and retrievable, but it does not independently verify its status.

### Activity 3 Boundary thinking

Design boundary or edge cases for blank identifiers, whitespace-only names, same-time practitioner bookings, cancelled appointments and invalid status transitions.
For each input/state, expected result and supporting contract: [response]
| Input/state | Expected result | Supporting contract |
| :--- | :--- | :--- |
| Empty patient ID (`""`) | Reject with `ValueError`. | Patient ID must not be blank. |
| Whitespace-only patient ID | Reject with `ValueError`. | Patient ID must contain valid text. |
| Whitespace-only patient name | Reject with `ValueError`. | Required names must not be blank. |
| Same practitioner and exact time with an existing scheduled appointment | Reject with `ValueError`. | FR-05 prevents practitioner conflicts. |
| Same time after cancellation | Allow the new booking. | Cancelled appointments do not block slots. |
| Cancel an already cancelled appointment | Reject with `ValueError`. | Repeated cancellation is not allowed. |
| Cancel a completed appointment | Reject with `ValueError`. | Completed appointments cannot be cancelled. |
| Date/time containing seconds or microseconds | Reject with `ValueError`. | Appointment time uses minute precision. |
| Timezone-aware date/time | Reject with `ValueError`. | Date/time must be local and timezone-naive. |
### Activity 4 Critique GitHub Copilot tests

GitHub Copilot generates five tests, all of which pass. Two only assert that objects are not None, one asserts True, and two assume SMS notifications exist. Identify what is wrong and rewrite the test intentions.

| Candidate | What is wrong | Rewritten test intention |
|---|---|---|
| 1 | Checking only that a patient object is not `None` does not prove that the correct patient was registered. | Register a valid patient and verify that the stored patient has the expected ID and name. |
| 2 | Checking only that an appointment object is not `None` does not prove that the appointment was booked correctly. | Book an appointment and verify its ID, patient, practitioner, date/time and initial `SCHEDULED` status. |
| 3 | `assert True` does not check any actual system behaviour. | Cancel a scheduled appointment and verify that its status changes to `CANCELLED`. |
| 4 | Assumes that an SMS notification feature exists, but this is not included in the stated requirements. | Test that a cancelled appointment remains stored and retrievable. |
| 5 | Assumes another SMS notification behaviour that is not supported by the requirements. | Attempt to cancel an already cancelled appointment and verify that `ValueError` is raised and the record remains unchanged. |
### Tutorial exit question

Why can 100% code coverage coexist with poor software verification?
100% code coverage can coexist with poor software verification because coverage only shows that the code was executed during testing. It does not prove that the tests check the correct behaviour. For example, a test using `assert True` may execute the code without checking the expected result. Good verification requires meaningful assertions and tests that are linked to the actual requirements.

## B Requirement to Test Traceability Matrix

Assign TEST IDs before implementation or generation. Use canonical AC IDs with their actual meaning; quote supporting revision 2 contracts when no canonical AC is assigned. Blank-ID validation is not AC-01.2. Identify supplied versus student-authored evidence.

## B. Requirement-to-Test Traceability Matrix

| Requirement | Acceptance Criterion / Contract | Test ID | Test Type | Test Name / Location | Expected Behaviour | Result |
|---|---|---|---|---|---|---|
| FR-01 Register Patient | Supporting validation contract | DOM-P01 | Domain | `test_valid_patient` – `test_domain.py` | A valid Patient object is created with the expected ID and name. | Domain evidence |
| FR-01 Register Patient | Supporting validation contract | DOM-P02 | Domain | `test_invalid_patient_id` – `test_domain.py` | Blank, whitespace-only, None and invalid patient IDs are rejected with `ValueError`. | Domain evidence |
| FR-02 Patient Lookup | AC-02.1 | SVC-P01 | Service | `test_find_patient_returns_stored_object` – `test_services.py` | Looking up a known patient ID returns the stored patient object. | Service evidence |
| FR-02 Patient Lookup | AC-02.2 | SVC-P02 | Service | `test_find_patient_unknown_id_raises_lookup_error` – `test_services.py` | Looking up an unknown patient ID raises `LookupError`. | Service evidence |
| FR-03 Practitioner Registration | Supporting domain contract | DOM-PR01 | Domain | `test_valid_practitioner` – `test_domain.py` | A valid Practitioner object is created with the expected ID, name and specialty. | Domain evidence |
| Practitioner Lookup | Supporting operation | SVC-PR01 | Service | `test_find_practitioner_returns_stored_object` – `test_services.py` | Looking up a known practitioner ID returns the stored practitioner object. | Service evidence |
| Practitioner Lookup | Supporting operation | SVC-PR02 | Service | `test_find_practitioner_unknown_id_raises_lookup_error` – `test_services.py` | Looking up an unknown practitioner ID raises `LookupError`. | Service evidence |
| FR-04 Book Appointment | AC-03.1 | DOM-A01 | Domain | `test_valid_appointment` – `test_domain.py` | A valid Appointment object is created with its initial status set to `SCHEDULED`. | Partial domain evidence |
| FR-04 Book Appointment | AC-03.1 | SVC-A01 | Service | `test_cancelled_appointment_slot_can_be_reused` – `test_services.py` | A replacement appointment can be booked at the same time after the original appointment is cancelled. The replacement is stored with `SCHEDULED` status. | Service evidence |
| FR-05 Prevent Practitioner Conflict | AC-04.1 | SVC-A02 | Service | `test_rejected_booking_conflict_preserves_existing_appointment` – `test_services.py` | A booking for the same practitioner at the same exact time is rejected, and the original appointment remains unchanged. | Service evidence |
| FR-06 Cancel Appointment | AC-05.1 | DOM-A02 | Domain | `test_appointment_cancellation` – `test_domain.py` | Cancelling a scheduled appointment changes its status to `CANCELLED`. | Domain evidence |
| FR-06 Cancel Appointment | AC-05.1 | SVC-A03 | Service | `test_cancel_retains_same_appointment` – `test_services.py` | Cancellation returns the same appointment object and changes its status to `CANCELLED`. | Service evidence |
| FR-06 Cancel Appointment | AC-05.3 | DOM-A03 | Domain | `test_appointment_cancellation` – `test_domain.py` | Repeated cancellation is rejected with `ValueError`. | Domain evidence |
| FR-06 Cancel Appointment | AC-05.3 | SVC-A04 | Service | `test_repeated_cancellation_is_rejected` – `test_services.py` | A second cancellation is rejected and the appointment state remains unchanged. | Service evidence |
| FR-07 Retain Cancelled History | AC-05.2 | SVC-A05 | Service | `test_cancel_retains_same_appointment` – `test_services.py` | The cancelled appointment remains retrievable and present in the appointment listing. | Service evidence |
| FR-08 Appointment Lookup | AC-06.1 | SVC-A06 | Service | Lookup assertions in `test_cancel_retains_same_appointment` – `test_services.py` | Looking up the known appointment ID returns the same appointment object. | Supporting service evidence |

### Test Evidence Notes

- Domain tests cover Patient, Practitioner and Appointment construction, validation, cancellation and read-only properties.
- Service tests cover patient lookup, practitioner lookup, appointment cancellation, practitioner conflict rejection and cancelled appointment history.
- Constructor-only tests provide partial domain evidence and do not independently prove service registration or storage.
- The supplied starter tests and group-authored tests should be identified separately.
- Actual execution results must be recorded after running the tests.
## C Test Design

Use descriptive test names such as test_cancel_changes_status() or test_blank_patient_id_is_rejected(). Explain what new evidence each case adds.

| Test ID | Requirement | Acceptance criterion | Positive / Negative / Boundary | Test intention | Observable result expected | Added evidence beyond supplied tests |
|---|---|---|---|---|---|---|
| DOM-P01 | FR-01 | Supporting validation contract | Positive | Check valid Patient construction. | Patient object contains the expected ID and name. | Additional domain construction evidence. |
| DOM-P02 | FR-01 | Supporting validation contract | Negative / Boundary | Check invalid patient IDs. | Invalid IDs raise `ValueError`. | Tests multiple invalid ID values. |
| DOM-P03 | FR-01 | Supporting validation contract | Negative | Check invalid patient names. | Invalid names raise `ValueError`. | Additional required-field validation. |
| DOM-PR01 | FR-03 | Supporting validation contract | Positive | Check valid Practitioner construction. | Practitioner contains the expected ID, name and specialty. | Additional domain construction evidence. |
| DOM-PR02 | FR-03 | Supporting validation contract | Negative | Check invalid practitioner IDs, names and specialties. | Invalid values raise `ValueError`. | Additional required-field validation. |
| DOM-A01 | FR-04 | AC-03.1 | Positive | Check valid Appointment construction. | Appointment is created with the correct details and `SCHEDULED` status. | Partial domain evidence only. |
| DOM-A02 | FR-06 | AC-05.1 | Positive | Check appointment cancellation. | Status changes from `SCHEDULED` to `CANCELLED`. | Domain state-transition evidence. |
| DOM-A03 | FR-06 | AC-05.3 | Negative / Boundary | Check repeated cancellation. | Repeated cancellation raises `ValueError`. | Domain cancellation guard evidence. |
| SVC-P01 | FR-02 | AC-02.1 | Positive | Check lookup of a registered patient. | The service returns the same stored patient object. | Service lookup evidence. |
| SVC-P02 | FR-02 | AC-02.2 | Negative | Check lookup of an unknown patient. | `LookupError` is raised. | Service error-handling evidence. |
| SVC-PR01 | Supporting operation | Supporting contract | Positive | Check lookup of a registered practitioner. | The service returns the same stored practitioner object. | Practitioner lookup evidence. |
| SVC-PR02 | Supporting operation | Supporting contract | Negative | Check lookup of an unknown practitioner. | `LookupError` is raised. | Practitioner lookup error evidence. |
| SVC-A01 | FR-04 | AC-03.1 | Positive | Check booking after cancellation releases the original time slot. | Replacement appointment is stored with `SCHEDULED` status. | Service booking evidence for this scenario. |
| SVC-A02 | FR-05 | AC-04.1 | Negative / Boundary | Check booking conflict for the same practitioner and exact time. | Booking raises `ValueError`; original appointment remains unchanged. | Service conflict evidence. |
| SVC-A03 | FR-06 | AC-05.1 | Positive | Check cancellation through AppointmentService. | Same appointment object is returned with `CANCELLED` status. | Service cancellation evidence. |
| SVC-A04 | FR-06 | AC-05.3 | Negative | Check repeated cancellation through the service. | Second cancellation raises `ValueError`; existing state remains unchanged. | Service cancellation guard evidence. |
| SVC-A05 | FR-07 | AC-05.2 | Positive | Check cancelled appointment history. | Cancelled appointment remains retrievable and listed in the store. | Service history-retention evidence. |

## D Arrange Act Assert Record

Arrange test data; act on one meaningful behaviour; assert the required observable outcome. Use the specific current exception with pytest.raises where needed.

| Test ID | Arrange | Act | Assert | Why meaningful / why assertion proves criterion |
|---|---|---|---|---|
| DOM-P01 | Prepare a valid patient ID and name. | Create a Patient object. | Check the patient ID and name. | Confirms that valid patient details are stored in the object correctly. |
| DOM-P02 | Prepare invalid patient IDs. | Attempt to create Patient objects. | Check that `ValueError` is raised. | Confirms that invalid required IDs are rejected. |
| DOM-PR01 | Prepare valid practitioner details. | Create a Practitioner object. | Check ID, name and specialty. | Confirms valid practitioner construction. |
| DOM-A01 | Create valid Patient and Practitioner objects and a valid date/time. | Create an Appointment object. | Check appointment details and `SCHEDULED` status. | Confirms valid appointment construction and initial state. |
| DOM-A02 | Create a scheduled appointment. | Cancel the appointment. | Check that status becomes `CANCELLED`. | Directly verifies the cancellation state transition. |
| DOM-A03 | Create an appointment and cancel it once. | Attempt cancellation again. | Check that `ValueError` is raised. | Verifies that repeated cancellation is rejected. |
| SVC-P01 | Create a fresh store and register a patient. | Search using the registered patient ID. | Check that the returned object is the registered patient. | Proves that the service returns the stored record. |
| SVC-P02 | Create a fresh store and register a patient. | Search using an unknown patient ID. | Check that `LookupError` is raised. | Verifies correct handling of an unknown patient. |
| SVC-A02 | Create a fresh store and book an appointment. | Attempt another booking for the same practitioner and exact time. | Check `ValueError` and confirm the original appointment remains unchanged. | Proves that conflicting bookings are rejected without damaging existing data. |
| SVC-A03 | Create a scheduled appointment using the service. | Cancel the appointment. | Check object identity and `CANCELLED` status. | Confirms that the same stored appointment is updated. |
| SVC-A04 | Create and cancel a scheduled appointment once. | Attempt a second cancellation. | Check `ValueError` and unchanged appointment details. | Confirms that repeated cancellation is safely rejected. |
| SVC-A05 | Create and cancel an appointment. | Retrieve the appointment and list stored appointments. | Check that the same appointment remains available. | Proves that cancelled history is retained during the session. |

## E Domain Test Evidence

Cover Patient/Practitioner construction and validation; Appointment construction, initial status, cancellation and illegal/repeated transitions. Preserve the four reference intentions described in handout Part C.
| Test ID | Behaviour | Test file/function | Result |
|---|---|---|---|
| DOM-P01 | Valid Patient construction | `test_valid_patient` | Execution result to be recorded |
| DOM-P02 | Invalid patient ID rejection | `test_invalid_patient_id` | Execution result to be recorded |
| DOM-P03 | Invalid patient name rejection | `test_invalid_patient_name` | Execution result to be recorded |
| DOM-P04 | Patient ID read-only property | `test_patient_id_read_only` | Execution result to be recorded |
| DOM-PR01 | Valid Practitioner construction | `test_valid_practitioner` | Execution result to be recorded |
| DOM-PR02 | Invalid practitioner ID rejection | `test_invalid_practitioner_id` | Execution result to be recorded |
| DOM-PR03 | Invalid practitioner name rejection | `test_invalid_practitioner_name` | Execution result to be recorded |
| DOM-PR04 | Invalid practitioner specialty rejection | `test_invalid_practitioner_specialty` | Execution result to be recorded |
| DOM-PR05 | Practitioner ID read-only property | `test_practitioner_id_read_only` | Execution result to be recorded |
| DOM-A01 | Valid Appointment construction and initial status | `test_valid_appointment` | Execution result to be recorded |
| DOM-A02 | Invalid appointment ID rejection | `test_invalid_appointment_id` | Execution result to be recorded |
| DOM-A03 | Invalid patient and practitioner references | `test_invalid_appointment_patient`, `test_invalid_appointment_practitioner` | Execution result to be recorded |
| DOM-A04 | Invalid appointment status | `test_invalid_appointment_status` | Execution result to be recorded |
| DOM-A05 | Invalid appointment date/time | `test_invalid_appointment_date_time` | Execution result to be recorded |
| DOM-A06 | Appointment cancellation and repeated cancellation | `test_appointment_cancellation` | Execution result to be recorded |
| DOM-A07 | Completed appointment cancellation guard | `test_completed_appointment_cancellation` | Execution result to be recorded |
| DOM-A08 | Appointment read-only properties | `test_appointment_read_only_properties` | Execution result to be recorded |

## F Service Test Evidence

Use fresh shared SmartCareDataStore state, registered objects and completed Stage 6 services.

| Test ID | Behaviour | Requirement / criterion | Test file/function | Result |
|---|---|---|---|---|
| SVC-PR01 | Known practitioner lookup | Supporting operation | `test_find_practitioner_returns_stored_object` | Execution result to be recorded |
| SVC-PR02 | Unknown practitioner lookup | Supporting operation | `test_find_practitioner_unknown_id_raises_lookup_error` | Execution result to be recorded |
| SVC-P01 | Known patient lookup | AC-02.1 | `test_find_patient_returns_stored_object` | Execution result to be recorded |
| SVC-P02 | Unknown patient lookup | AC-02.2 | `test_find_patient_unknown_id_raises_lookup_error` | Execution result to be recorded |
| SVC-A01 | Reuse of cancelled appointment time slot | AC-03.1 supporting booking evidence | `test_cancelled_appointment_slot_can_be_reused` | Execution result to be recorded |
| SVC-A02 | Rejected booking conflict | AC-04.1 | `test_rejected_booking_conflict_preserves_existing_appointment` | Execution result to be recorded |
| SVC-A03 | Cancellation and retention of appointment | AC-05.1 and AC-05.2 | `test_cancel_retains_same_appointment` | Execution result to be recorded |
| SVC-A04 | Repeated cancellation rejection | AC-05.3 | `test_repeated_cancellation_is_rejected` | Execution result to be recorded |
| SVC-A05 | Completed appointment cancellation rejection | Supporting cancellation contract | `test_completed_appointment_cannot_be_cancelled` | Execution result to be recorded |
| SVC-A06 | Cancellation of one appointment does not change another | Supporting state-preservation contract | `test_cancel_does_not_change_other_appointment` | Execution result to be recorded |
| SVC-A07 | Invalid or unknown appointment ID rejection | Supporting lookup validation contract | `test_cancel_rejects_invalid_or_unknown_id` | Execution result to be recorded |

## G Negative and Boundary Cases

Connect cases to actual contracts and verify unchanged state after rejection.

| Behaviour | Boundary / invalid input | Expected result | Test ID |
|---|---|---|---|
| Patient ID validation | Empty patient ID | `ValueError` | DOM-P02 |
| Patient ID validation | Whitespace-only patient ID | `ValueError` | DOM-P02 |
| Patient name validation | Whitespace-only patient name | `ValueError` | DOM-P03 |
| Practitioner ID validation | Empty or whitespace-only ID | `ValueError` | DOM-PR02 |
| Practitioner name validation | Invalid or whitespace-only name | `ValueError` | DOM-PR03 |
| Practitioner specialty validation | Invalid or whitespace-only specialty | `ValueError` | DOM-PR04 |
| Appointment ID validation | Empty or invalid appointment ID | `ValueError` | DOM-A02 |
| Appointment participant validation | Patient or practitioner is `None` | `ValueError` | DOM-A03 |
| Appointment status validation | Invalid status value | `ValueError` | DOM-A04 |
| Appointment date/time validation | Timezone-aware datetime | `ValueError` | DOM-A05 |
| Appointment date/time validation | Date/time containing seconds or microseconds | `ValueError` | DOM-A05 |
| Practitioner booking conflict | Same practitioner, exact time and existing scheduled appointment | `ValueError`; original appointment remains unchanged | SVC-A02 |
| Cancelled appointment slot | Book another appointment at the same time after cancellation | New appointment is accepted and stored | SVC-A01 |
| Repeated cancellation | Cancel an already cancelled appointment | `ValueError`; appointment remains unchanged | SVC-A04 |
| Completed appointment cancellation | Attempt to cancel a completed appointment | `ValueError`; appointment remains unchanged | SVC-A05 |

## H GitHub Copilot Test Design

**Requirement:** FR-05 – Prevent Practitioner Conflict.

**Acceptance criterion:** AC-04.1 – A booking for the same practitioner at the exact same time as an existing scheduled appointment must be rejected.

**Behaviour to test:** The system should reject a second appointment booking for the same practitioner at the exact same date and time.

**Human-first test idea/categories:**

- Positive: Book an appointment when the practitioner is available.
- Negative: Attempt to book another appointment with the same practitioner at the same time.
- Boundary: Check the exact date and time conflict.

**Prompt and purpose:**
GitHub Copilot to suggest pytest test cases for AC-04.1 using the existing SmartCareDataStore and AppointmentService. The purpose is to check whether conflicting bookings are rejected and existing appointment details remain unchanged.

**Copilot test idea/candidate:**

Attempt to book a second appointment with the same practitioner at the exact time as an existing scheduled appointment.

**What it claims to verify:** Conflicting bookings are rejected with `ValueError`.

**Requirement trace:** FR-05, AC-04.1.

**Assertion quality:** Check the exception, original appointment status and details, and confirm that the rejected appointment is not stored.

**Human critique:** The test checks the actual conflict rule using meaningful assertions rather than simply checking whether an appointment exists.

**Decision:** Accept as a test-design candidate.

**Reason:** It directly checks the stated acceptance criterion without introducing additional requirements.

**Final test reference:** `test_rejected_booking_conflict_preserves_existing_appointment` in `project/tests/test_services.py`.

**Actual verification result:** To be confirmed by running the test.
Before accepting: traces to a requirement/criterion; can fail for the right reason; assertion checks required behaviour; no invented business rule; no unnecessary private implementation dependence. Reject/modify weak assertions, invented requirements, excessive mocking, duplicates, wrong exceptions, obsolete architecture and unnecessary dependencies.

## I Weak Copilot Test Reflection
**Which Copilot-generated test looked convincing but was weak?**

A test that only checked whether the appointment object was not `None` looked convincing but was weak.

**Why was it weak?**

It only confirmed that an appointment object existed. It did not verify whether the booking followed the practitioner conflict requirement.

**How did you strengthen it?**

The test was strengthened by checking that a conflicting booking raises `ValueError`, the original appointment remains in `SCHEDULED` status, and the rejected appointment is not stored.

**Accepted / modified / rejected test decisions and evidence:**

The weak test idea was modified to include meaningful assertions. The improved test checks the actual booking conflict behaviour and verifies that existing appointment data remains unchanged.


## J Regression Run

Run python -m pytest from project/. Retain all accumulated tests. Record the tested SHA accurately.

| Command | Working directory | Code SHA | Passed | Failed | Failure summary | Product defect / test defect / unresolved | Evidence and interpretation |
|---|---|---|---:|---:|---|---|---|
| `python -m pytest` | `project/` | 2e63d47011f8bd1201e4ab9639873261e59ccc59 | 72 | 0 | No failures reported. | N/A – No failures identified. | The Stage 7 test files `test_domain.py`, `test_services.py` and `test_starter.py` contained 72 tests in total. All 72 passed, indicating that the implementation passed the available Stage 7 tests. |
Individual test runs and changed-order independence evidence: [commands, results, links]
Optional tutor-led demonstration notes: [optional; leave blank if not used]
A meaningful test should detect a relevant incorrect result. Students do not have to perform the demonstration or submit failure/restoration evidence for assessment. The tutor restores the example and reruns its tests. This is not a Stage 8 fault activity.
Requirement → test → failure/observation → diagnosis → change → verification: [concise links where applicable]

## K What the Suite Still Does Not Prove

**What does your test suite still not prove?**

The test suite does not prove that every possible scenario works correctly. Some areas still need additional testing, including duplicate patient registration, booking with unknown participants and allowing a different practitioner to have an appointment at the same time. Passing tests does not guarantee that the entire application is free from defects.

**Coverage if used:**

Code coverage was not used.

**Which uncovered areas matter, and why does coverage percentage alone not establish correctness?**

Duplicate patient registration and booking validation are important because incorrect handling could affect stored records and appointment data. Code coverage percentage alone does not prove correctness because executing a line of code does not guarantee that the expected behaviour is properly tested.

**Optional fixtures/parametrisation used and why, if any:**

Pytest parametrisation was used to test multiple invalid input values, such as blank, `None` and invalid values. This helps check validation behaviour with different inputs.
## L Git and Review Evidence
| Issue/task | Branch | PR | Reviewer     | Key feedback | Outcome |
|---|---|---|--------------|---|---|
| Practitioner lookup tests | `stage7-practitioner-tests` | PR #13 | Ujwal        | Reviewed the practitioner lookup tests and tested the changes locally using PyCharm. Service tests: 22 passed. Complete test suite: 30 passed. | Tests passed and the reviewer approved the PR. |
| Domain testing | feature/stage7-domain-tests | PR #11 | Merged by me | No separate reviewer feedback recorded. | I merged the pull request after checking the changes. |
## M Contribution Evidence

Record actual work in test design, implementation, review, traceability, diagnosis, necessary fixes and integration. Do not include confidential peer ratings.

| Member | Actual contribution | Evidence link |
|---|---|---|
| [complete] | [complete] | [complete] |
## M. Contribution Evidence

| Member       | Actual contribution | Evidence link |
|--------------|---|---|
| Chloe Ruan   | Worked on domain tests for Patient, Practitioner and Appointment. | `2e91a57ef772b8ae53b7beb36c89006c98b919e2` |
| Ujwal        | Worked on patient lookup and booking tests. | `1686718d2c8d0542e50a3b75442cbeca93722f1f` |
| me(u3330161) | Implemented practitioner lookup tests. | `0ab4944e1703d52eb4f65d7e108d344c7e96a10d` |
| Saphal       | Worked on appointment cancellation service tests. | `348ac7cfebbfb1ccb802de77d15557dd80c4045a` |

## N Formative Questions

1. What question does verification answer?
Verification checks whether the software was built correctly according to the requirements and specifications.

2. What question does validation answer?
Validation checks whether the software meets the user's needs and solves the intended problem.

3. What is a unit test?
A unit test checks a small individual part of the program, such as a function or class, to make sure it works correctly.

4. What is a pytest fixture?
A pytest fixture provides reusable test data or setup before a test runs. It helps avoid repeating the same setup code.

5. What is parametrisation in pytest?
Parametrisation allows one test function to run multiple times with different input values and expected results.

6. What is regression testing?
Regression testing checks that existing functionality still works after code changes or new features are added.

7. What does code coverage tell us, and what does it not prove?
Code coverage shows how much of the code is executed during testing. However, it does not prove that the code is correct or that all possible situations are tested.

8. What makes an assertion weak?
An assertion is weak when it only checks a basic result without verifying the actual expected behaviour. For example, checking that an object is not None may not confirm that its details are correct.

9. What is the appropriate role of GitHub Copilot as a test assistant?
GitHub Copilot can suggest test cases and help identify missing scenarios. However, developers must review its suggestions and make sure the tests match the actual requirements.

10. What is the Stage 7 engineering rule?
Write tests based on requirements, use meaningful assertions, check both valid and invalid inputs, and verify that existing functionality continues to work after changes.

## O Stage Completion

**Tested Stage 7 main SHA:**  
`2e63d47011f8bd1201e4ab9639873261e59ccc59`

**Full-suite result:**  
The Stage 7 test files were executed using the following command from the `project/` directory:

`python -m pytest tests/test_domain.py tests/test_services.py tests/test_starter.py`

The result was **72 passed and 0 failed in 0.11 seconds**.

**Unresolved defects and effect on baseline:**  
No unresolved defects were identified in the 72 passing Stage 7 tests. The tested functionality passed the available domain, service and starter tests.

**Clean working tree and integration evidence:**  
The Stage 7 documentation file has been updated. The changes are not yet committed or integrated into the main branch. Final Git status and integration evidence will be added after the documentation changes are committed and merged.

**Stage 8 handover status:**  
Stage 7 testing and verification documentation has been completed. No Stage 8 work is assigned as part of Stage 7. The project is ready for the next stage after final integration checks.

**All tutorial/formative responses and traceability/Copilot decisions complete:**  
All tutorial and formative questions have been answered. Requirement-to-test traceability and Copilot decisions have been documented. Supporting evidence and links have been included where available.