# Stage 8 activities and evidence

UG and PG | One evolving group project | Complete this blank record using the Stage 8 handout.

All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage08/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions. The Stage 8 preparation utility is supplied or run by teaching staff when Stage 8 begins. Follow your tutor’s controlled workflow and the handout. If temporarily supplied, keep it outside the repository in a sibling Stage_8_Assets/ folder; exclude it from Git and the final submission.

Group/tutorial: [complete]
Members and UG/PG cohorts: [complete]
Record owner / contribution links for each member: [complete]

Use concise results and accessible artefact links rather than copying entire logs. Keep human-first entries before consulting GitHub Copilot. Link shared evidence once; do not repeat it across sections. No entries below are specimen answers or claimed results.

## A. Tutorial activities

### A.1 Classify all five statements
For each, choose symptom, evidence or hypothesis/opinion, and explain your reason. These are discussion statements, not confirmed diagnoses.
- Appointment disappears after cancellation.
- The data-store removal path is probably being called.
- The failing test shows store.find_appointment('A1') returns None.
- The service layer is badly designed.
- Traceback points to smartcare/services.py line 42 in the example.
The example line number is illustrative; inspect the actual line in your run. The removal hypothesis must be tested against the current project, which has no public delete operation.

Response and reason: [complete]

### A.2 Build a debugging record
Choose the cancelled-history scenario or a same-practitioner/time booking. Before changing code, record expected behaviour, observed behaviour, minimal reproduction, a hypothesis and evidence to inspect. Use a requirement to justify the expectation. Keep the initial hypothesis even if later evidence disproves it.

Response and reason: [complete]

### A.3 Test defect or product defect
A test expects cancelled appointments to be deleted, but FR-07 says history must be retained. What should be changed? Explain why. Also decide whether a test expecting different practitioners at the same time to conflict reflects AC-04.2. Do not assume every failing test is correct.

Response and reason: [complete]

### A.4 Refactoring smell hunt
Consider a hypothetical 70-line AppointmentService method containing duplicate status strings, direct collection manipulation, printing, validation and four nested conditionals. Identify the smells and propose small refactorings that preserve required behaviour. The direct collection work replaces the old storage-specific scenario; use the existing SmartCareDataStore boundary. Do not implement an extra architecture.
Classify these proposed changes as refactoring, repair or feature: rename appt to appointment; extract a repeated conflict helper; add rescheduling; restore retained cancellation lookup; replace a magic status string with the existing enum. Explain the behaviour that must remain unchanged.

Response and reason: [complete]

### A.5 Traceback and hypothesis ranking
Using one actual failure, identify its exception/assertion, expected and observed values, test line, application call path and supporting requirement. List three plausible causes and rank them by fit with the available evidence. For each cause, name a check that could distinguish it from the others. Explain why a traceback alone does not establish the cause.

Response and reason: [complete]

### A.6 Exit question
Why is changing code immediately after seeing a failure often a poor debugging strategy?

Response and reason: [complete]


Classification responses (1–5, each with reason): [complete]
Tutorial debugging record — expected; observed; reproduction; hypothesis; evidence to inspect: [complete]
Traceback — exception/assertion; expected/observed values; test line; call path; requirement; ranked causes and discriminating checks: [complete]

## B. Stage 7 baseline and safe preparation

- Stage 7 code SHA and requirement baseline: [complete]
- Baseline test command / working directory / observed result / evidence: [complete]
- Clean preparation SHA if a record-only commit followed Stage 7: [complete]
- Branch and preparer / how teammates obtained this branch: [complete]
- Downloaded tool version, source SHA256 and --check outcome: [complete]
- --apply and --verify output summaries / artefact references: [complete]
- Bounded diff inspected and recovery location (not committed): [complete]
- Prepared faulty-state commit SHA: [complete]
- Preparation or recovery issues and resolution, if any: [complete]
- Initial prepared full-suite command / result / key failures: [complete]

## C. F8-01 diagnosis and repair

- Symptom / observed behaviour:

The system did not reject a conflicting appointment booking. Two existing tests failed with DID NOT RAISE ValueError.
- Expected behaviour and requirement: 

