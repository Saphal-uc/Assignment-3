# Stage 8 activities and evidence

UG and PG | One evolving group project | Complete this blank record using the Stage 8 handout.

All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage08/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions. The Stage 8 preparation utility is supplied or run by teaching staff when Stage 8 begins. Follow your tutor’s controlled workflow and the handout. If temporarily supplied, keep it outside the repository in a sibling Stage_8_Assets/ folder; exclude it from Git and the final submission.

Group/tutorial: Thu 2:30 PM, Group 4

Members and UG/PG cohorts: 

Ujwal B K - UG

Srilakshmi Ravipati - UG

Hong Ruan - PG

Saphal Bhattarai - PG

Record owner / contribution links for each member: 

- Hong Ruan

Contribution: F8-01 and F8-02 debugging, regression tests, bug fixes, and related documentation.

Evidence: Issue #18, Issue #19, Commit a35280b

- Srilakshmi Ravipati

Contribution: Stage 8 code refactoring.

Evidence: PR #20

- Ujwal

Contribution: Stage 8 activities and evidence documentation.

Evidence: PR #21

 

Use concise results and accessible artefact links rather than copying entire logs. Keep human-first entries before consulting GitHub Copilot. Link shared evidence once; do not repeat it across sections. No entries below are specimen answers or claimed results.

## A. Tutorial activities

### A.1 Classify all five statements
For each, choose symptom, evidence or hypothesis/opinion, and explain your reason. These are discussion statements, not confirmed diagnoses.
- Appointment disappears after cancellation.
Classification- Symptom
Reason- Describes the observed behaviour without explaining its cause.
- The data-store removal path is probably being called.
Classification - Hypothesis
Reason - Suggests a possible explanation that needs investigation.
- The failing test shows store.find_appointment('A1') returns None.
Classification - Evidence
Reason - Provides an observable result from a test.
- The service layer is badly designed.
Classification - Opinion
Reason - Makes a judgement without providing supporting evidence.
- Traceback points to smartcare/services.py line 42 in the example.
Classification - Evidence
Reason - Identifies where an error occurred, although it does not necessarily establish the root cause.

The example line number is illustrative; inspect the actual line in your run. The removal hypothesis must be tested against the current project, which has no public delete operation.

### A.2 Build a debugging record
Choose the cancelled-history scenario or a same-practitioner/time booking. Before changing code, record expected behaviour, observed behaviour, minimal reproduction, a hypothesis and evidence to inspect. Use a requirement to justify the expectation. Keep the initial hypothesis even if later evidence disproves it.

Use F8-02(cancelled appointment history)
- Expected behaviour: Cancelled appointments should remain stored and retrievable, with their status changed to CANCELLED. Requirement: FR-07
- Observed behaviour: The system raised LookupError when trying to find a cancelled appointment.
- Minimal Reproduction steps: 
- 1 Register a patient and a practitioner.
- 2 Create an appointment with the appointment ID A1.
- 3 Cancel appointment A1.
- 4 Search for appointment A1 using its ID.
- 5 Observe whether the appointment can still be retrieved.

- Initial Hypothesis: The appointment might still exist in the data store, but the lookup function may be filtering out cancelled appointments.

- Evidence to inspect: 
- 1 Appointment status after cancellation.
- 2 Whether the appointment remains in the data store.
- 3 Implementation of find_appointment().
- 4 Relevant failing regression tests.

### A.3 Test defect or product defect
A test expects cancelled appointments to be deleted, but FR-07 says history must be retained. What should be changed? Explain why. Also decide whether a test expecting different practitioners at the same time to conflict reflects AC-04.2. Do not assume every failing test is correct.

Response and reason:

The test should be changed because expecting cancelled appointments to be deleted contradicts requirement FR-07. According to FR-07, cancelled appointments must remain stored in the system so that appointment history can be retained and accessed when required. The appointment status should change to CANCELLED, but the appointment record should not be removed. Therefore, the test expectation is incorrect, not the application behaviour. The test should be updated to verify that the cancelled appointment remains retrievable with its status set to CANCELLED.

