# Stage 10 PG agentic rescheduling activities and evidence

PG-only stage. Undergraduate students are not required to complete this record. UG-only groups retain this supplied template unchanged as intentionally not applicable; do not fabricate N/A responses. Optional UG help is voluntary and unassessed.

All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage10_pg/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions. Protect the common Stage 9 SHA and UG Stage 12 pathway.

This is a blank student record. Use actual accessible links and concise evidence; do not invent an agent session, test result or approval. Retain this record's headings when linking equivalent issue/PR evidence.

Group/tutorial: Thursday 2:30 PM, Group 4

Assessed PG members and roles: 
- Hong Ruan — Stage 10 implementation and agent plan approval 
- Saphal — independent PR review

- Optional UG contributors: none

## A Access baseline and recovery

- Confirmed GitHub Copilot feature/mode, version/environment and teaching-team approval reference: 

1. We used GitHub Copilot in VS Code on macOS: Plan Mode for planning and Interactive Mode for implementation after human approval, with Manual Permissions.
2. VS Code version: 1.145.2 (Universal)
3. GitHub Copilot Chat: Built-in extension.
4. Our tutor confirmed by email on 8 November 2026 that this workflow is appropriate in principle and consistent with the Stage 10 requirements, subject to confirmation of the approved Copilot environment.


