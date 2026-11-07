# Stage 6 activities and evidence

Complete this one group record. Link actual issues, diffs, tests and reviews; avoid copying entire histories. Blank fields are intentional. Duplicate rows as needed. Use synthetic data only. Every member records their own meaningful contribution. Do not invent results, reviews or Copilot use.

- Group/tutorial: [Thu 2:30 group 4]
- Members, GitHub usernames and cohorts: 

Hong Ruan - @realllchloe 

Saphal Bhattarai - @Saphal-uc

Ujwal B K - @UjwalBk1998

Srilakshmi Ravipati - @u3330161

Cohort: Thu 2:30 PM (all members)

- Repository URL:  https://github.com/Saphal-uc/Assignment-3
- Starting SHA: 1aa6e3a

## A Requirement to issue activities

### FR-02 Patient Search

- Title: Patient Search by ID
- Context: Receptionist need to find registered patients quickly using their patient IDs.
- Requirement: The system must allow a user to search for a patient using a valid patient ID.
- Acceptance criteria: The system returns the matching patient when the patient ID exists. It rejects a blank or invalid patient ID and raises an appropriate error when the patient cannot be found.
- Scope: Patient lookup and input validation in the service layer.
- Definition of Done: The lookup method is implemented, invalid inputs are handled, missing patients are reported appropriately, and the supplied tests pass.
- Owner: Ujwal BK
- Actual issue link: https://github.com/Saphal-uc/Assignment-3/issues/2

* Test command: PYTHONPATH=project python3 -m pytest project/tests/test_starter.py -v
* Working directory: st1-assignment-3 project root
* Observed result: 8 tests passed in 0.01 seconds.
* Additional check: git diff --check completed without reporting errors.

### FR-06 Appointment Cancellation with FR-07 retained history

- Title: Implement appointment cancellation with retained history
- Context: Receptionists need to cancel scheduled appointments while keeping the appointment record available for future lookup.
- Requirement:

FR-06: Allow cancellation only for scheduled appointments.

FR-07: Keep cancelled appointments available in the appointment history.

- Acceptance criteria: 
A scheduled appointment changes to CANCELLED.

The service returns the same stored appointment object.

The cancelled appointment remains retrievable using its ID.

A valid but unknown appointment ID raises LookupError.

A blank or invalid appointment ID raises ValueError.

Repeated cancellation or cancellation of a completed appointment raises ValueError.

Rejected cancellation leaves the appointment unchanged.

Existing tests and new cancellation tests pass.

- Scope: 

Implement AppointmentService.cancel_appointment() in project/smartcare/services.py, using the existing lookup and domain cancellation methods. Add focused tests in project/tests/test_services.py.

- Definition of Done: 

The cancellation method meets all acceptance criteria.

Meaningful tests verify cancellation, retained history and rejected operations.

The full available test suite passes.

A pull request links to this issue.

Another group member reviews and approves the change before merging.

Actual test results and review evidence are recorded in the Stage 6 evidence file.

- Owner: Saphal-uc
- Actual issue link: https://github.com/Saphal-uc/Assignment-3/issues/5

## B Commit quality

| Original example | Strong or Weak | Reason                                                       |
|---|----------------|--------------------------------------------------------------|
| changes | Weak           | The message does not explain what changed or why             |
| final version | Weak           | It does not identify the implemented functionality           |
| Add patient search by ID | Strong         | It clearly identifies the features being implemented         |
| fix stuff | Weak           | It does not explain the problem fixed                        |
| Prevent cancellation of completed appointments | Strong         | The message describe a specific behaviour and business rule. |

## C Over scoped PR review

A cancellation PR also renames unrelated patient fields, restructures unrelated code and adds a new dependency.