For AC-04.2, appointments belonging to different practitioners at the same time should be allowed. A booking conflict should only occur when the same practitioner has another appointment scheduled at the same time. Therefore, a test expecting different practitioners with appointments at the same time to conflict does not correctly reflect AC-04.2 and should be corrected.

Overall, tests must follow the approved requirements rather than forcing the application to behave according to incorrect test expectations.

### A.4 Refactoring smell hunt
Consider a hypothetical 70-line AppointmentService method containing duplicate status strings, direct collection manipulation, printing, validation and four nested conditionals. Identify the smells and propose small refactorings that preserve required behaviour. The direct collection work replaces the old storage-specific scenario; use the existing SmartCareDataStore boundary. Do not implement an extra architecture.
Classify these proposed changes as refactoring, repair or feature: rename appt to appointment; extract a repeated conflict helper; add rescheduling; restore retained cancellation lookup; replace a magic status string with the existing enum. Explain the behaviour that must remain unchanged.

Response and reason:

The 70-line AppointmentService method contains several code smells that make the code difficult to understand, maintain and test.

The main code smells and proposed improvements are:

1. Duplicate status strings: Using the same status strings repeatedly can lead to inconsistencies and errors. This can be improved by using the existing AppointmentStatus enum.
2. Direct collection manipulation: Directly accessing and modifying appointment collections creates unnecessary dependencies between the service and data storage. The existing SmartCareDataStore should be used to manage appointment records through its add, find and list operations.
3. Long method: A 70-line method performs too many responsibilities. It can be improved by extracting smaller helper methods for specific tasks, such as appointment validation and conflict checking.
4. Printing inside the service: Printing messages directly from the service mixes business logic with output handling. The service should return appropriate results or raise exceptions, allowing the user interface to handle messages.
5. Nested conditionals: Four levels of nested conditions make the code difficult to follow. These can be simplified using early validation checks and smaller helper methods.

Classification of proposed changes:

Rename appt to appointment-
- Classification-Refactoring	
- Reason-Improves readability without changing the program’s behaviour.
	
Extract a repeated conflict helper.	
- Classification-Refactoring	
- Reason- Removes duplicated logic while preserving the existing conflict rules.

Add rescheduling.	
- Classification-Feature	
- Reason-Introduces new functionality that was not previously available.

Restore retained cancellation lookup.
- Classification-Repair	
- Reason-Fixes incorrect behaviour so cancelled appointments remain retrievable as required by FR-07.

Replace a magic status string with the existing enum.	
- Classification-Refactoring	
- Reason-Improves code consistency and maintainability without changing behaviour.

Behaviour that must remain unchanged:

During refactoring, the system must continue to validate appointments correctly, prevent bookings with the same practitioner at the same time, allow different practitioners to have appointments at the same time, and retain cancelled appointments with their CANCELLED status. Existing return values, exceptions, appointment IDs and object identity must also remain unchanged.

Refactoring should improve the internal structure and readability of the code without introducing new features or changing the existing system requirements. All existing regression tests should continue to pass after the refactoring.

### A.5 Traceback and hypothesis ranking
Using one actual failure, identify its exception/assertion, expected and observed values, test line, application call path and supporting requirement. List three plausible causes and rank them by fit with the available evidence. For each cause, name a check that could distinguish it from the others. Explain why a traceback alone does not establish the cause.

Response and reason:

The F8-02 failure occurred when the system attempted to find an appointment after it had been cancelled.

1. Failure evidence

* Exception: LookupError: Appointment not found.
* Expected behaviour: After cancellation, the appointment should remain stored, have the status CANCELLED, and still be retrievable using its appointment ID.
* Observed behaviour: The system raised a LookupError when attempting to find the cancelled appointment.
* Test evidence: The regression test test_f8_02_cancelled_appointment_retained failed before the repair.
* Requirement: FR-07 requires cancelled appointment history to be retained.