- Actual account access and tool permissions check: GitHub Copilot is accessible in VS Code with our GitHub account. Plan Mode and Interactive Mode are available. Manual Permissions is selected, and automatic approval for file edits and terminal commands is disabled.
- Live route or convenor-confirmed equivalent staged interaction: We used GitHub Copilot in VS Code. We started in Plan Mode and changed to Interactive Mode after reviewing and approving the final plan.
- Access limitation and tutor resolution if applicable: No
- Protected Stage 9 common SHA / recoverable reference: d4556d25090d48ebf993a85ec5d57343c0ac6c6f; tag stage9-common-baseline pushed to GitHub.
- Common baseline command / project working directory / actual result: 
1. Command: python -m pytest -q
2. Working directory: project/
3. Actual result: 106 passed
- Clean branch and preparer / recovery baseline: feature/stage10-rescheduling Hong Ruan / d4556d25090d48ebf993a85ec5d57343c0ac6c6f on main, protected by tag stage9-common-baseline. Branch feature/stage10-rescheduling was created from this commit and pushed to GitHub. The working tree was clean when checked.
- Evidence-only later SHA if different / explanation: Tested and integrated Stage 10 SHA: 9a4ea9e222bc522f557689bac631b364384fa53b (PR #34). The earlier Stage 9 baseline remains d4556d25090d48ebf993a85ec5d57343c0ac6c6f. The later documentation updates do not change the tested Python code.

## B Tutorial activities

### B1 Rewrite the vague task

“Improve SmartCare appointment scheduling.” Write your bounded goal, requirements, exclusions, constraints, acceptance criteria and Definition of Done: 
- Goal: Add a feature to reschedule an existing appointment.
- Requirements: Allow rescheduling for SCHEDULED appointments only. Check the new date and time, prevent conflicts with another scheduled appointment for the same practitioner, and keep the appointment ID, patient and practitioner unchanged.
- Exclusions: Do not change the behaviour of existing SmartCare features or add unrelated features.
- Constraints: Add the rescheduling feature in domain.py and services.py. Reuse the existing validation and in-memory DataStore. Do not change the storage method or other parts of the system unless required for rescheduling.
- Acceptance criteria: Valid rescheduling works. Invalid requests are rejected without changing the appointment. Appointment lookup and listing show the updated time.
- Definition of Done: The code is reviewed, new tests pass, and existing tests still pass.
Predicted changed files and human test intentions: 

Predicted changed files:
- project/smartcare/domain.py: Add the rescheduling rules.
- project/smartcare/services.py: Add the rescheduling service and check appointment conflicts.
- project/tests/test_rescheduling.py: Add tests for the new feature.

Human test intentions:
- Test if a SCHEDULED appointment can be rescheduled successfully.
- Test invalid dates and appointment IDs.
- Test time conflicts for the same practitioner.
- Test that CANCELLED and COMPLETED appointments cannot be rescheduled.
- Test rescheduling to the same time.
- Check that the appointment ID, patient and practitioner stay the same.
- Check that failed rescheduling does not change the appointment.
- Check that appointment lookup and listing show the new time.
- Check that the old time slot becomes available after rescheduling.

### B2 Judge every proposed plan step

| Proposed step | Accept / Modify / Reject | Requirement evidence and reason |
|---|---|---|
| Redesign database schema | Reject | SmartCare already uses an in-memory DataStore. Rescheduling does not need a new database design. We should keep the existing storage method. |
| Add notifications | Reject | Notifications are not part of the Stage 10 requirements. We only need to add the rescheduling feature. |
| Introduce calendar library | Reject | SmartCare already has date-time validation. We can reuse the existing code without adding a new calendar library. |
| Modify Patient | Reject | Rescheduling only changes the appointment date and time. We do not need to change the Patient class. |
| Add rescheduling | Accept | Rescheduling is the main requirement of Stage 10. It allows us to change the appointment date and time by following the existing SmartCare rules. |
| Rewrite all tests | Modify | We need to add new tests for rescheduling, but keep the existing tests unchanged to make sure the new feature does not break existing functions. |

### B3 Six proposed changes

| File or action | Expected? | Review concern and evidence needed |
|---|---|---|
| Appointment in project/smartcare/domain.py | Accept | The Appointment class should check the appointment status and validate the new date and time before updating it. This follows the existing domain design. |
| project/smartcare/services.py | Accept | The service needs to find the appointment and check for time conflicts before rescheduling. |
| Proposed sqlite_repository.py / schema change | Reject | SmartCare already uses an in-memory DataStore. We do not need to add a new database for rescheduling. |
| Patient fields in project/smartcare/domain.py | Reject | Rescheduling only changes the appointment date and time. We do not need to add new fields to the Patient class. |
| requirements-dev.txt adds calendar package | Reject | SmartCare already has date-time validation. We do not need a new calendar library. |
| Existing appointment assertions weakened | Reject | We need to keep the existing test assertions. If a test fails, we should fix the code. |

### B4 Approval gate

Agent says “All tests pass.” Give at least SIX distinct checks before approval.
1. Review the production code changes to make sure only the required files and functions are changed.
2. Review the new tests to make sure they cover all the Stage 10 requirements.
3. Check that the original tests have not been changed or weakened.
4. Run python -m pytest -q tests/test_rescheduling.py to check the new rescheduling tests.
5. Run python -m pytest -q --ignore=tests/test_rescheduling.py to check the original tests.
6. Run python -m pytest -q to check the full test suite.

Additional checks if useful: no

### B5 Exit question

Why does increasing AI autonomy increase rather than decrease the importance of software engineering discipline? 

The more autonomy an AI agent has, the less human review there may be during the process. Clear rules and limits help control what the agent can do and reduce risks. Code reviews and testing are still needed to check the final results.

## C Human task specification before AI

- Goal: Add a rescheduling feature to SmartCare. Allow users to change the date and time of an existing SCHEDULED appointment.
- Requirements RES-01–06 with RES-05-R2: 

1. Only SCHEDULED appointments can be rescheduled. CANCELLED and COMPLETED appointments cannot be rescheduled, even to the same time.
2. The new date and time must be a valid datetime, without timezone, seconds or microseconds.
3. Keep the same Appointment object, ID, patient and practitioner. Only update the date and time.
4. Raise ValueError for invalid or blank appointment IDs, and LookupError for unknown IDs.
5. Reject conflicts with another SCHEDULED appointment for the same practitioner at the exact new time. Different practitioners can use the same time.
6. Allow same-time rescheduling for SCHEDULED appointments as a no-op.
7. After rescheduling, the old time slot becomes available.
8. Update appointment lookup and listing in the same session, with the correct sorting.
9. If rescheduling fails, keep the original appointment unchanged.
- Out of scope: Do not change the behaviour of existing SmartCare features or add unrelated features.
- Architecture constraints: 

1. Add Appointment.reschedule(new_date_time: datetime) -> None in domain.py for status and date-time validation.
2. Add AppointmentService.reschedule_appointment(appointment_id: str, new_date_time: datetime) -> Appointment in services.py for appointment lookup and conflict checks.
3. Reuse the existing validate_date_time() and has_practitioner_conflict() functions. Use exclude_appointment_id to exclude the current appointment from conflict checks.
4. Update the existing Appointment object instead of creating a new one.
5. Keep the existing in-memory DataStore. Do not add a database or change the storage method.

- Acceptance criteria: 
1. A SCHEDULED appointment can be rescheduled to a valid and available time.
2. The appointment keeps the same object, ID, patient and practitioner.
3. Invalid requests are rejected with the correct errors, without changing the appointment.
4. Time conflicts for the same practitioner are prevented.
5. Same-time rescheduling is allowed for SCHEDULED appointments.
6. After rescheduling, the old time slot becomes available.
7. Appointment lookup and listing show the updated time in the correct order.
8. CANCELLED and COMPLETED appointments cannot be rescheduled.

- Definition of Done: 
  - Implement Appointment.reschedule() in domain.py and AppointmentService.reschedule_appointment() in services.py. Make sure they meet all the rescheduling requirements.
  - Add new tests for rescheduling without weakening the existing tests.
  - Review the production code and test changes separately.
  - Run the new tests, original tests and full test suite. All tests must pass.
  - Fix any problems found during code review or testing.
  - Get another group member to review the PR before merging.
  - Record the AI contributions, review decisions and test evidence in the Stage 10 MD.
- Issue / PG owner: #33 Hong Ruan
- Human expected positive, negative and boundary tests:

  **Positive tests:**
  - A SCHEDULED appointment can be rescheduled to a valid free time.
  - The same Appointment object, ID, patient and practitioner are kept.
  - A different practitioner can use the same date and time.
  - The old time slot becomes available after rescheduling.
  - Appointment lookup and listing show the updated time in the correct order.

  **Negative tests:**
  - Invalid or blank appointment IDs raise ValueError.
  - Unknown appointment IDs raise LookupError.
  - A time conflict with another SCHEDULED appointment for the same practitioner raises ValueError.
  - CANCELLED and COMPLETED appointments cannot be rescheduled.
  - Failed rescheduling does not change the original appointment.

  **Boundary tests:**
  - Rescheduling a SCHEDULED appointment to the same time is allowed as a no-op.
  - Reject a new date and time if it is not a Python datetime object.
  - Reject a new datetime if it contains timezone information.
  - Reject datetime values with nonzero seconds or microseconds.
  - CANCELLED and COMPLETED appointments cannot be rescheduled, even to their original time.

- Allowed files: 
  - project/smartcare/domain.py — Add the Appointment rescheduling method.
  - project/smartcare/services.py — Add the rescheduling service method.
  - project/tests/test_rescheduling.py — Add new rescheduling tests.
  
- Forbidden/unnecessary files and changes: 
  - Do not modify files outside the allowed file list.
  - Do not modify data_store.py or change the existing in-memory storage method.
  - Do not change the fields, methods or behaviour of the Patient and Practitioner classes.
  - Do not change or weaken existing tests.
  - Do not add a database, notifications or new libraries.
  - Do not add unrelated features or change existing SmartCare behaviour.
  - Do not modify project/README.md. It will be updated manually.

- Baseline/recovery link: 
  
  **Stage 9 baseline:** The reviewed and tested Stage 9 commit on main.

  **Recovery reference:** stage9-common-baseline Git tag.

  **Stage 9 SHA:** d4556d25090d48ebf993a85ec5d57343c0ac6c6f

- Evidence that human analysis preceded agent use: I reviewed the Stage 10 requirements and prepared Issue #33 before using the Copilot agent.

## D Agent plan and approval

Actual plan-only prompt/context and response or confirmed equivalent artefacts: https://github.com/Saphal-uc/Assignment-3/issues/33

| Plan step / action | Requirement link | Reason | Expected files | Accept / Modify / Reject | Conditions / evidence |
|---|---|---|---|---|---|
| Step 1 — Add Domain rescheduling | RES-01, RES-02, RES-06 | Validate the new time and only allow SCHEDULED appointments to be rescheduled. | domain.py | Modify | The first plan did not clearly mention Appointment.reschedule(new_date_time: datetime) -> None. I wanted to clarify this to make sure it followed my plan. It also did not clearly say that CANCELLED and COMPLETED appointments must raise ValueError, so I asked Copilot to add these details. |
| Step 2 — Add Service rescheduling | RES-01, RES-03, RES-04, RES-06 | Check appointment IDs and practitioner conflicts before changing the appointment time. | services.py | Modify | The first plan used date_time. I asked Copilot to use reschedule_appointment(appointment_id: str, new_date_time: datetime) -> Appointment as required in Stage 10. |
| Step 3 — Add rescheduling tests | RES-01–RES-06, RES-05-R2 | Test successful changes, invalid requests, conflicts and unchanged state after failure. | test_rescheduling.py | Modify | The first plan did not include a separate production code review before adding tests. I asked Copilot to add this review step and stop after writing the tests, so I could review them separately and run the tests myself. |
Approved bounded scope / forbidden changes / verification plan: 

  - Copilot was only allowed to change domain.py, services.py and add test_rescheduling.py.

  - It was not allowed to change DataStore, existing tests, README, dependencies or unrelated features.

  - After Copilot finished each part, I checked its summary and the actual Git Diff before giving it the next instruction. I also ran the tests myself to make sure the changes did not break the existing code.

Human plan approver and approval before edits: 

I compared Copilot's final plan with my original plan to make sure it matched what I wanted. I then approved the plan and switched to Interactive Mode. I asked Copilot to work on one part at a time and reviewed each change before continuing.

Tool permissions and any expanded-scope requests / decision: 

I used GitHub Copilot in VS Code with Interactive Mode and Manual Permissions. I only allowed Copilot to change the files I selected for each step. I checked the changes and clicked Allow Once before Copilot could apply them. Copilot did not make or request any changes outside my original plan.

## E Production diff review

Actual proposal / branch diff / version reviewed: https://github.com/Saphal-uc/Assignment-3/pull/34

| File | Change purpose and reason | Requirement / test link | Expected? | Architecture OK? | Decision | Notes / correction |
|---|---|---|---|---|---|---|
| project/smartcare/domain.py | Added Appointment.reschedule() to check the new time and appointment status before changing the time. | RES-01, RES-02, RES-06 | Yes | Yes | Accept | I checked the actual Git Diff. The changes followed my plan and only updated the appointment time. No correction was needed. |
| project/smartcare/services.py | Added reschedule_appointment() to find the appointment, check for time conflicts and call the domain method. | RES-01, RES-03, RES-04, RES-06 | Yes | Yes | Accept | I checked the actual Git Diff. It reused the existing conflict check and did not change unrelated functions. No correction was needed. |

Every changed file inspected, including new/untracked files: 
I checked all three changed files: domain.py, services.py and the new test_rescheduling.py. I reviewed the actual code changes and confirmed that no other files were changed. https://github.com/Saphal-uc/Assignment-3/pull/34/files

Unexpected changes, scope creep, secrets/dependencies/configuration, unrelated cleanup: None https://github.com/Saphal-uc/Assignment-3/pull/34/files

## F Separate test review

| Test | Criterion | Actual assertion | Assertion meaningful / adequate? | Agent changed expected behaviour? | Human or agent authorship | Decision and reason |
|---|---|---|---|---|---|---|
| test_domain_reschedule_changes_only_time | RES-01, RES-02 | The Domain method returns None. Only the appointment time changes. The ID, patient, practitioner and status stay the same. | Yes. It checks the updated time, original participant objects and unchanged appointment details. | No change identified. | Copilot-generated. | Accept. The assertions check the required Domain behaviour and keep the other appointment details unchanged. |
| test_domain_reschedule_same_time_is_a_no_op | RES-06 | The Domain method returns None and keeps the appointment unchanged when rescheduling to the same time. | Yes. A valid same-time request keeps the appointment unchanged. | No change identified. | Copilot-generated. | Accept. The Domain method allows same-time rescheduling without changing the appointment. |
| test_domain_reschedule_invalid_datetime_does_not_mutate | Datetime validation contract, RES-06 | The Domain method raises ValueError for invalid datetime values. The appointment stays unchanged. | Yes. It checks the correct error and confirms invalid inputs do not change the appointment. | No change identified. | Copilot-generated. | Accept. The test covers six invalid datetime cases and checks that the original appointment remains unchanged. |
| test_domain_reschedule_rejects_non_scheduled_without_mutation | RES-06, AC-RES-05 | The Domain method raises ValueError for CANCELLED and COMPLETED appointments, including same-time requests. The appointment stays unchanged. | Yes. It checks the correct error and unchanged state after an invalid status request. | No change identified. | Copilot-generated. | Accept. The test covers four invalid status cases and checks that the original appointment remains unchanged. |
| test_reschedule_preserves_identity_updates_lookup_listing_and_releases_old_slot | RES-01, RES-02, RES-05-R2, AC-RES-06-R2, RES-06 | The Service returns the same appointment with an updated time. The ID and participants stay the same. Lookup and listing show the new time and order. The old slot can be reused. | Yes. It checks object identity, updated time, lookup results, listing order and old-slot reuse. | No change identified. | Copilot-generated. | Accept. The test checks successful Service rescheduling and confirms that related functions show the correct results. |
| test_reschedule_to_same_time_is_a_no_op | RES-06 | The Service returns the original appointment and keeps its details unchanged when rescheduling to the same time. It does not create a duplicate record in DataStore. | Yes. It checks the returned object, unchanged state and DataStore contents. | No change identified. | Copilot-generated. | Accept. The Service handles same-time rescheduling without changing the appointment or creating a duplicate record. |
| test_reschedule_allows_time_used_by_another_practitioner | RES-04, AC-RES-04 | The Service returns the original appointment when rescheduling to a time used by another practitioner. Both appointments have the same time. | Yes. The test checks the returned object and confirms that different practitioners can use the same time. | No change identified. | Copilot-generated. | Accept. Different practitioners can have appointments at the same time. |
| test_reschedule_ignores_non_scheduled_appointments_at_destination | RES-04, BR-05 | The Service successfully reschedules an appointment to a time used by a CANCELLED or COMPLETED appointment. The original appointment object is returned with the new time. | Yes. Both cases succeed, and the appointment time is updated correctly. | No change identified. | Copilot-generated. | Accept. Only SCHEDULED appointments cause time conflicts. CANCELLED and COMPLETED appointments do not block rescheduling. No extra time restrictions are required by the assignment. |
| test_reschedule_conflict_excludes_only_target_and_does_not_mutate | RES-04, AC-RES-03, RES-06 | The Service raises ValueError when rescheduling causes a conflict with another SCHEDULED appointment. All appointments stay unchanged. | Yes. The test checks the correct error and compares the DataStore before and after the failed operation. | No change identified. | Copilot-generated. | Accept. The Service rejects time conflicts and keeps the original appointments unchanged. |
| test_reschedule_rejects_invalid_or_unknown_ids_without_mutation | RES-03, AC-RES-02 | The Service raises ValueError for invalid appointment IDs. Unknown IDs raise LookupError. Failed rescheduling keeps the original appointments unchanged. | Yes. The test checks both error types. It also checks that the stored appointments stay unchanged. | No change identified. | Copilot-generate. | Accept. The test covers four invalid ID cases and one unknown ID case. All failed requests keep the original appointments unchanged. |
| test_reschedule_rejects_invalid_datetimes_without_mutation | Datetime validation contract, RES-06 | The Service raises ValueError for invalid datetime values. Failed rescheduling keeps the original appointments unchanged. | Yes. The test checks six invalid datetime cases. Also, it checks that the DataStore stays unchanged. | No change identified. | Copilot-generated. | Accept. The test checks invalid datetime inputs at the Service level. Also, it confirms that failed requests do not change stored appointments. |
| test_non_scheduled_appointment_cannot_be_rescheduled | RES-06, AC-RES-05 | The Service raises ValueError when rescheduling CANCELLED or COMPLETED appointments. This includes requests using the same time. All appointments stay unchanged. | Yes. The test checks four invalid status cases. Also, it checks that the DataStore stays unchanged. | No change identified. | Copilot-generated. | Accept. The Service rejects rescheduling for CANCELLED and COMPLETED appointments. Failed requests do not change the stored appointments. |

Comparison with original common tests / any proposed weakening: The original 106 tests were kept unchanged. There was no proposed weakening. Copilot added new tests for rescheduling separately.
Independent human checks and corrections: I reviewed the new tests and compared them with my original requirements, acceptance criteria and test boundaries. I checked the expected errors, object identity and time conflicts. Then, I reviewed the failed-request tests to make sure the original appointments stayed unchanged. No corrections were needed.

## G Actual verification

| Requirement / acceptance scenario | Test or demonstration | Meaningful expected result | Actual result | Evidence / version |
|---|---|---|---|---|
| RES-01 / AC-RES-01 successful move | test_reschedule_preserves_identity_updates_lookup_listing_and_releases_old_slot | A SCHEDULED appointment can be moved to a valid and available time. | Passed. The appointment time changed from 09:00 to 11:00. | project/tests/test_rescheduling.py — 33 passed. |
| RES-02 same object and participant identities | test_reschedule_preserves_identity_updates_lookup_listing_and_releases_old_slot | The appointment keeps the same object, ID, patient and practitioner after rescheduling. | Passed. The same appointment object, ID, patient and practitioner were kept. | project/tests/test_rescheduling.py — 33 passed. |
| RES-03 / AC-RES-02 unknown and invalid IDs | test_reschedule_rejects_invalid_or_unknown_ids_without_mutation | Invalid appointment IDs raise ValueError. Unknown IDs raise LookupError. The original appointments stay unchanged. | Passed. All five cases raised the expected errors. The stored appointments stayed unchanged. | project/tests/test_rescheduling.py — 33 passed. |
| RES-04 / AC-RES-03 conflicting practitioner | test_reschedule_conflict_excludes_only_target_and_does_not_mutate | Rescheduling to a time used by another SCHEDULED appointment with the same practitioner raises ValueError. The appointments stay unchanged. | Passed. The Service raised ValueError. All stored appointments stayed unchanged. | project/tests/test_rescheduling.py — 33 passed. |
| AC-RES-04 different practitioner allowed | test_reschedule_allows_time_used_by_another_practitioner | Appointments with different practitioners can use the same time. Rescheduling succeeds. | Passed. The Service returned the original appointment. Both appointments had the same time. | project/tests/test_rescheduling.py — 33 passed. |
| RES-06 / AC-RES-05 cancelled and completed | test_non_scheduled_appointment_cannot_be_rescheduled | CANCELLED and COMPLETED appointments cannot be rescheduled, even to the same time. All appointments stay unchanged. | Passed. All four cases raised ValueError. The DataStore stayed unchanged. | project/tests/test_rescheduling.py — 33 passed. |
| RES-05-R2 / AC-RES-06-R2 lookup and listing order | test_reschedule_preserves_identity_updates_lookup_listing_and_releases_old_slot | Lookup shows the updated appointment time. Listing shows the appointments in the correct time order. | Passed. Lookup returned the updated appointment. The listing showed A2 before A1 after rescheduling. | project/tests/test_rescheduling.py — 33 passed. |
| Self-exclusion and same-time no-op | test_reschedule_to_same_time_is_a_no_op, test_reschedule_conflict_excludes_only_target_and_does_not_mutate | The Service allows rescheduling to the same time without changing the appointment. Only the target appointment is excluded from conflict checks. | Passed. Same-time rescheduling returned the original appointment without changes. Conflicts with other SCHEDULED appointments were rejected. | project/tests/test_rescheduling.py — 33 passed. |
| Invalid datetime and failed-state snapshots | test_domain_reschedule_invalid_datetime_does_not_mutate, test_reschedule_rejects_invalid_datetimes_without_mutation | Invalid datetime values raise ValueError. Failed rescheduling keeps the original appointment and DataStore unchanged. | Passed. All six invalid datetime cases were rejected at both Domain and Service levels. The original appointment and DataStore stayed unchanged. | project/tests/test_rescheduling.py — 33 passed. |
| Successful old-slot reuse | test_reschedule_preserves_identity_updates_lookup_listing_and_releases_old_slot | The old time slot becomes available after successful rescheduling. Another appointment can use that time. | Passed. A new appointment was booked at the old time. The listing showed the appointments in the correct order. | project/tests/test_rescheduling.py — 33 passed. |

| Suite | Command / working directory | Code SHA | Actual count and result | Evidence |
|---|---|---|---|---|
| Focused PG | python -m pytest -q tests/test_rescheduling.py from project/ on merged main | 9a4ea9e222bc522f557689bac631b364384fa53b | 33 passed, 0 failed | Manually run on main; project/tests/test_rescheduling.py. |
| Common independently | python -m pytest -q --ignore=tests/test_rescheduling.py from project/ on merged main | 9a4ea9e222bc522f557689bac631b364384fa53b | 106 passed, 0 failed | Manually run on main; original tests excluding test_rescheduling.py. |
| Full cumulative | python -m pytest -q from project/ on merged main | 9a4ea9e222bc522f557689bac631b364384fa53b | 139 passed, 0 failed | Manually run on main; full pytest suite. |
| Integrated retest | python -m pytest -q from project/ after PR #34 merged into main | 9a4ea9e222bc522f557689bac631b364384fa53b | 139 passed, 0 failed | Integrated retest on merged main, reported by Hong Ruan; [PR #34](https://github.com/Saphal-uc/Assignment-3/pull/34). |


Failures / diagnosis / corrections and reruns / unresolved concerns: No test failures were found. All 33 rescheduling tests and 106 original tests passed. No corrections or reruns were needed.


## H Decisions corrections and independent review

| Significant agent action | Human review and evidence | Accept / Modify / Reject and reason | Manual correction or recovery | Recheck evidence |
|---|---|---|---|---|
| Copilot added Appointment.reschedule() in domain.py. | I reviewed the Git Diff and compared the changes with my original requirements. The method validates the new time and checks the appointment status. [PR #34](https://github.com/Saphal-uc/Assignment-3/pull/34/files) | Accept. The changes followed my plan and kept the existing Domain design. | None. | Domain rescheduling tests passed. test_rescheduling.py — 33 passed. |
| Copilot added reschedule_appointment() in services.py. | I reviewed the Git Diff and compared the changes with my original requirements. The Service uses the existing conflict check and calls the Domain method. [PR #34](https://github.com/Saphal-uc/Assignment-3/pull/34/files) | Accept. The changes followed my plan and kept the existing Service design. | None. | Service rescheduling tests passed. test_rescheduling.py — 33 passed. |
| Copilot added test_rescheduling.py including 12 test functions and 33 test cases. | I reviewed the test file and compared it with my original requirements, acceptance criteria and test boundaries. I checked the assertions and confirmed that the original tests were unchanged. [PR #34](https://github.com/Saphal-uc/Assignment-3/pull/34/files) | Accept. The tests cover successful rescheduling, invalid inputs, time conflicts and unchanged state after failed requests. | None. | test_rescheduling.py — 33 passed. Original tests — 106 passed. Full suite — 139 passed. |


Final proposal decision: Accepted
Evidence supporting decision: I reviewed the production code and tests separately. The changes followed my approved plan and met the Stage 10 requirements. All 33 rescheduling tests and 106 original tests passed. [PR #34](https://github.com/Saphal-uc/Assignment-3/pull/34).
If rejected, how the required feature was subsequently completed and verified: not applicable
Saved proposal and targeted recovery details if needed: not applicable
Human explanation of every changed method and limitations: 
- Appointment.reschedule() updates the appointment time. AppointmentService.reschedule_appointment() handles the rescheduling process, including appointment lookup and conflict checks.
- Both methods only allow SCHEDULED appointments to be rescheduled. They do not check past dates, appointment duration or clinic hours.
Another PG / willing UG / tutor reviewer, actual PR/diff review and feedback: Saphal review for [PR #34](https://github.com/Saphal-uc/Assignment-3/pull/34). PR #34 was merged. No specific review feedback was recorded here.
Corrections, recheck and actual approval before integration: https://github.com/Saphal-uc/Assignment-3/pull/34
Integrated PG SHA / common protected SHA: Integrated PG SHA: 9a4ea9e222bc522f557689bac631b364384fa53b (merged main, 139 tests passed). Common protected SHA: d4556d25090d48ebf993a85ec5d57343c0ac6c6f (stage9-common-baseline).
Each assessed PG member's implementation, supervision and test contribution: 
- **Hong Ruan:** Prepared the requirements and approved the Copilot plan. Supervised the Domain and Service implementation. Reviewed the code and tests separately and verified the test results.
- **Saphal:** Responsible for independent review of PR #34, including code changes and tests.

Optional UG help, acknowledged separately: none

## I Four reflections

1. Which agent change had the greatest blast radius? 

The reschedule_appointment() method in services.py had the greatest blast radius. It handles appointment lookup and checks for scheduling conflicts. Additionally, it updates appointment times. A mistake could affect appointment data and listing results.

2. Did the plan predict it? 

Yes. My original plan already covered these risks. It included conflict checks and required failed rescheduling to keep the original appointment unchanged.

3. What did you reject or manually correct? 

I changed Copilot's original plan because some details were not clear. I asked it to follow my method requirements and include the validation rules. I also asked for separate code and test reviews. No manual code changes were needed.

4. What evidence justified final approval? 

I reviewed the code changes and tests to make sure they met my original requirements. I manually ran all the tests. All 33 new tests and 106 original tests passed. No unexpected changes were found.

## J Ten formative questions

1. What is the difference between an AI assistant and an engineering agent? 

- AI Assistant: Humans do most of the work. The AI helps answer questions, explain code and provide suggestions. Humans perform the actual tasks.
- AI Agent: It can plan tasks, use tools, inspect files and modify code based on given requirements. It has more autonomy, so clear permission limits and human approval are needed.

2. What is the simplified agent loop used in Stage 10? 

An AI agent loop is a process that repeats several steps. The agent makes a plan, takes action and checks the results. If the task is not finished, it repeats these steps until the task is completed or human approval is needed.

3. Why should an agent plan be reviewed before repository edits begin? 

Plan review helps us check if the agent understands the requirements. We can find mistakes or unnecessary steps before the agent changes the code. This helps reduce risks and keeps the changes within the task scope.

4. What is meant by the blast radius of a software change? 

Blast radius means how many parts of a project may be affected by a code change. In AI-assisted development, AI agents may change many files or functions to complete a task. This can affect existing functions and increase the risk of problems. We should limit unnecessary changes to reduce this risk.

5. Why is diff review essential for agentic changes? 

Git diff shows what code has been changed. It helps us check if the AI agent made the correct changes or if any unnecessary changes were added. We can find problems before accepting the code.

6. What is a human approval gate? 

A human approval gate is a point where the AI agent must wait for human approval before continuing. It allows us to check the plan or actions before the agent makes changes.

7. What is test accommodation and why is it dangerous? 

Test accommodation means changing or weakening tests to make the code pass. It is dangerous because the tests may pass even when the code still has problems.

8. What is rollback in the context of agentic software engineering? 

Rollback allows us to return to an earlier working version when the AI agent makes incorrect changes. It helps protect the existing code and reduces the risk of losing working features.

9. Who remains accountable for accepted agentic changes? 

The developer is responsible for AI-generated code. Even though AI does the actual work, the developer is still responsible for the results. We need to review the changes, test the code and make sure it meets the requirements before accepting it.

10. What is the Stage 10 engineering rule? 

The most important rule is human control. We need to define the task requirements and plan before using the AI agent. Then we review the agent's plan and approve it before any code changes. After approval, the agent can only make changes within the approved scope and permissions.

## K Completion and Stage 11 handover

- [x] Common Stage 9 checkpoint protected; UG pathway unaffected.
- [x] RES-01–06 and RES-05-R2 implemented in the same project.
- [x] Domain/service boundaries, current exceptions and coding standard preserved.
- [x] Positive/negative/boundary cases and failed-state checks verified.
- [x] Common tests remain valid and independently passing; full suite passes.
- [x] Plan reviewed before bounded actions; every file and test diff inspected.
- [x] Actual agent route, decisions, corrections and rechecks recorded honestly.
- [x] No unrelated features, persistence, dependencies or staff solutions introduced.
- [x] Another-member or tutor review and integrated retest complete.
- [x] Tutorial, four reflections, ten formative responses and PG contributions complete.
- [x] Each PG member can explain their code and supervision.
- [x] README PG note, actual integrated SHA and limitations recorded.

Unresolved issues / owner / action: None

Stage 11 handover references to extension, tests, dependencies and actual AI/review evidence:

Stage 10 added Appointment.reschedule() in domain.py and AppointmentService.reschedule_appointment() in services.py. New tests were added in test_rescheduling.py. No new dependencies were added. Copilot planning and human review evidence are recorded in this MD, Issue #33 and PR #34.

[Saphal tested the merged code from [PR #34](https://github.com/Saphal-uc/Assignment-3/pull/34) at commit `9a4ea9e222bc522f557689bac631b364384fa53b`. From `project/`, `python -m pytest -q` passed all 139 tests, and `python -m pytest -q --ignore=tests/test_rescheduling.py` passed all 106 common tests.]

Submitted SHA / explanation if later than tested code: Tested and integrated SHA: 9a4ea9e222bc522f557689bac631b364384fa53b. The final submission may have a later SHA because the Stage 10 MD and README are updated after testing. No Python code was changed in these documentation updates.

Stage 11 materials are supplied from the beginning. Begin Stage 11 only after Stage 10 has been integrated, verified and recorded. UG follows the protected common code from Stage 9 to Stage 12.
