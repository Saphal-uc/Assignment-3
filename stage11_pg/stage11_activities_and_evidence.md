# Stage 11 PG assurance activities and evidence

PG-only stage. Undergraduate students are not required to complete this record. UG-only groups retain this supplied template unchanged as intentionally not applicable; do not fabricate N/A responses. Optional UG participation is unassessed.

Blank student template. All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied file in stage11_pg/ in your EXISTING repository. Preserve project/, earlier records/tests and the protected common Stage 9 SHA. Do not copy staff references or fabricate AI evidence.

Group/tutorial: [response]
Assessed PG members and contributions: [response]
Optional UG contributors: [response or none]

## A Handover and human-first scope

Integrated Stage 10 code SHA / protected Stage 9 common SHA: [`9a4ea9e222bc522f557689bac631b364384fa53b` / `d4556d25090d48ebf993a85ec5d57343c0ac6c6f`]

Recoverable branch / baseline / actual commands, working directory and results: [`feature/stage11-pg-assurance`; current Stage 11 starting SHA: `13362ac3afec3c4d0153698390acf5dc40be1548`; working directory: `project/`; full baseline command: `python -m pytest -q`; result: `139 passed`; protected common command: `python -m pytest -q --ignore=tests/test_assurance.py --ignore=tests/test_rescheduling.py`; result: `106 passed`.]
Domain, store, services, queries, console, entry point, tests and rescheduling inspected: [I manually inspected `project/smartcare/domain.py`, `data_store.py`, `services.py`, `queries.py`, `console.py`, `project/main.py`, `tests/test_rescheduling.py` and `tests/test_workflows.py`. Domain rules validate identifiers, date/time values and status transitions. The store retains appointments and checks conflicts using scheduled appointments. Services coordinate booking, cancellation, rescheduling and listing. Queries return a sorted new list. The console handles expected input errors, and the existing tests check successful behaviour and state preservation after rejected operations.]
Selected PG feature and common workflow / requirements / code locations: [The selected PG feature is appointment rescheduling. The common workflow is appointment cancellation with retained history and reuse of the freed time slot. The required behaviour is that only scheduled appointments can be rescheduled or cancelled, practitioner conflicts are rejected, failed operations leave stored records unchanged, cancelled appointments remain available in history and their time slots can be reused with a new appointment ID. Relevant code locations are `project/smartcare/domain.py`, `project/smartcare/data_store.py`, `project/smartcare/services.py`, `project/tests/test_rescheduling.py`, `project/tests/test_workflows.py` and `project/tests/test_assurance.py`.]
Actual available earlier AI, issue, PR and dependency evidence: [Stage 10 evidence is recorded in `stage10_pg/stage10_activities_and_evidence.md`, Issue #33 and Pull Request #34. The evidence records Copilot planning, human supervision, independent review by Saphal, 33 rescheduling tests passed, 106 protected common tests passed and 139 cumulative tests passed. Stage 10 was integrated at SHA `9a4ea9e222bc522f557689bac631b364384fa53b`. Pull Request #35 contains later handover documentation. No new runtime dependency was added; `pytest 8.3.5` is used as the test tool.]
Missing evidence / honest limitation: [response]
Assets and trust boundaries: [The protected assets are the SmartCare source code, appointment records, patient and practitioner records, tests, repository history and assessment evidence. Input crosses the trust boundary when data enters through the console and service methods before reaching the domain objects and shared data store. Invalid identifiers, date/time values, status values and conflicting bookings must be rejected. Real patient information, passwords, API keys, access tokens and other private data must not be entered into Copilot. Only synthetic records such as P1, D1 and A1 will be used.]
Scope, assumptions, exclusions and initial observations made BEFORE Copilot:

- **Scope:** Review what happens when a scheduled appointment is moved to a conflicting time, and what happens to its record and time slot after cancellation.
- **Assumption:** The review uses synthetic appointments in the same in-memory SmartCare session. It does not assess whether records survive after the program closes.
- **Exclusions:** Adding new features, changing the console menu and replacing the data store are outside this review.
- **Initial observation from the baseline:** Before adding Stage 11 tests, the full suite passed all 139 tests, and the protected common suite passed all 106 tests. These runs show that the existing tests passed. The counts alone do not show whether a rejected reschedule leaves both appointments unchanged.
Confirmed Copilot mode / student entitlement / permissions / approval reference: [response]
Plan-only → human approval → bounded editing check / approved equivalent route: [response]
Overview/revision 2 availability / source: [response]
Assigned PG owner / independent reviewer: [response]

## B Original tutorial activities


### B1 Risk classification

| Scenario | Risk | Why | Control |
|---|---|---|---|
| AI explains a public Python error | Low | The explanation could be wrong, but no private data or code change is needed. | Share a small example and check the explanation by running it locally. |
| Student pastes an API key into AI | High | Someone who obtains the key could use the access it grants. | Use a placeholder. If a real key was shared, notify its owner and revoke or rotate it. |
| Agent proposes an unknown package | Potentially high | The package may be unnecessary or come from an untrusted source. | Check why it is needed and verify its source before approving installation. |
| AI-generated code logs patient names | High | A log creates another copy of identifying information that the task may not need. | Remove names from diagnostic logs and use synthetic records to check the output. |
| Agent modifies deployment configuration | High | A configuration change could affect access or interrupt the application. | Keep deployment changes outside this review. Any required change needs a human-reviewed diff and a recovery plan. |
### B2 Green Amber Red
Choose GREEN / AMBER / RED and justify each.

| Use | Classification | Reason and policy/control |
|---|---|---|
| Ask AI to explain a pytest fixture | GREEN | This is learning support. Use a small example with synthetic data and check that the fixture behaves as explained. |
| Generate 100 lines of assessed domain code | AMBER | This is a substantial contribution to assessed work. Use it only if the assessment explicitly permits code generation. Record what AI generated, review it and test it. If the task requires independent coding, this use is RED. |
| Paste a real patient record for debugging | RED | Debugging does not require a real patient’s details. Reproduce the problem with a synthetic record instead. |
| Use AI to draft test ideas, then verify them | AMBER | AI influences what gets tested. Where permitted, record its suggestions, compare them with existing tests and independently check that each new test detects a specific failure. |
| Agent autonomously deletes repository files | RED | The agent could remove source code, tests or assessment evidence without human review. Any necessary deletion requires a person to check the exact files and approve the change first. |

### B3 VERIFY patient search
Record one concrete question/evidence item for each letter against the current PatientService/shared-store contract.

| VERIFY element | Question or evidence |
|---|---|
| Validate | Does `PatientService.find_patient()` return the registered patient for a known ID, raise `LookupError` for a valid but unknown ID, and raise `ValueError` for a blank or invalid ID? |
| Examine | For a valid ID, trace the call from `PatientService.find_patient()` in `services.py` to `SmartCareDataStore.find_patient()` in `data_store.py`. The store returns `None` when the ID is absent; the service turns that result into `LookupError`. |
| Run meaningful tests | Register a synthetic patient as `P1` and check `service.find_patient("P1") is patient`. Then search for `"UNKNOWN"`, `" "` and `None`, checking the expected exception for each. |
| Inspect risks | Could a failed search create a record or change the original patient? Compare `store.list_patients()` before and after each failed search, and check that `P1` still refers to the same object with the same name. |
| Fit architecture/policy | Does the service use its existing shared data store? Patient lookup needs no new database, external package or patient-name logging. Use synthetic records for verification. |
| You remain responsible | As PG owner, I must check the implementation against the requirement, run the tests and record the actual results before accepting the lookup behaviour. |

### B4 TRUST decision
The feature passes tests but adds an unreviewed package and logs full patient records. Should it be accepted?

| TRUST element | Reason/evidence/action |
|---|---|
| Trace | Find the change that introduced the package and the logging statement. Check which requirement, if any, justifies adding the package or recording full patient details. |
| Review | Ask another team member to inspect the dependency and logging changes. The review should identify what data is written and who could read it. |
| Understand | Check what the package does and whether SmartCare can perform the same task without it. A passing functional test does not explain why the package is needed. |
| Secure | Remove full patient records from diagnostic logs. Use synthetic records to check the output, and keep the package out unless its need and source are verified. |
| Test | Run the existing tests again. Add a check that captures the diagnostic output and confirms that the feature works without writing the synthetic patient’s details to the log. |

Decision and reason: [Do not accept the feature as submitted. The tests show that the tested behaviour works, but they do not justify the new dependency or the disclosure of patient details. Reconsider acceptance after these concerns are resolved, reviewed and retested.]
Exit: Why is a technically correct AI-generated feature still potentially unacceptable? [A feature can return the correct result and still cause harm. For example, a patient search can find the right person while also writing their full record to a log. A test that checks only the returned patient would pass and miss that disclosure.]

### B5 Sanitised critique only
Identify the hard-coded demo-key placeholder, unnecessary requests import, patient-ID/name logging, fabricated lookup and missing test/provenance evidence. Do not copy or run the old audit target.

| Concern | Observed example evidence | Severity | Correction and recheck |
|---|---|---|---|
| Hard-coded demo key | The snippet assigns a placeholder directly to `API_KEY`. This shows an unsafe pattern, but it is not evidence that a real key was exposed. | Medium | Remove the unused assignment. Check the source and test examples for credentials without copying any values into the report. |
| Unnecessary dependency | The snippet imports `requests`, although patient lookup only needs the existing SmartCare data store. | Medium | Remove the import. Verify that lookup works using the shared store without installing `requests`. |
| Patient details in logs | The logging statement includes the patient ID and name. This creates a second copy of identifying information that lookup does not require. | High | Remove identifying details from diagnostic logs. Use a synthetic patient and check that neither the ID nor the name appears in captured logs. |
| Fabricated patient lookup | `search_patient` builds a dictionary from the supplied ID and name instead of checking registered records. It also returns `None` for an empty ID. | High | Use the existing patient service and store. Verify that a known ID returns the same registered object, a valid unknown ID raises `LookupError`, and a blank ID raises `ValueError`. Check that failed searches leave records unchanged. |
| Missing test and provenance evidence | The snippet shows no meaningful assertions or record of where the code came from and who reviewed it. | Medium | Require a source or diff link, a human review and reproducible tests for known, unknown and blank IDs before accepting the code. |

## C Actual risk register


### Verification of existing controls — AI-assisted follow-up

| Risk | Artefact | Likelihood | Impact | Control | Status |
|---|---|---|---|---|---|
| A rejected reschedule could raise the correct error but still change the original appointment or the appointment blocking the requested time. | `project/tests/test_rescheduling.py` — `test_reschedule_conflict_excludes_only_target_and_does_not_mutate` | Low for the tested conflict: the service checks for a clash before changing the time, and the test checks both records after rejection. | High: a receptionist could tell a patient that the move failed while the stored schedule shows a different time. | The test takes a snapshot of the store before requesting the conflicting time. After `ValueError`, it checks that the same appointment objects remain and that their IDs, patients, practitioners, times and statuses are unchanged. | Existing control identified. The Stage 11 starting suite passed; this is not a new assurance test or a reproduced defect. |
| Reusing a cancelled appointment’s time slot could overwrite the cancelled record and remove it from appointment history. | `project/tests/test_workflows.py` — `test_cancellation_frees_slot_but_preserves_appointment_history` | Low for the tested workflow: the test retrieves both records after the slot is reused and checks their different statuses. | High: the receptionist could lose evidence of the cancellation or mistake the replacement booking for the original appointment. | The test cancels A1, checks that its ID cannot be reused, then books A2 with the same practitioner at the freed time. It verifies that A1 is still the original cancelled object, A2 is scheduled, and both records remain stored. | Existing control identified. This test covers cancellation followed by rebooking; it does not exercise rescheduling before cancellation. |

## D Actual findings tests and corrective actions

For each of at least TWO new/materially strengthened tests, explain the earlier coverage gap and the incorrect behaviour its assertions detect. No duplicated unchanged tests. [The first test checks whether the same patient ID can belong to different patients in separate stores without leaking or replacing a record. The second combines operations that earlier tests checked separately: rescheduling, cancellation and reuse of the moved slot. The tests were drafted with ChatGPT assistance and run locally in `project/`.]

| Claim / risk / requirement | Location / version | Independent check / test | Observed result / finding or no finding | Action / owner | Recheck / limitation |
|---|---|---|---|---|---|
| Patient lookup must keep records separate between sessions. | `project/tests/test_assurance.py` on baseline `13362ac` with local test changes | `test_patient_lookup_is_separate_between_sessions` searches for P1 in store B after registering P1 only in store A, then registers a different P1 in B. | Passed. The failed lookup left B empty. After registration, each store returned its own patient object. No defect was observed. | Saphal Bhattarai: retain the regression test. No production change needed. | Full suite: 141 passed. This check covers two in-memory stores. |
| Cancelling a moved appointment must preserve its history when another booking reuses its new slot. | `project/tests/test_assurance.py` on baseline `13362ac` with local test changes | `test_reschedule_then_cancel_preserves_history_when_new_slot_is_reused` moves A1 to 11:00, cancels it, books A2 at 11:00 and clears the returned history list. | Passed. A1 remained cancelled at 11:00, A2 remained scheduled, and both records were still retrievable. No defect was observed. | Saphal Bhattarai: retain the combined workflow test. No production change needed. | Full suite: 141 passed. This check covers the tested sequence within one session. |

| Assurance test | Earlier gap | Input/setup | Meaningful assertion | Incorrect result detected | Evidence/result |
|---|---|---|---|---|---|
| Test 1 — Patient lookup across sessions | A lookup in one store does not show whether records are shared between sessions. | Register P1 in store A. Search for P1 in empty store B, then register a different P1 in B. | The failed search leaves B empty. Each store later returns its own P1. | A patient record leaks into another session or is replaced. | Passed: `test_patient_lookup_is_separate_between_sessions`. |
| Test 2 — Reschedule, cancel and reuse the moved slot | Earlier tests checked rescheduling and cancellation separately. | Move A1 from 09:00 to 11:00, cancel it, then book A2 at 11:00. Clear the returned history list. | A1 stays cancelled at 11:00, A2 stays scheduled, and both remain retrievable after the list is cleared. | Reusing the slot overwrites A1, or clearing the list deletes stored history. | Passed: `test_reschedule_then_cancel_preserves_history_when_new_slot_is_reused`. |
| Additional if useful | [response] | [response] | [response] | [response] | [response] |

| Suite | Command / project working directory | Tested code SHA | Actual result | Evidence |
|---|---|---|---|---|
| Assurance focused | `python -m pytest -v tests/test_assurance.py` from `project/` | Stage 11 starting commit `13362ac` plus local test changes | 2 passed in 0.03s | [Both assurance tests](../project/tests/test_assurance.py) |
| Previous PG independently | `python -m pytest -q --ignore=tests/test_assurance.py` from `project/` | Stage 11 starting commit `13362ac` plus local test changes | 139 passed in 0.12s | All earlier tests passed with the two new assurance tests excluded. |
| Common independently | `python -m pytest -q --ignore=tests/test_assurance.py --ignore=tests/test_rescheduling.py` from `project/` | Stage 11 starting commit `13362ac` plus local test changes | 106 passed in 0.10s | All protected common tests passed with the Stage 10 rescheduling and Stage 11 assurance tests excluded. |
| Full PG cumulative | `python -m pytest -q` from `project/` | Stage 11 starting commit `13362ac` plus local test changes | 141 passed in 0.13s | All 139 earlier tests and both new assurance tests passed together. |
| Integrated retest | [response] | [response] | [response] | [response] |

Confirmed defect / minimal correction / before-after evidence, or justified no-change decision: Neither new test exposed a defect. Patient lookup kept the two sessions separate, and reusing the moved appointment’s slot preserved its cancelled record. No production-code change was needed for these two scenarios.
Preserved earlier assertions / inspected test diff: Compared with `13362ac`, no tracked files under `project/smartcare/` or `project/tests/` changed. Git listed only the new `project/tests/test_assurance.py`. All earlier test assertions were preserved.

Unresolved failures, action and owner: No failures were observed in the local full suite: 141 tests passed in 0.13s. Saphal Bhattarai will rerun the full suite after the Stage 11 changes are reviewed and merged, then record the result in the Integrated retest row.

## E VERIFY assessment


| VERIFY element | Evidence | Finding/action |
|---|---|---|
| Validate against requirements | Stage 10 Issue #33 covers rescheduling. The common cancellation workflow requires a cancelled appointment to remain retrievable while its time slot can be reused. | The conflict test checked that a rejected move preserved both appointments. The new workflow test checked that A1 remained cancelled at its moved time after A2 booked that slot. |
| Examine implementation | `AppointmentService.reschedule_appointment()` checks for a practitioner conflict before calling `appointment.reschedule()`. Cancellation calls `Appointment.cancel()`, which changes the status without deleting the record. | The order of these operations explains why a rejected move leaves the records unchanged and why a cancelled appointment can still be retrieved. |
| Run meaningful tests | [Stage 11 assurance tests](../project/tests/test_assurance.py): 2 passed. Section D records 139 previous tests passed, 106 protected common tests passed and 141 full-suite tests passed locally. | The new tests covered two gaps: lookup across separate stores and the combined reschedule–cancel–reuse workflow. Neither test exposed a defect. |
| Inspect risks and assumptions | The lookup test used P1 in two stores. The appointment test cleared a returned history list, then retrieved the records again. Both used synthetic data. | Each store retained its own patient, and clearing the returned list did not erase appointment history. These results apply to the tested in-memory scenarios; they do not establish wider privacy or security guarantees. |
| Fit architecture and policy | The tests use the existing services and data store. The Git comparison with `13362ac` showed no changes to tracked production files or earlier tests. | Keep the new tests without changing production code. Section G records Copilot’s review; Section D identifies ChatGPT’s assistance in drafting the tests. |
| You remain responsible | Saphal Bhattarai ran the tests locally and recorded the results in Section D. Section G separates Copilot’s claims from the evidence used to check them. | No production fix is justified by these two checks. Independent human review and a retest after integration are still required before final sign-off. |

## F TRUST assessment


| TRUST element | Evidence | Status/action |
|---|---|---|
| Trace | [Issue #33](https://github.com/Saphal-uc/Assignment-3/issues/33) and [PR #34](https://github.com/Saphal-uc/Assignment-3/pull/34) link the rescheduling requirement to the Stage 10 implementation. Section G records Copilot’s review, and Section D identifies ChatGPT’s assistance with the two new tests. | The earlier implementation, AI suggestions and locally observed results are recorded separately so a reviewer can trace each claim to its source. |
| Review | The Stage 10 review covered PR #34. The Stage 11 changes add two assurance tests with different assertions. | Ask an independent reviewer to inspect the Stage 11 diff and check whether each test would fail if the behaviour it protects were broken. Record their feedback and the response in Section I. |
| Understand | A cancelled appointment keeps its ID and history, but its practitioner’s time slot becomes available. The new workflow test moved A1 to 11:00, cancelled it and booked A2 at 11:00. | A1 remained retrievable as cancelled and A2 was scheduled. This explains why the slot can be reused without overwriting the original record. |
| Secure | The tests use synthetic records. The lookup test checks that a failed search in one store does not return or change a patient from another store. | The result supports isolation between the two tested in-memory stores. It does not establish access control or project-wide privacy. Document the separate dependency, output and permissions checks in Section H. |
| Test | Section D records 2 focused assurance tests passed, 139 previous tests passed, 106 protected common tests passed and 141 tests passed in the full local run. | No production correction was needed for the tested scenarios. Run the full suite again after the reviewed changes are merged and record that result separately. |

## G GitHub Copilot audit

Sanitised material / actual prompt, context, version and response links: [Stage 11 Copilot review transcript](copilot_review.md). The reviewed version was `13362ac3afec3c4d0153698390acf5dc40be1548`. The first prompt omitted the source excerpts, so Copilot could not assess the behaviour. The follow-up supplied the service and domain methods, snapshot helpers, two existing tests and the pytest declaration. The test data used synthetic identifiers such as A1, A2 and D1.

Evidence that human scope and initial observations preceded Copilot: Section A records the selected rescheduling and cancellation workflows and the baseline results of 139 full-suite passes and 106 protected common passes. These are baseline results, not Stage 11 assurance-test results. Only the initial observations personally recorded before the audit are treated as human-first evidence.

Actual supported route or approved equivalent / access limitations: The review took place in VS Code Copilot Chat. The interface showed Agent, Local and Default permissions; no Plan option appeared in the inspected menu. The prompt requested a text-only review without commands, edits or installations. The interface alone does not establish institutional approval or student entitlement.

Significant earlier AI contributions reviewed / available evidence / missing provenance: The [Stage 10 evidence record](../stage10_pg/stage10_activities_and_evidence.md), [Issue #33](https://github.com/Saphal-uc/Assignment-3/issues/33) and [PR #34](https://github.com/Saphal-uc/Assignment-3/pull/34) document Copilot-assisted planning and human review of appointment rescheduling. These records do not establish who wrote each individual line of code.

| AI claim | Affected requirement/code/evidence | Observed vs speculative / human verification | Severity / Accept Modify Reject / reason | Outcome / correction or no change | Recheck / limit |
|---|---|---|---|---|---|
| [response] | [response] | [response] | [response] | [response] | [response] |

**Independent recheck:** From `project/` on branch `feature/stage11-pg-assurance`, I ran `python -m pytest -v tests/test_rescheduling.py::test_reschedule_conflict_excludes_only_target_and_does_not_mutate tests/test_workflows.py::test_cancellation_frees_slot_but_preserves_appointment_history`. Result: **2 passed in 0.03s**. The first test verified that the rejected move preserved both stored appointments. The second verified that the cancelled appointment remained retrievable when a new booking reused its slot. Neither test moved an appointment, cancelled it and then reused its new slot in one sequence.

No false/rejected suggestion, if applicable: [state honestly and explain checks]

## H Dependency provenance and privacy review


| Dependency/artefact | Source | Purpose | Licence/provenance | Verified? | Decision | Evidence link |
|---|---|---|---|---|---|---|
| Python 3.14.3 standard library | Python distribution | SmartCare uses `datetime` for appointment times, `enum` for statuses, `re` for input format checks and `argparse` for the entry point. | Python Software Foundation licence and notices for incorporated software. | The local pytest output reported Python 3.14.3. The application imports at baseline `13362ac` were standard-library or project-local imports. | Retain. No external runtime package was needed for the reviewed workflows. | [Python licence](https://docs.python.org/3.14/license.html) |
| pytest 8.3.5 | Python Package Index (PyPI) | Runs the automated tests; it is not an application runtime dependency. | The official release lists the MIT licence. | `requirements-dev.txt` pins `pytest==8.3.5`, and the local test output reported the same version. | Retain as a test dependency. Matching versions do not verify every installed package. | [Project declaration](../project/requirements-dev.txt) · [Official release](https://pypi.org/project/pytest/8.3.5/) |
| AI-assisted review and tests | Stage 10 handover, Stage 11 Copilot exchange and ChatGPT-assisted test drafting | Trace the source of the review claims and the two new assurance tests. | Section G records what Copilot reviewed. Section D records the source of the test drafts and the local results. | The two new tests passed locally, and the full local suite passed all 141 tests. | Retain the source acknowledgements and obtain independent review before integration. | [Stage 10 handover](../stage10_pg/stage10_activities_and_evidence.md) · [Assurance tests](../project/tests/test_assurance.py) |

Actual runtime imports / test-tool dependencies / versions checked: At baseline `13362ac`, the application directly imported `argparse`, `datetime`, `enum`, `re` and local `smartcare` modules. The development requirements file declared pytest 8.3.5. The local test session reported Python 3.14.3, pytest 8.3.5 and pluggy 1.7.0. Pluggy appeared in the test environment; it was not imported by the application.

Secret/data/output/input/permission/minimisation checks and evidence: The Copilot review used synthetic identifiers such as P1, D1 and A1. No real patient record or credential appeared in the supplied excerpts. The review prompt requested no commands, installations or edits. In `console.py`, patient lookup displays the requested patient’s ID and name; that user-facing output is distinct from writing a patient record to a diagnostic log. The inspected console code handles `ValueError` and `LookupError`. These checks do not establish that the entire repository or its history is free of secrets.

Requirements/model/code/tests/Stage 10 provenance links: [Issue #33](https://github.com/Saphal-uc/Assignment-3/issues/33) records the rescheduling task, and [PR #34](https://github.com/Saphal-uc/Assignment-3/pull/34) links it to the implementation and review. The [domain model implementation](../project/smartcare/domain.py) guards appointment status changes; the [service](../project/smartcare/services.py) checks for practitioner conflicts. The [rescheduling tests](../project/tests/test_rescheduling.py) and [Stage 11 assurance tests](../project/tests/test_assurance.py) show which outcomes were checked.

Bias/hidden assumptions / name formats / unnecessary fields / accessibility / scheduling policy: Patient registration requires a non-blank name but does not require a first-name/last-name split, gender or contact details. Scheduling uses local times at minute precision and checks for a scheduled appointment with the same practitioner at the same time. The assurance tests do not establish accessibility of the console or suitability for real clinical use.

Policy questions or unresolved provenance / responsible contact: The VS Code menu showed Agent, Local and Default permissions. These labels do not establish institutional entitlement or approval for automated edits. The unit teaching team or convenor is the contact for confirming the approved route. No broader approval is claimed.

## I Independent review and final audit statement

Human reviewer / PR or diff link / feedback: [response]
Corrections and recheck / approval before integration: [response]
Overall decision: [Acceptable / Acceptable with remediation / Not yet acceptable] [response]
Unresolved risks: [response]
Evidence supporting decision: Before independent review, both new assurance tests passed locally. The previous PG suite passed 139 tests, the protected common suite passed 106, and the full suite passed 141. The comparison with baseline `13362ac` showed no changes to existing production files or earlier tests. No production correction was needed for the two scenarios tested. These results are local; the integrated retest has not yet been run.
Remediation owner / action / status: [response]
Residual limitations and conditions of acceptance: [response]
Accountable reviewer and PG member sign-off: [response]
Integrated PG SHA / protected common SHA: [response]

## J Reflections

1. **Which risk would have been easy to miss if you only checked whether tests passed?**  
   I could have missed whether a cancelled appointment stayed in history after it had been moved and its new slot was booked again. All 139 earlier tests passed, but the rescheduling test and the cancellation test checked different sequences. The new test followed A1 from 09:00 to 11:00, cancelled it, and booked A2 at 11:00. It then checked that A1 was still retrievable as cancelled and A2 was scheduled. This showed me why reading the assertions matters more than relying on the pass count alone.

2. **Which AI audit finding was false or overstated?**  
   I did not identify a false finding in the Copilot review. In the first exchange, I supplied the requirements but left out the code, so Copilot correctly said it could not assess the behaviour. After I supplied the methods and assertions, it identified a sequence that the two tests did not cover. I checked that observation against the existing tests and ran the new combined test. It passed, so the finding was a gap in test coverage, not a defect in SmartCare.
3. What evidence supports your final trust decision? [response]

## K Ten formative questions


1. **What does least privilege mean?** Give a person or tool only the access needed for the current task. For example, reviewing SmartCare code does not require permission to edit files or install packages.

2. **What is provenance in AI-assisted software engineering?** Provenance is the record of where code, dependencies or suggestions came from and how they were checked. In Stage 11, the Copilot transcript records the review claims, while Section D identifies ChatGPT’s contribution to the test drafts.

3. **What is data minimisation?** Use only the data needed for the task. Synthetic IDs such as P1, D1 and A1 were enough to test appointment behaviour without sharing real patient information.

4. **What is dependency hallucination?** It occurs when AI recommends a package, version or API that does not exist, or claims it has capabilities it does not have. Check the official source and the project’s actual need before installing it.

5. **What is software supply-chain risk?** It is the risk that software is affected by a problem in a dependency or in how that dependency is built or distributed. Pinning `pytest==8.3.5` identifies the intended version, but does not by itself prove that an installed copy is trustworthy.

6. **What does VERIFY ask students to do?** Validate the requirement, Examine the implementation, Run meaningful tests, Inspect risks and assumptions, check Fit with architecture and policy, and remember that You remain responsible. For SmartCare, this meant checking the stored appointments after a rejected move, rather than checking only that an exception was raised.

7. **What does TRUST ask students to do?** Trace the source, obtain human Review, Understand the behaviour, check how the work is Secured, and Test the result. These checks help the team decide whether to accept the work and what limits to record.

8. **What does an AMBER AI-use classification mean?** The use makes a significant contribution and requires care. It may proceed only if the assessment permits it, and the student must document and verify the contribution. AI-generated test ideas are one example.

9. **Who remains responsible for professionally accepted AI-assisted software?** The people who review, approve and integrate the work remain responsible. As Stage 11 owner, I am responsible for explaining my tests and the evidence behind my conclusions.

10. **What is the Stage 11 engineering rule?** Identify the risk, verify the claim, make a trust decision, correct confirmed defects and recheck the result. In SmartCare, a missing test justified adding coverage; it did not justify changing production code when the new test passed.

## L Completion and Stage 12 handover


- [ ] Actual SmartCare scope and human-first observations recorded.
- [ ] All tutorial activities and every VERIFY/TRUST element complete.
- [x] At least two meaningful assurance tests with added-value explanations.
- [ ] Real findings/no-findings and corrective actions or no-change evidence recorded.
- [x] Earlier assertions preserved; common and PG suites independently checked.
- [ ] Copilot claims independently verified and actual decisions recorded honestly.
- [ ] Dependency/provenance/privacy review and residual limits complete.
- [ ] Independent human review, integration and retest recorded.
- [ ] All three reflections and ten formative questions answered.
- [ ] Accountable PG contribution/sign-off and protected UG pathway retained.

Unresolved issues / owner / handover action: No test failures were observed in the local run. Saphal Bhattarai will record the independent reviewer’s feedback, address any requested changes, and rerun the full suite on the integrated commit.

Tested code SHA / command / working directory / observed result: Local Stage 11 working tree based on `13362ac3afec3c4d0153698390acf5dc40be1548`, with `project/tests/test_assurance.py` added. From `project/`, `python -m pytest -q` reported `141 passed in 0.13s`. This was the pre-merge run.

Stage 12 handover links to same project/tests/assurance conclusion and limitations: [SmartCare project](../project/) · [Stage 11 assurance tests](../project/tests/test_assurance.py) · [Section D: findings and test results](#d-actual-findings-tests-and-corrective-actions) · [Section I: independent review and final audit statement](#i-independent-review-and-final-audit-statement). The results cover the tested in-memory workflows; final handover follows independent review and an integrated retest.
Begin Stage 12 after the previous applicable stage is integrated, verified and recorded. Its handout and blank record are already supplied.