2. Application call path

The test created an appointment, cancelled it and then attempted to retrieve it using its ID. The service called the data-store lookup operation. When the lookup returned None, the service raised a LookupError.

The traceback identified the failure in the appointment lookup process. However, the exception alone did not establish why the appointment could not be found. Further investigation of the data store and lookup logic was necessary.

3. Ranked debugging hypotheses

Rank	Possible cause	Evidence or investigation required
1	The find_appointment() method filters out appointments with CANCELLED status.	Inspect the lookup implementation and check whether cancelled appointments are excluded.
2	The cancellation process removes the appointment from the data store.	Inspect the data store after cancellation and check whether the original appointment record still exists.
3	The service is searching the wrong data store or using an incorrect appointment ID.	Check whether cancellation and lookup use the same data-store instance and verify that the appointment ID is unchanged.

4. Root cause and verification

Investigation confirmed that the appointment had not been removed from the data store. Instead, the find_appointment() method contained a condition that excluded cancelled appointments:

appointment.status.value != "cancelled"

This meant the appointment remained stored but was not returned by the lookup method.

The repair removed the filtering condition so appointments with all statuses could be retrieved. This restored the required FR-07 behaviour.

5. Test results

* Before repair: The F8-02 regression test failed with LookupError: Appointment not found.
* After repair: The focused F8-02 regression test passed: 1 passed.
* Full regression suite after both F8-01 and F8-02 repairs: 75 passed.

Conclusion:

The traceback helped identify where the failure occurred, but it did not independently prove the root cause. Inspecting the lookup implementation and checking the stored appointment provided the evidence needed to identify and fix the problem.

Test assertion and line reference:

The relevant regression test is test_f8_02_cancelled_appointment_retained. It checks that an appointment remains retrievable after cancellation and that its status is CANCELLED.

The exact source line number was not recorded in the available test output, so no line number is claimed.

Expected result: The lookup should return the original appointment object with status CANCELLED.

Observed result: The lookup returned None, causing the service to raise LookupError: Appointment not found.

### A.6 Exit question
Why is changing code immediately after seeing a failure often a poor debugging strategy?

Response and reason:

Changing code immediately after seeing a failure is often a poor debugging strategy because the failure does not always reveal the actual root cause. Making changes without investigating can introduce new bugs, affect other parts of the system or create unnecessary code changes.

A developer should first reproduce the failure, examine the error message or traceback, compare the expected and observed behaviour, and develop possible explanations. These hypotheses should then be tested using evidence before deciding on a repair.

For example, in our F8-02 debugging task, the system raised a LookupError when retrieving a cancelled appointment. Initially, it was possible to assume that the cancellation process had deleted the appointment. However, investigation showed that the appointment was still stored, but the find_appointment() method filtered out cancelled appointments.

This demonstrated why evidence-based debugging is important. Identifying the actual root cause allowed the team to make a small, targeted repair and verify it using regression tests.

Therefore, developers should investigate first, identify the root cause, make the smallest appropriate change and run tests to confirm that the repair works without breaking existing functionality.


Classification responses (1–5, each with reason): [complete]
Tutorial debugging record — expected; observed; reproduction; hypothesis; evidence to inspect: [complete]
Traceback — exception/assertion; expected/observed values; test line; call path; requirement; ranked causes and discriminating checks: [complete]

## B. Stage 7 baseline and safe preparation

- Stage 7 code SHA and requirement baseline: 
Stage 7 code SHA and requirement baseline:

The integrated Stage 7 code baseline is commit 9f8c5696d1bb984fed1a68474cf0c0aecd917280.

Commit message: Merge pull request #17 – Strengthen appointment cancellation service tests.

The requirements baseline used for Stage 8 is SmartCare A3 Requirements Baseline 2026, revision 2.

- Baseline test command / working directory / observed result / evidence: 
Baseline test command / working directory / observed result / evidence:

The integrated Stage 7 baseline was tested using the following command:

python3 -m pytest -vv -s

Working directory: /tmp/smartcare-stage7-baseline/project

Test environment: Python 3.14.3 and pytest 9.1.1.

Observed result: 72 passed in 0.08 seconds.

The test was executed in a separate Git worktree at the Stage 7 integration commit 9f8c5696d1bb984fed1a68474cf0c0aecd917280, without modifying the active Stage 8 branch.
- Clean preparation SHA if a record-only commit followed Stage 7: 
Clean preparation SHA if a record-only commit followed Stage 7:

Not applicable. No separate record-only commit was identified between the Stage 7 baseline and the Stage 8 preparation commit.

The Stage 8 preparation commit was 7b60b556036f6ebfd407c4fa1d4e957baa987a84, whose parent was the Stage 7 integration commit 9f8c5696d1bb984fed1a68474cf0c0aecd917280. The preparation commit modified project/smartcare/data_store.py (11 insertions and 18 deletions).
- Branch and preparer / how teammates obtained this branch: 
Branch and preparer / how teammates obtained this branch:

Hong Ruan prepared the Stage 8 debugging work on the shared branch debug/stage08.

Preparation commit: 7b60b556036f6ebfd407c4fa1d4e957baa987a84.

Other group members obtained the shared branch by fetching the remote repository. I used git fetch --all and accessed the existing local debug/stage08 branch, which tracks origin/debug/stage08.
- Downloaded tool version, source SHA256 and –check outcome:

The original preparation utility and its source checksum could not be independently verified. Several copies of prepare_debugging.py were found in the Downloads folder, but they were not confirmed to be the utility used by teaching staff. Therefore, no version, SHA256 checksum or –check result is claimed.
- --apply and --verify output summaries / artefact references: 
The original –apply and –verify command outputs were unavailable for independent verification. The prepared Stage 8 branch was instead inspected through Git history and its code changes. The faulty-state checkpoint was tested in a separate temporary worktree, producing 67 passed and 5 failed tests. No unverified utility output is claimed.

- Bounded diff inspected and recovery location (not committed): 
Inspected the preparation commit 7b60b556036f6ebfd407c4fa1d4e957baa987a84 against the Stage 7 baseline. The change was limited to project/smartcare/data_store.py, specifically the find_appointment() method. The prepared implementation validates the appointment ID and excludes appointments with a cancelled status from lookup results. This introduced the intended F8-02 behaviour while leaving the Stage 7 baseline commit unchanged. The Git commit provides a recoverable checkpoint.Recovery checkpoints were retained through Git commits. The Stage 7 baseline is 9f8c569, and the prepared Stage 8 checkpoint is 7b60b55. Separate temporary worktrees were used for testing outside the original repository. The existing documentation changes in the main working tree were preserved.
- Prepared faulty-state commit SHA: 7b60b556036f6ebfd407c4fa1d4e957baa987a84
- Preparation or recovery issues and resolution, if any: 
A preparation utility was not available in the repository or its expected project location. Several copies of prepare_debugging.py were found in the Downloads folder, but they were not confirmed to be the original utility used to prepare the Stage 8 branch. Therefore, they were not used as evidence of the original preparation process.

The prepared Stage 8 branch was available remotely. It was fetched and accessed through the local debug/stage08 branch. The preparation checkpoint was verified through Git history, and a separate temporary worktree was successfully created at commit 7b60b556036f6ebfd407c4fa1d4e957baa987a84 to run the initial tests. The existing documentation changes in the main working tree were preserved.
- Initial prepared full-suite command / result / key failures: 
The initial full test suite was executed at the prepared faulty-state commit 7b60b556036f6ebfd407c4fa1d4e957baa987a84 using python3 -m pytest -vv -s. The result was 67 passed and 5 failed (72 tests total) in 0.11 seconds.

Three failures related to F8-02 returned LookupError: Appointment not found when attempting to retrieve cancelled appointments. Two failures related to F8-01 showed that conflicting bookings were not rejected because the expected ValueError was not raised. These failures provided the initial evidence for investigating the two seeded defects.

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