The system should reject a new booking if the same practitioner already has an appointment at the same time. It should only allow different practitioners to have appointments at the same time. (Requirement: AC-04.1, AC-04.2)

- Minimal synthetic reproduction steps: 
1. Register two patients and one practitioner.
2. Book A1 for Patient 1 with the practitioner at a specific time.
3. Try to book A2 for Patient 2 with the same practitioner at the same time.
4. Check whether A2 is rejected. 
- Meaningful failing test path/name and exact relevant failure: 

File: test_starter.py 

test_conflict_rule_and_different_practitioner: Failed (DID NOT RAISE ValueError.)

File: tests/test_services.py

test_rejected_booking_conflict_preserves_existing_appointment: Failed (DID NOT RAISE ValueError.)

- Human hypothesis and intended checks: see E, F8-01.
- Supported root cause and inspected code/runtime evidence:

The practitioner ID comparison in has_practitioner_conflict() is wrong. It uses != instead of ==. This causes the system to miss conflicts for the same practitioner and reject bookings for different practitioners.

- Smallest justified fix / diff / why other behaviour is preserved: 

Change != to == in has_practitioner_conflict(). It only changes the practitioner ID comparison logic. No other code is changed.

- Repair SHA / focused verification result: 

679d99f8681882fc0fa69c2bc11f41c89bd04c10 / 2 passed, 1 deselected in 0.01s.

## D. F8-02 diagnosis and repair

- Symptom / observed behaviour: 

The system could not find an appointment after it was cancelled. Three existing tests failed with LookupError: Appointment not found.

- Expected behaviour and requirement: 

The system should keep the appointment after it is cancelled. The status should change to CANCELLED. Also, we should still be able to find it using its ID. (Requirement: FR-07)

- Minimal synthetic reproduction steps: 
1. Register one patient and one practitioner.
2. Create an appointment A1 for the patient and practitioner.
3. Cancel appointment A1.
4. Try to find A1 using its ID.
5. Check if A1 can still be found and its status is CANCELLED.

- Meaningful failing test path/name and exact relevant failure: 

File: tests/test_services.py

test_repeated_cancellation_is_rejected (LookupError: Appointment not found.)

test_cancel_retains_same_appointment (LookupError: Appointment not found.)

test_cancelled_appointment_slot_can_be_reused (LookupError: Appointment not found.)

- Human hypothesis and intended checks: see E, F8-02.
- Supported root cause and inspected code/runtime evidence: 

The find_appointment() function does not return cancelled appointments. It checks appointment.status.value != "cancelled". Therefore, the record is still stored, but the function does not return the cancelled appointment.

- Smallest justified fix / diff / why other behaviour is preserved: 

Remove the appointment.status.value != "cancelled" condition from find_appointment(). Appointments can be found using their IDs, regardless of their status. No other code is changed.

- Repair SHA / focused verification result: 

3732390fe607a309acb7426d24dbb62605ed9f7d /  1 passed in 0.01s

## E. Human-first hypotheses

Complete both entries BEFORE Copilot. C/D supply observed/expected/reproduction/test; retain those initial facts and link them here.

### F8-01 human entry
Likely cause and why plausible: 

The system could not actually detect the conflict, so it did not raise a ValueError.

Evidence to inspect: 

Check the code related to detecting duplicate bookings in the appointment booking service.
Competing explanation: 

There may be an error in the code for creating appointments without checking for existing appointments.

Discriminating check: 

Check whether the system performs a duplicate booking check when creating an appointment. If it does, check whether the logic is correct.

Member and saved sequence/time or commit showing this preceded consultation: 

Hong Ruan — Commit 6b88467ccba08e66319d783b7440615859862223

### F8-02 human entry
Likely cause and why plausible: 

The system may not keep the cancelled appointment in the data store.

Evidence to inspect:

Check the code related to the appointment record after cancellation.

Competing explanation:

The appointment may still be stored, but the find appointment function does not return it.

Discriminating check:

1. Check if the appointment status changes to CANCELLED. 
2. Check if the record is still stored. If it is, check if the find appointment function returns it.

Member and saved sequence/time or commit showing this preceded consultation: 