- Scope concerns: The pull Request combines appointment cancellation with unrelated patient-field renaming, code restructuring and a new dependency. This increases the scope of the review and makes it harder to identify the changes necessary for the cancellation requirement. 
- Responsibility and architecture concerns: Unrelated patient-field changes may affect patient management responsibilities, while cancellation belongs to appointment management. Combining these changes can increase coupling and introduce unintended effects on existing functionality.
- Testing and review concerns: The reviewer needs to verify appointment cancellation, retained appointment history, existing patient functionality and the effects of the new dependency. Regression tests are necessary to ensure that unrelated functionality continues to work.
- Changes to remove or separate, with reasons: Keep the appointment cancellation and retained history changes in the current Pull request. Move unrelated patient-field renaming and refactoring into separate Pull Requests unless they are essential to the requirement. Include the new dependency only if it is justified and necessary, with appropriate testing and documentation.

## D Challenge a weak Copilot review

GitHub Copilot says: "Looks good; tests pass."

- Missing evidence: Copilot did not explain what code it checked, which tests passed, and how the code meets the requirements. It also did not provide any test results.
- Follow-up review question 1: Does the code meet the acceptance criteria?
- Follow-up review question 2: Are there any unnecessary changes in the PR?
- Follow-up review question 3: Do the tests test valid and invalid inputs?
- Follow-up review question 4: Does the code follow the existing design and responsibilities?
- Follow-up review question 5: Which tests passed, and how did you verify the results?
- Additional questions if useful: Do you have any suggestions for improvement?

## E Team workflow agreement

| Practice | Team agreement |
|---|---|
| Branch naming | Name the branch based on the task. |
| Commit message convention | Write clear commit messages to describe the changes. |
| PR size | Each member should create a PR for their assigned task within the stage. Keep the PR focused on that task. |
| Another-member review requirement | Each PR must be reviewed by another group member. The reviewer checks if the code meets the Issue requirements and runs the tests before approval. |
| Merge rule | All tests must pass. The PR must be approved by another group member before merging. |
| Significant Copilot disclosure rule | Record significant Copilot suggestions and explain our decisions with reasons. If no issues are found, record the review result. |

## F Issue and backlog index

Create at least two focused issues. Add a linked practitioner-lookup issue or an explicit supporting criterion with the tutor if needed to cover all three service targets.

| Issue link | Requirement | Owner | Acceptance criteria or precise link | Status |
|---|---|---|---|---|
| https://github.com/Saphal-uc/Assignment-3/issues/2 | FR-02 Patient Search | Ujwal BK | See acceptance criteria in Issue #2 | Closed |
| https://github.com/Saphal-uc/Assignment-3/issues/5 | FR-06 Appointment Cancellation and FR-07 Retained History | Saphal-uc | See acceptance criteria in Issue #5 | Closed |
| https://github.com/Saphal-uc/Assignment-3/issues/6 | Practitioner Lookup | u3330161 | See acceptance criteria in Issue #6 | Closed |

## G Pull request evidence

Repeat this block per PR. Record actual events, not planned approvals.

PR #3 — Implement patient search by ID
- PR link and title: https://github.com/Saphal-uc/Assignment-3/pull/3 — Implement patient search by ID
- Linked issue and requirement: https://github.com/Saphal-uc/Assignment-3/issues/2 — FR-02 Patient Search
- Feature branch: stage06-patient-search
- Changed behaviour: Implemented patient search by ID in PatientService.
- Meaningful commits: 4aa83d7 — Implement patient search by ID.
- Test command, directory and observed result: 

PYTHONPATH=project python3 -m pytest 

project/tests/test_starter.py -v, 

st1-assignment-3 

project root, 8 tests passed in 0.01 seconds (recorded in the original Stage 6 file).