H. Refactoring decision and before/after verification

Smell and exact location:

The find_appointment() method in SmartCareDataStore contained an unnecessary loop through stored appointments. This made the lookup process more complicated than necessary.

Small proposed structural change / why justified:

The method was simplified by replacing the loop with direct dictionary lookup using self._appointments.get(). This makes the code shorter and easier to understand while retaining the existing appointment ID validation.

External behaviour to preserve / relevant tests:
The refactoring must preserve the following external behaviour:

* Existing valid appointment IDs must return the correct stored appointment object.
* Valid appointment IDs that do not exist must return None.
* Blank or invalid appointment IDs must continue to raise ValueError.
* Cancelled appointments must remain retrievable with their CANCELLED status, as required by FR-07.
* Existing appointment IDs, object identity, booking conflict rules and cancellation behaviour must remain unchanged.

The refactoring must improve the internal implementation without changing the expected results of existing operations.
Before result:

Before refactoring, the full test suite passed: 75 passed. See Section G.

Actual change / diff / separate refactor SHA:
Refactoring commit: 2e63d47.

Integrated merge commit: ef57eb8.

The refactoring replaced the unnecessary iteration in find_appointment() with direct dictionary lookup using self._appointments.get(). Appointment ID validation and existing lookup behaviour were preserved.

The refactoring was submitted through Pull Request #20, Stage 8 – Refactor appointment lookup. The change removed the unnecessary loop and replaced it with direct dictionary lookup.

Source branch: stage8-refactoring.

Target branch: main.

Contributor: u3330161.

Record the final refactoring commit SHA after checking the PR’s Commits tab.

Focused and full after-refactor commands / results:

The PR reports that the following command was run from the project/ directory:

python -m pytest -q

Result: 75 passed.

Result — accepted, revised or rejected:

Accepted and merged through Pull Request #20, Stage 8 – Refactor appointment lookup.

The refactoring simplified the find_appointment() method by replacing the unnecessary loop with direct dictionary lookup using self._appointments.get().

The PR reported that all 75 tests passed after the refactoring. This provides evidence that the existing test suite continued to pass.

After PR #20 was merged into main, the latest integrated project was tested in the original local repository.

* Branch: main
* Integrated commit: ef57eb8
* Command: python3 -m pytest -vv -s
* Result: 75 passed in 0.04 seconds

This confirms that the integrated Stage 8 repairs and appointment lookup refactoring passed the complete regression test suite.

## I. Git, human review and integration

I. Git, human review and integration

Issues for both defects / refactor scope and owners:

* Issue #18 – F8-01: Appointment booking conflict detection. The issue covered correcting the practitioner ID comparison so that bookings for the same practitioner at the same time are rejected. Hong Ruan investigated and completed the repair.
* Issue #19 – F8-02: Cancelled appointment history. The issue covered ensuring cancelled appointments remain stored and retrievable with CANCELLED status. Hong Ruan investigated and completed the repair.
* PR #20 – Stage 8 refactoring: Refactoring the find_appointment() method in SmartCareDataStore. The assigned group member completed the lookup refactoring.

Branch / prepared, repair and refactor checkpoints:

* Prepared Stage 8 branch: debug/stage08.
* Preparation checkpoint: 7b60b556036f6ebfd407c4fa1d4e957baa987a84.
* F8-01 repair checkpoint: 679d99f8681882fc0fa69c2bc11f41c89bd04c10.
* F8-02 repair checkpoint: 3732390fe607a309acb7426d24dbb62605ed9f7d.
* Refactoring branch: stage8-refactoring.
* Refactoring and integration checkpoint: ef57eb8.

PR link and another member’s reviewer identity:

Stage 8 refactoring was submitted through PR #20, titled Stage 8: Refactor appointment lookup. The PR merged the stage8-refactoring branch into main.