Hong Ruan — Commit 64ef1947090b0c5ab88a21053bb166b4b2f8f803

## F. GitHub Copilot prompts, findings and human decisions

Use the full handout prompt separately for BOTH defects, after E. Keep each actual prompt or accessible reference; include observed behaviour, expected behaviour, reproduction, failing test, human hypothesis, relevant code, three ranked causes and discriminating checks, with the no-rewrite/no-invented-requirements constraints.

### F8-01 Copilot review
Actual prompt / output reference and member: 

Hong Ruan — GitHub Copilot Chat. https://github.com/copilot/share/82374202-0804-80e4-9950-fe0e40eb29a8

1. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: 

suggestion: Incorrect practitioner ID comparison

Evidence check: Check has_practitioner_conflict() in data_store.py.

Observed evidence: The code uses != to compare practitioner IDs.

Evaluation: Correct.

Decision: Accept. This explains the two failing regression tests.

2. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason:

Suggestion: Tests bypass the booking service

Evidence check: Check how the regression tests create appointments.

Observed evidence: Both tests use appointment_service.book_appointment().

Evaluation: Wrong

Decision: Reject. The tests do not bypass the booking service.

3. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: 

Suggestion:Different code version or incorrect booking data

Evidence check: Check the code version and test data.

Observed evidence: The test data is correct, and the code version is the same.

Evaluation: Wrong.

Decision: Reject. The code version and test data are both correct.

Final human conclusion and comparison with initial hypothesis: 

My initial hypothesis was that the system could not detect appointment conflicts correctly. Based on Copilot's suggestions, I checked the code and found that has_practitioner_conflict() uses != instead of ==. This explains why the two regression tests failed.

### F8-02 Copilot review
Actual prompt / output reference and member: 

Hong Ruan — GitHub Copilot Chat. https://github.com/copilot/share/c8565392-4024-80e0-a851-6c4f40a149ba

1. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: 

Suggestion: Cancelled appointments are filtered out

Evidence check: Check find_appointment() in data_store.py.

Observed evidence: The code uses != "cancelled" to filter appointment records.

Evaluation: Correct.

Decision: Accept. This explains why cancelled appointments cannot be found.

2. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: 

Suggestion: The service raises LookupError

Evidence check: Check find_appointment() and cancel_appointment() in services.py.

Observed evidence: The service raises LookupError when the data store returns None.

Evaluation: Correct.

Decision: Accept. It is not the direct cause, but it is related to the problem.

3. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: 

Suggestion: Appointment removed or different data store

Evidence check: Check the appointment record after cancellation and the test setup.

Observed evidence: The appointment status changes to CANCELLED. The record is still stored, and the test uses the same data store.

Evaluation: Wrong.

Decision: Reject. The appointment is not removed, and the same data store is used.

Final human conclusion and comparison with initial hypothesis: 

My initial hypothesis was that the system might not keep the cancelled appointment record. Based on Copilot's suggestions, I checked the code and found that find_appointment() does not return cancelled appointments. The record is still stored, but the function returns None.



## G. Failing to passing regression evidence

| Checkpoint | Code SHA or precise diff                 | Command and working directory                                                                 | Actual result and artefact reference                                                                             |
|---|------------------------------------------|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| F8-01 before repair | 6b88467ccba08e66319d783b7440615859862223 | python3 -m pytest tests/test_regressions.py -vv -s  (project/)                                          | result: 2 failed in 0.03s artefact reference: https://github.com/Saphal-uc/Assignment-3/issues/18                |
| F8-01 after repair | 679d99f8681882fc0fa69c2bc11f41c89bd04c10                                       | python3 -m pytest tests/test_regressions.py -k f8_01 -vv -s   (project/)                                                                                         | result: 2 passed, 1 deselected in 0.01s. artefact reference: https://github.com/Saphal-uc/Assignment-3/issues/18 |
| F8-02 before repair | 64ef1947090b0c5ab88a21053bb166b4b2f8f803 | python3 -m pytest tests/test_regressions.py::test_f8_02_cancelled_appointment_retained -vv -s (project/)| result: 1 failed in 0.03s artefact reference: https://github.com/Saphal-uc/Assignment-3/issues/19                |
| F8-02 after repair | 3732390fe607a309acb7426d24dbb62605ed9f7d                              | python3 -m pytest tests/test_regressions.py::test_f8_02_cancelled_appointment_retained -vv -s  (project/)                                                                                 | result: 1 passed in 0.01s.  artefact reference: https://github.com/Saphal-uc/Assignment-3/issues/19                                                                    |
| Full suite after both repairs, before refactor | 3732390fe607a309acb7426d24dbb62605ed9f7d                              | python3 -m pytest -vv -s (project/)                                                                                   | result: 75 passed in 0.03s.  artefact reference: https://github.com/Saphal-uc/Assignment-3/issues/19                                                                                                       |