- Another-member reviewer: Saphal-uc
- Human observations recorded before Copilot: Saphal-uc reviewed the Patient Search code before merging. No written review was recorded; the exact review time was not recorded.
- Requirement, responsibilities, test assertions and unrelated-scope checks: The code meets the Patient Search requirements in Issue #2. It uses the existing data store to find patients and handles invalid or unknown IDs. The original 8 starter tests passed. The PR also updated the Stage 6 evidence file.
- Key feedback: Saphal-uc review feedback not recorded
- Author response/change and verification: No changes were needed.
- Reviewer recheck and approval: Saphal-uc reviewed the code, but no formal GitHub approval was recorded.
- Merge outcome and SHA: Merged by UjwalBk1998, commit ab169cf
- Significant Copilot assistance: none
- Linked issue closure: Issue #2 — Closed.
- Each member updated main: All four members updated main before starting Stage 7.
- Integrated verification after merge: python -m pytest -q, project/, 27 passed in 0.02s on final Stage 6 main, commit 099b7dd (final integrated run; not a separate test immediately after PR #3 merge).

PR #7 — Implement practitioner lookup service

- PR link and title: https://github.com/Saphal-uc/Assignment-3/pull/7 — Implement practitioner lookup service
- Linked issue and requirement: https://github.com/Saphal-uc/Assignment-3/issues/6 — Practitioner Lookup
- Feature branch: feature/practitioner-search
- Changed behaviour: Implemented practitioner lookup by ID.
- Meaningful commits: 93eb170 — Practitioner lookup PR commit.
- Test command, directory and observed result: python -m pytest -q, project/, 14 passed in 0.01s (reviewed code SHA 93eb170).
- Another-member reviewer: realllchloe
- Human observations recorded before Copilot: I checked the code and ran the tests. All 14 tests passed. Review submitted on 26 October 2026 at 10PM. https://github.com/Saphal-uc/Assignment-3/pull/7#pullrequestreview-5651110056
- Requirement, responsibilities, test assertions and unrelated-scope checks: The practitioner lookup uses the existing data store. The tests check valid and invalid IDs, missing practitioners and the returned practitioner object. No unrelated changes were found.
- Key feedback: No issues were found during the human review.
- Author response/change and verification: No changes were requested. All 14 tests passed.
- Reviewer recheck and approval: Approved by realllchloe on commit 93eb170. https://github.com/Saphal-uc/Assignment-3/pull/7#pullrequestreview-5651110056
- Merge outcome and SHA: Merged by realllchloe, commit b5d0690.
- Significant Copilot assistance: Copilot reviewed the practitioner lookup code and tests and did not find any issues.
- Linked issue closure: Issue #6 — Closed.
- Each member updated main: All four members updated main before starting Stage 7.
- Integrated verification after merge: All tests passed on updated main. Exact test count and tested SHA for this immediate run were not recorded; merge SHA b5d0690.

PR #8 — Patient Lookup Tests

- PR link and title: https://github.com/Saphal-uc/Assignment-3/pull/8 — Patient Lookup Tests
- Linked issue and requirement: https://github.com/Saphal-uc/Assignment-3/issues/2 — FR-02 Patient Search
- Feature branch: feature/patient-search-verification
- Changed behaviour: Added patient lookup tests.
- Meaningful commits: 484ba06 — Patient lookup tests PR commit.
- Test command, directory and observed result: python -m pytest -q, project/, 20 passed (reviewed code SHA 484ba06).
- Another-member reviewer: realllchloe
- Human observations recorded before Copilot: I checked the tests and ran them locally. All 20 tests passed. Review submitted on 28 October 2026 at 3PM. https://github.com/Saphal-uc/Assignment-3/pull/8#pullrequestreview-5677599479
- Requirement, responsibilities, test assertions and unrelated-scope checks: The tests check patient lookup behaviour and error handling. No unrelated service changes were found.
- Key feedback: No issues were found during the human review.
- Author response/change and verification: No changes were requested. All 20 tests passed.
- Reviewer recheck and approval: Approved by realllchloe on commit 484ba06. https://github.com/Saphal-uc/Assignment-3/pull/8#pullrequestreview-5677599479
- Merge outcome and SHA: Merged by realllchloe, commit f532ef8.
- Significant Copilot assistance: Copilot suggested adding tests for non-string patient IDs.
- Linked issue closure: Issue #2 — Closed.
- Each member updated main: All four members updated main before starting Stage 7.
- Integrated verification after merge: python -m pytest -q, project/, 20 passed on main, SHA f532ef8.

PR #9 — Appointment Cancellation

- PR link and title: https://github.com/Saphal-uc/Assignment-3/pull/9 — Appointment Cancellation
- Linked issue and requirement: https://github.com/Saphal-uc/Assignment-3/issues/5 — FR-06 Appointment Cancellation and FR-07 Retained History
- Feature branch: feature/appointment-cancellation
- Changed behaviour: Added appointment cancellation and retained appointment history.
- Meaningful commits: ca572dc — Appointment cancellation PR commit.
- Test command, directory and observed result: python -m pytest -q, project/, 27 passed (reviewed code SHA ca572dc).
- Another-member reviewer: realllchloe
- Human observations recorded before Copilot: I checked the code and ran the tests. All 27 tests passed. I found some duplicate imports, but they do not affect the implementation. We can clean them up later. Review submitted on 28 October 2026 at 9PM. https://github.com/Saphal-uc/Assignment-3/pull/9#pullrequestreview-5681036195
- Requirement, responsibilities, test assertions and unrelated-scope checks: The cancellation follows the existing appointment rules and keeps cancelled appointments available. The tests check invalid IDs and rejected cancellations.
- Key feedback: I found some repeated imports, but the code still works.
- Author response/change and verification: No changes were required before merging. All 27 tests passed.
- Reviewer recheck and approval: Approved by realllchloe on commit ca572dc. https://github.com/Saphal-uc/Assignment-3/pull/9#pullrequestreview-5681036195
- Merge outcome and SHA: Merged by realllchloe, commit 099b7dd.
- Significant Copilot assistance: Copilot found some imports below the existing tests.
- Linked issue closure: Issue #5 — Closed.
- Each member updated main: All four members updated main before starting Stage 7.
- Integrated verification after merge: python -m pytest -q, project/, 27 passed in 0.02s, commit 099b7dd.
## H Copilot collaboration record

Record meaningful required use, not every trivial completion. Repeat per significant interaction.

PR #7 — Practitioner Lookup (realllchloe)
- Member and task: realllchloe, PR #7 Practitioner Lookup.
- Prompt/purpose and relevant issue/diff: Asked Copilot to review PR #7 for Practitioner Lookup (Issue #6), including the code and tests. https://github.com/Saphal-uc/Assignment-3/pull/7
- Summary of output: Copilot reviewed the PR. It found no major issues.
- Human check against actual code, requirements and tests: I checked the code and ran the tests. All 14 tests passed.
- Decision — Accept / Modify / Reject: Accept.
- Reason: The PR met the Issue requirements. All tests passed.
- Verification/evidence: 14 tests passed. PR #7 was approved. https://github.com/Saphal-uc/Assignment-3/pull/7#pullrequestreview-5651110056

PR #8 — Patient Lookup Tests (realllchloe)
- Member and task: realllchloe, PR #8 Patient Lookup Tests.
- Prompt/purpose and relevant issue/diff: Asked Copilot to review the Patient Lookup tests in PR #8 (Issue #2). https://github.com/Saphal-uc/Assignment-3/pull/8
- Summary of output: Copilot did not find any problems with the code. It suggested adding tests for non-string patient IDs.
- Human check against actual code, requirements and tests: I checked the tests and ran them locally. All 20 tests passed.
- Decision — Accept / Modify / Reject: Reject.
- Reason: These extra tests were not needed for Stage 6. We planned to add more boundary tests in Stage 7.
- Verification/evidence: All 20 tests passed. PR #8 was approved. https://github.com/Saphal-uc/Assignment-3/pull/8#pullrequestreview-5677599479

PR #9 — Appointment Cancellation (realllchloe)
- Member and task: realllchloe, PR #9 Appointment Cancellation.
- Prompt/purpose and relevant issue/diff: Asked Copilot to review PR #9 for Appointment Cancellation (Issue #5), including the code and tests. https://github.com/Saphal-uc/Assignment-3/pull/9
- Summary of output: Copilot found some imports below the existing tests. It found no problems with the functionality.
- Human check against actual code, requirements and tests: I checked the code and ran the tests. All 27 tests passed. I found some duplicate imports, but they do not affect the implementation. We can clean them up later.
- Decision — Accept / Modify / Reject: Accept.
- Reason: The import issue did not affect the code. All 27 tests passed.
- Verification/evidence: All 27 tests passed. PR #9 was approved. https://github.com/Saphal-uc/Assignment-3/pull/9#pullrequestreview-5681036195

## I Human versus Copilot review comparison

Based on PR #9:

- Human reviewer noticed before consulting Copilot: I found some duplicate imports in the tests. All 27 tests passed.
- Copilot noticed: Copilot found some imports below the existing tests.
- Overlap: Both noticed issues with the imports.
- What did the human reviewer notice that Copilot did not: I found duplicate imports. Copilot only mentioned their location.
- What did Copilot identify that the human reviewer initially missed: Copilot noticed that some imports were placed below the existing tests.
- Unsupported or incorrect Copilot suggestion: No incorrect suggestions were found. Copilot's feedback matched the code.
- Human judgement accepted, modified or rejected, and why: I accepted Copilot's feedback. The import issue did not affect the code, so no changes were needed before merging.
- Which evidence justified merge approval: All 27 tests passed. The code met the Issue #5 requirements. The import issue did not affect the functionality. https://github.com/Saphal-uc/Assignment-3/pull/9#pullrequestreview-5681036195


## J Contributions

Repeat per member. Include only categories that describe actual work; write not applicable where appropriate. Pairing or mentoring can be supported by a short corroborated note.

- Member: UjwalBk1998
- Implementation: Implemented Patient Search (FR-02). https://github.com/Saphal-uc/Assignment-3/issues/2
- Testing: Added Patient Lookup tests in PR #8. https://github.com/Saphal-uc/Assignment-3/pull/8
- Review: Not applicable.
- Issue refinement: Worked on Issue #2 for Patient Search.
- Design and responsibility discussion: Participated in team discussions about the design and responsibilities.
- Debugging or integration: Not applicable.
- Documentation or team support: Provided Patient Search information and test evidence for the Stage 6 document. Also participated in team discussions.

- Member: u3330161
- Implementation: Implemented Practitioner Lookup. https://github.com/Saphal-uc/Assignment-3/issues/6
- Testing: Added Practitioner Lookup tests in PR #7. https://github.com/Saphal-uc/Assignment-3/pull/7
- Review: Not applicable.
- Issue refinement: Worked on Issue #6 for Practitioner Lookup.
- Design and responsibility discussion: Participated in team discussions about the design and responsibilities.
- Debugging or integration: Not applicable.
- Documentation or team support: Provided information for the Stage 6 evidence file and participated in team discussions.

- Member: Saphal-uc
- Implementation: Implemented Appointment Cancellation and retained appointment history (FR-06 and FR-07). https://github.com/Saphal-uc/Assignment-3/issues/5
- Testing: Added Appointment Cancellation tests in PR #9. https://github.com/Saphal-uc/Assignment-3/pull/9
- Review: Reviewed the Patient Search code in PR #3. No formal GitHub approval was recorded. https://github.com/Saphal-uc/Assignment-3/pull/3
- Issue refinement: Worked on Issue #5 for Appointment Cancellation.
- Design and responsibility discussion: Participated in team discussions about the design and responsibilities.
- Debugging or integration: Helped integrate the Patient Search changes in PR #3. (GitHub shows the merge under the UjwalBk1998 account.)
- Documentation or team support: Provided information for the Stage 6 evidence file and participated in team discussions.

- Member: realllchloe
- Implementation: Not applicable.
- Testing: Ran and checked the tests for PR #7, #8 and #9. All 14, 20 and 27 tests passed.
- Review: Reviewed and approved PR #7, #8 and #9. Used Copilot to help with the reviews. https://github.com/Saphal-uc/Assignment-3/pull/7#pullrequestreview-5651110056 ; https://github.com/Saphal-uc/Assignment-3/pull/8#pullrequestreview-5677599479 ; https://github.com/Saphal-uc/Assignment-3/pull/9#pullrequestreview-5681036195
- Issue refinement: Not applicable.
- Design and responsibility discussion: Participated in team discussions about the design and responsibilities.
- Debugging or integration: Merged PR #7, #8 and #9 into main. Closed Issues #2, #5 and #6. Updated main and ran the tests after merging.
- Documentation or team support: Managed the Stage 6 evidence and completed the Stage 6 document. Also participated in team discussions.

## K Exit question

Why is a high commit count not necessarily evidence of strong contribution?

A high commit count does not mean a strong contribution because commits may contain small or unnecessary changes. Code quality, testing, and actual work should also be considered when evaluating contributions.

## L Stage 6 formative questions

1. What is version control?

Version control is a system for tracking the history of a program. It can track the steps and changes in code. It helps team members work together at the same stage and go back to earlier versions if needed.

2. Why is a feature branch useful?

A feature branch helps developers work on a new feature without changing the main branch. It can also help teammates work together. The changes can be reviewed and tested before merging to improve the stability of the program.

3. What makes a commit a good engineering commit?

A good commit can define the change and explain the changes clearly to keep it readable.

4. What is a pull request?

A pull request is a request to merge the new code from the feature branch into the main branch. It allows team members to review the changes before merging.

5. What is the purpose of code review?

Code review can help find problems and check code quality. It can also help ensure that the changes meet the requirements.

6. What does a Git diff show?

A Git diff shows the changes between the updated and original versions. The related change information includes added, removed and modified lines.

7. What is a Definition of Done?

The Definition of Done is a list of conditions. The conditions have to be met before completing the task, such as passing tests.

8. What is the appropriate role of GitHub Copilot in pull-request review?

GitHub Copilot can help reviewers review the code as an assistant. It may find potential problems and suggest improvements. That can provide a reference for humans. The final decision is made by human reviewers.

9. Why should individual contribution not be judged only by commit count?

Commit count does not show the quality or workload. Contributions should also be evaluated based on testing, code reviews, debugging and documentation.

10. What is the Stage 6 engineering rule?

The engineering rules focus on the necessary changes to implement the function, reviewing the actual code, testing the changes and recording the evidence. Copilot will help with the review, and the decision is made by humans.

## M Completion and handover

- Starting SHA: 1aa6e3a
- Final Stage 6 code SHA: 099b7dd
- Test command: python -m pytest -q
- Working directory: project
- Observed result: 27 passed in 0.02s
- PR and another-member reviewer: 

PR #3 (Saphal-uc; no formal approval recorded): https://github.com/Saphal-uc/Assignment-3/pull/3 ; 

PR #7: https://github.com/Saphal-uc/Assignment-3/pull/7#pullrequestreview-5651110056 ; 

PR #8: https://github.com/Saphal-uc/Assignment-3/pull/8#pullrequestreview-5677599479 ; 

PR #9: https://github.com/Saphal-uc/Assignment-3/pull/9#pullrequestreview-5681036195

- Unresolved issue or none: None
- Stage 7 handover status: ready for tutor checkpoint
- Final submitted SHA if later than tested SHA: 05f00de (Stage 6 evidence update only).

- [x] Three Stage 6 service targets completed and checked.
- [x] Original supplied tests retained and passing.
- [x] At least two focused issues link requirements and acceptance criteria.
- [x] Feature work reviewed by another member using the actual diff.
- [x] Human-first review and required Copilot comparison recorded.
- [x] Feedback resolved and approval recorded before merge.
- [x] Everyone pulled main and integrated checks passed.
- [x] Required activities, quiz responses and contribution notes completed.
- [x] Only synthetic data included; confidential peer material kept out.
- [x] Tutor can trace a requirement through issue, code, tests, PR and checkpoint.

Do not write a file's own future commit SHA into that file. Record the tested code SHA first, then commit the evidence; explain the difference when submitting.