PR link: https://github.com/Saphal-uc/Assignment-3/pull/20

The PR screenshot identifies the contributor as u3330161. PR #20 was merged into the main branch. However, the GitHub pull request page displays “No reviews”, so no formal GitHub review or approval is recorded. The PR was integrated, but formal review evidence is unavailable.

Key human feedback, difference from Copilot findings and response/outcome:PR #20 was successfully merged into the main branch. However, the GitHub pull request page displayed “No reviews”, so no formal GitHub reviewer approval or review comments were recorded.

The refactoring was integrated through the pull request, and its behaviour was verified using the complete regression test suite. No unrecorded reviewer feedback or approval is claimed.

The refactoring focused on simplifying the existing find_appointment() method. The proposed change removed the unnecessary loop through stored appointments and replaced it with direct dictionary lookup using self._appointments.get().

The change retained the existing appointment ID validation and the behaviour for both found and missing appointments. Unlike the earlier Copilot debugging work, this task focused on improving the internal structure of the lookup method rather than diagnosing either seeded defect.

The proposed refactoring was incorporated into PR #20 and merged into main.

Actual review approval / merge evidence:

PR #20 was merged into main. The merge is confirmed by the terminal Git history, which shows:

ef57eb8 Merge pull request #20 from Saphal-uc/stage8-refactoring

Integrated code SHA and team pull/retest command / working directory / result:

Integrated commit: ef57eb8.

The updated main branch was retrieved using:

git pull --ff-only origin main

The full test suite was executed using:

python3 -m pytest -vv -s

Working directory: /Users/ujwalkhati/Desktop/st1-assignment-3/project

Observed result: 75 passed in 0.04 seconds.

The test was performed after switching to the integrated main branch in the original local repository.

This confirms that the full test suite passed against the integrated refactoring code.

Evidence-only later SHA / explanation if different:

Not applicable based on the current evidence. The integrated code checkpoint recorded above is ef57eb8.

Each member’s substantive contribution and artefact:

* Hong Ruan: Prepared the Stage 8 debugging work, recorded the human-first hypotheses, investigated F8-01 and F8-02, completed the repairs and contributed the debugging evidence. Relevant checkpoints include the preparation commit, F8-01 and F8-02 repair commits, and issues #18 and #19.
* Sri: Completed the find_appointment() refactoring by replacing the unnecessary iteration with direct dictionary lookup. Artefact: PR #20, stage8-refactoring.
* Ujwal(u3319048): Add each member’s actual contribution and supporting issue, commit, pull request or documentation evidence here.
* Ujwal(u3319048): The Stage 8 activities and evidence record was maintained and updated to document the debugging process, test results, refactoring and integration evidence.
## J. Required reflections

1. Which Copilot diagnosis appeared convincing but lacked evidence?

One of Copilot’s suggestions for F8-02 was that the appointment might have been removed from the data store or that the service might be using a different data-store instance. This initially seemed convincing because the system raised a LookupError when trying to retrieve the cancelled appointment.

However, this suggestion was not supported by the actual evidence. Investigation showed that the appointment was still stored and its status had correctly changed to CANCELLED. The real problem was that find_appointment() filtered out cancelled appointments.

This demonstrated that Copilot can suggest possible causes, but its suggestions must be checked against the actual code and test results before accepting them.

2. What evidence changed your group’s view?

The evidence that changed our group’s understanding came from inspecting the relevant data-store methods and running the regression tests.

For F8-01, inspecting has_practitioner_conflict() revealed that the practitioner ID comparison used != instead of ==. This explained why the system failed to detect bookings for the same practitioner at the same time.

For F8-02, inspecting find_appointment() showed that cancelled appointments were filtered out even though their records remained in the data store.

These findings helped the group move from initial assumptions to evidence-based root causes. We then applied small repairs and confirmed that the focused regression tests passed.

3. How did regression tests protect the refactoring?

Regression tests protected the refactoring by checking that the existing functionality continued to work after the internal code structure was changed.