Explain how the assertions detect each relevant incorrect result and protect previous behaviour: 

F8-01: I wrote two new regression tests. One checks the booking conflict for the same practitioner at the same time. The other checks if different practitioners can have appointments at the same time.

F8-02: I wrote one new regression test. It checks if the appointment status changes to CANCELLED. Also, it checks if the record is still stored and can be found using its ID.

Existing tests: I also ran all the existing tests to make sure my fixes did not break other functions. After fixing both bugs, all 75 tests passed.

Unrelated failures investigated / resolution: 

Not applicable. There were no unrelated failures. All the failed tests were related to F8-01 and F8-02. After fixing both bugs, all 75 tests passed.

## H. Refactoring decision and before/after verification

Smell and exact location: [complete]
Small proposed structural change / why justified: [complete before editing]
External behaviour to preserve / relevant tests: [complete]
Before result: see G, full passing suite.
Actual change / diff / separate refactor SHA: [complete]
Focused and full after-refactor commands / working directory / results / evidence: [complete]
Result — accepted, revised or rejected / reason / behaviour-preservation conclusion: [complete]

## I. Git, human review and integration

Issues for both defects / refactor scope and owners: [complete]
Branch / prepared, repair and refactor checkpoints: [link B/C/D/H]
PR link and another member's reviewer identity: [complete]
Key human feedback, difference from Copilot findings and response/outcome: [complete]
Actual review approval / merge evidence: [complete]
Integrated code SHA and team pull/retest command / working directory / result: [complete]
Evidence-only later SHA / explanation if different: [complete or not applicable]
Each member's substantive contribution and artefact: [complete]

## J. Required reflections

1. Which Copilot diagnosis appeared convincing but lacked evidence? [complete; report honestly if none and discuss the least-supported real suggestion]
2. What evidence changed your group's view? [complete]
3. How did regression tests protect the refactoring? [complete]

## K. Ten formative questions

1. What should an engineer do before changing code in response to a failure?

Response: [complete]

2. Where should expected behaviour come from during debugging?

Response: [complete]

3. What is a debugging hypothesis?

Response: [complete]

4. What is a regression test and why is it retained?

Response: [complete]

5. What is meant by root cause?

Response: [complete]

6. What is refactoring?

Response: [complete]

7. What is a swallowed exception?

Response: [complete]

8. What is a code smell?

Response: [complete]

9. How should GitHub Copilot-generated debugging diagnoses be treated?

Response: [complete]

10. What is the Stage 8 engineering rule?

Response: [complete]

## L. Completion and handover

- [ ] Existing project, earlier tests and stage records preserved.
- [ ] Passing Stage 7 SHA and safe preparation details recorded.
- [ ] Both defects reproduced with meaningful failing tests.
- [ ] Both human hypotheses recorded before Copilot; actual suggestions evaluated with evidence.
- [ ] Supported causes and minimal repairs explained; focused and full regression results recorded.
- [ ] One genuine refactor verified under passing before/after tests.
- [ ] Human PR review, feedback resolution and integrated retest recorded.
- [ ] Tutorial, three reflections and ten formative responses complete.
- [ ] Local recovery metadata excluded from submitted source.
- [ ] Same project and full suite ready for Stage 9 after Stage 8 integration, verification and recording.

Verified integrated code SHA / result: see I.
Submitted SHA and evidence-only difference if any: [complete]
Unresolved issues or incomplete checks / owner / next action: [complete]
Handover note: [complete]