Before refactoring, the full test suite passed with 75 tests. The refactoring simplified find_appointment() by replacing an unnecessary loop with direct dictionary lookup using self._appointments.get().

The existing appointment ID validation and behaviour for both existing and missing appointments were preserved. The tests also helped confirm that cancelled appointments remained retrievable and that the earlier F8-01 and F8-02 repairs continued to work.

After the refactoring was merged through PR #20, the full test suite was executed again in the original local repository. All 75 tests passed in 0.04 seconds. This provided evidence that the refactoring preserved the tested application behaviour.

Therefore, regression testing provided evidence that the refactoring improved the internal implementation without changing the required external behaviour.
## K. Ten formative questions

K. Ten formative questions

1. What should an engineer do before changing code in response to a failure?

An engineer should first reproduce the failure, examine the error message and traceback, compare the expected and observed behaviour, and investigate possible causes. They should collect evidence and identify the root cause before making the smallest appropriate code change.

2. Where should expected behaviour come from during debugging?

Expected behaviour should come from the approved system requirements, acceptance criteria and documented specifications. Tests should reflect these requirements rather than assumptions or personal opinions.

3. What is a debugging hypothesis?

A debugging hypothesis is a possible explanation for why a failure has occurred. It should be based on the available information and tested using evidence before being accepted as the root cause.

4. What is a regression test and why is it retained?

A regression test checks that previously working functionality continues to work after code changes. It is retained so that future modifications do not accidentally reintroduce old defects or break existing behaviour.

5. What is meant by root cause?

The root cause is the underlying reason that a problem occurs. Identifying it allows developers to fix the actual problem rather than only addressing its symptoms.

6. What is refactoring?

Refactoring is improving the internal structure, readability or maintainability of existing code without changing its external behaviour. Existing functionality should continue to work after the changes.

7. What is a swallowed exception?

A swallowed exception occurs when a program catches an exception but does not properly handle it, report it or pass it on. This can hide errors and make debugging more difficult.

8. What is a code smell?

A code smell is a sign that code may have structural or design problems, such as duplicated logic, long methods or deeply nested conditions. It does not necessarily mean the code is incorrect, but it may indicate that improvement is needed.

9. How should GitHub Copilot-generated debugging diagnoses be treated?

GitHub Copilot-generated diagnoses should be treated as suggestions rather than confirmed facts. Developers should inspect the actual code, reproduce the issue and verify each suggestion using evidence before accepting or applying it.

10. What is the Stage 8 engineering rule?

The Stage 8 engineering rule is to investigate before changing code, use evidence to identify the root cause, make the smallest justified repair, and verify the result using regression tests. Refactoring should preserve existing behaviour and be supported by passing tests and appropriate human review.

## L. Completion and handover

- [x] Existing project, earlier tests and stage records preserved.
- [x] Passing Stage 7 SHA and safe preparation details recorded.
- [x] Both defects reproduced with meaningful failing tests.
- [x] Both human hypotheses recorded before Copilot; actual suggestions evaluated with evidence.
- [x] Supported causes and minimal repairs explained; focused and full regression results recorded.
- [x] One genuine refactor verified under passing before/after tests.
- [x] Human PR review, feedback resolution and integrated retest recorded.
- [x] Tutorial, three reflections and ten formative responses complete.
- [x] Local recovery metadata excluded from submitted source.
- [x] Same project and full suite ready for Stage 9 after Stage 8 integration, verification and recording.

Verified integrated code SHA / result: see I.
Submitted SHA and evidence-only difference if any: [complete]
Unresolved issues or incomplete checks / owner / next action: 
Handover note: Stage 8 debugging, repair, regression testing and refactoring have been completed. Both seeded defects were investigated and repaired. The refactoring was integrated into main through PR #20, and the integrated project passed all 75 tests in the original local repository. The Stage 8 activity and evidence record has been updated, with unavailable preparation and formal review evidence disclosed. The project is ready for the next applicable stage, subject to final documentation and submission checks.
