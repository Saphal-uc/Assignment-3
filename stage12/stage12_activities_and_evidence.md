# Stage 12 activities and evidence

BLANK student response template. Supplied from the beginning in stage12/ in your EXISTING repository; complete it only when you reach Stage 12 after the previous applicable stage is integrated, verified and recorded; preserve project/, tests, earlier records and Git history. UG/common and PG/extended scope must be explicit. Use concise results and versioned links, not copied logs or source. No staff answers or fabricated approvals.

Group/tutorial: SmartCare – Software Technology 1, Assignment 3.
Members and UG/PG applicability:
- Srilakshmi – UG
- Ujwal – UG
- Chloe – PG
- Saphal – PG
Group scope: Mixed UG/PG group. UG members follow Stages 6–9 and 12. PG members follow Stages 6–12, including the Stage 10 and 11 extensions.


## A Release scope and starting SHA

Release label/version and requirements baseline: The project is SmartCare, and the proposed release label is v1.0. The release follows the Undergraduate (UG) requirements baseline and includes Stages 6, 7, 8, 9 and 12. The release scope covers patient and practitioner management, appointment booking, cancellation, appointment history, practitioner appointment listing and the related testing and documentation.
Common starting SHA / branch / applicable members: Branch: main



Current SHA: 7e349978947726dd44a49fa50a167b097459ccba



Repository: https://github.com/Saphal-uc/Assignment-3



Applicable members: All UG group members.
PG starting SHA / branch / applicable members or not applicable: Not applicable. This project follows the Undergraduate pathway.
Working-state review and approved integration: The local main branch is up to date with origin/main, and the working tree is clean. The automated test suite completed with 141 passed, 0 failed and 0 errors. Final PR integration approval is not confirmed in the available evidence.
Protected common candidate and PG differences: The common UG release candidate will use the verified main branch. The final release SHA must be recorded before submission. PG-specific requirements are not applicable.
Feature freeze / owner / verifier: A feature freeze will be applied before final release testing. No new features will be added after the freeze. The team will focus on bug fixes, regression testing and documentation.
- Owner: Saphal


## B Requirements and release readiness matrix

Tutorial activity 1: All tests pass, README setup is incomplete, one dependency is unreviewed and a known limitation is undocumented. Decide Release / Release with conditions / Do not release and justify: DO NOT RELEASE.

Although all tests pass, the README setup instructions are incomplete, one dependency is unreviewed and a known limitation is undocumented. These issues must be addressed before release. The team should complete the README, review the dependency and document the known limitation.

Tutorial activity 2 and actual readiness matrix. Add exact requirement/acceptance IDs, evidence and reviewer; distinguish common/PG applicability.

| Release claim / requirement / scope | Evidence | Location/link and SHA | Reviewer | Sufficient? | Gap/action |
|---|---|---|--|---|---|
| Cancellation history works | Automated tests for cancellation and retained appointment history passed. | [Regression tests](https://github.com/Saphal-uc/Assignment-3/blob/main/project/tests/test_regressions.py) — SHA: `7e349978947726dd44a49fa50a167b097459ccba` | Chloe | Partially | Confirm final demonstration and review. |
| Architecture responsibilities are appropriate | Code is organised into domain, data store, services and queries modules. | [SmartCare repository](https://github.com/Saphal-uc/Assignment-3) | everyone | Partially | Complete architecture review. |
| Rescheduling is safe — PG only | Not applicable to UG pathway. | N/A | N/A | N/A | No action required. |
| AI use is responsible — common recheck / PG assurance | AI usage acknowledgement and project documentation. | Project documentation and AI usage record. | To be confirmed | Partially | Verify common AI acknowledgement. PG assurance is not applicable. |
| System is maintainable | Modular code structure and automated tests. | [SmartCare repository](https://github.com/Saphal-uc/Assignment-3) | To be confirmed | Partially | Complete maintainability review. |
| FR-01–03 register/find and validation | Domain and service tests cover registration, lookup and validation. | [Domain tests](https://github.com/Saphal-uc/Assignment-3/blob/main/project/tests/test_domain.py) and [Service tests](https://github.com/Saphal-uc/Assignment-3/blob/main/project/tests/test_services.py) | everyone | Partially | Confirm all acceptance criteria. |
| FR-04–05 booking/conflict rules | Booking and appointment conflict tests passed. | [Workflow tests](https://github.com/Saphal-uc/Assignment-3/blob/main/project/tests/test_workflows.py) and [Regression tests](https://github.com/Saphal-uc/Assignment-3/blob/main/project/tests/test_regressions.py) | everyone  | Partially | Confirm complete requirements coverage. |
| FR-06–08 cancellation/history/find | Cancellation, history and lookup service tests passed. | [Service tests](https://github.com/Saphal-uc/Assignment-3/blob/main/project/tests/test_services.py) | everyone  | Partially | Confirm all acceptance criteria and demonstration evidence. |
| FR-09 and QRY/FP listing/filter/order/purity | Practitioner appointment listing, filtering, ordering and record-preservation tests passed. | [Query tests](https://github.com/Saphal-uc/Assignment-3/blob/main/project/tests/test_queries.py), [Service tests](https://github.com/Saphal-uc/Assignment-3/blob/main/project/tests/test_services.py), [Issue #32](https://github.com/Saphal-uc/Assignment-3/issues/32) — SHA: `7e349978947726dd44a49fa50a167b097459ccba` | To be confirmed | Partially | Confirm final integration and reviewer approval. |
| UI full console sequence and error recovery | Workflow and starter tests provide automated evidence. | [Workflow tests](https://github.com/Saphal-uc/Assignment-3/blob/main/project/tests/test_workflows.py), [main.py](https://github.com/Saphal-uc/Assignment-3/blob/main/project/main.py) | everyone  | Partially | Add full console demonstration evidence. |
| Session-only scope / FR-10 retired | Requirements baseline has not yet been verified. | Project requirements documentation. | everyone  | Not confirmed | Verify session-only behaviour and FR-10 retirement. |
| PG RES and assurance integration | Not applicable to UG pathway. | N/A | N/A | N/A | No action required. |

## C Full regression results

| Suite/scope | Environment/version | Working directory and command | Tested SHA | Actual result | Evidence link |
|---|---|---|---|---|---|
| Complete common | [response] | [response] | [response] | [response] | [response] |
| Complete PG if applicable | [response] | [response] | [response] | [response] | [response] |
| Affected focused checks after correction | [response] | [response] | [response] | [response] | [response] |
| Full integrated recheck | [response] | [response] | [response] | [response] | [response] |
Prior assertions preserved / reviewed test diff: [response]
Remaining failure / limitation: [response]


## D Console and end to end demonstration

| Demo step | Synthetic setup/input | Expected requirement | Observed result | Evidence/link |
|---|---|---|---|---|
| Problem and stakeholders | [response] | [response] | [response] | [response] |
| Register and find Patient and two Practitioners | [response] | [response] | [response] | [response] |
| Valid booking | [response] | [response] | [response] | [response] |
| Same practitioner exact-time conflict rejected | [response] | [response] | [response] | [response] |
| Different practitioner same time allowed | [response] | [response] | [response] | [response] |
| Cancel SCHEDULED and retain/find CANCELLED object | [response] | [response] | [response] | [response] |
| Invalid/repeated cancellation rejected | [response] | [response] | [response] | [response] |
| Default all-status listing | [response] | [response] | [response] | [response] |
| Explicit filtering / empty vs unknown / deterministic order | [response] | [response] | [response] | [response] |
| Invalid date/status/menu/lookup recovery and continued operation | [response] | [response] | [response] | [response] |
| Session-only limitation and normal exit | [response] | [response] | [response] | [response] |
| One meaningful requirement-linked pytest test explained | [response] | [response] | [response] | [response] |
| Architecture and one actual AI decision / known limitation | [response] | [response] | [response] | [response] |
| PG reschedule identity/participants/time and no-op | [response] | [response] | [response] | [response] |
| PG conflict/invalid status/failure non-mutation | [response] | [response] | [response] | [response] |
| PG old slot / current lookup/list ordering / assurance risks | [response] | [response] | [response] | [response] |
Stable demo owner / fresh process / command: [response]
PG demonstrations through service/tests or not applicable: [response]




## E Final code quality and AI review

Review owner: Saphal Bhattarai (PG).
Release candidate checked: `7e349978947726dd44a49fa50a167b097459ccba`.
Scope: SmartCare domain objects, shared data store, services, queries, console, tests and the recorded AI-assisted changes. Release test results for this candidate are recorded in Section C.

| Review area | Code/evidence location | Finding or no finding | Correction/no change and recheck |
|---|---|---|---|
| OOP responsibilities and pure-query boundaries | [Domain](../project/smartcare/domain.py), [services](../project/smartcare/services.py), [queries](../project/smartcare/queries.py) | An appointment controls its own status. The service checks booking conflicts across appointments. The query selects and sorts records without changing the source collection. | Retain these responsibilities. The assurance test checks that clearing a returned list does not remove stored history. |
| PascalCase and snake_case naming | `AppointmentService`, `SmartCareDataStore`, `reschedule_appointment`, `select_appointments` | The reviewed class names use PascalCase, and the reviewed methods and functions use snake_case. | No rename is justified for these examples. |
| Useful type hints and meaningful docstrings | `PatientService.find_patient`, `PractitionerService.find_practitioner`, and the console menu helpers | The lookup methods have type hints, but their docstrings still describe a starter TODO and `NotImplementedError`, even though the methods are implemented. Some console helper parameters lack type hints. | Record this as a documentation and readability issue. If corrected before submission, review the diff and rerun the relevant tests. |
| Four-space indentation and imports/layout | [Services](../project/smartcare/services.py), [console](../project/smartcare/console.py) | The reviewed method bodies use four-space indentation. Imports distinguish standard-library modules from project modules. Some console functions could be separated more clearly by blank lines. | This is a readability issue. No behaviour change is needed. |
| Focused methods / duplication / dead or commented code | `run_menu` and the individual menu handlers in `console.py` | Menu handlers separate registration, lookup, booking and cancellation. Some display code is repetitive, but the inspected examples do not show that it causes a release failure. | Keep the tested behaviour. Do not introduce a broad console rewrite during release verification. |
| Globals / leakage / unnecessary inheritance or frameworks | `run_menu`, `SmartCareDataStore`, `AppointmentService` | The menu creates a store for the session and passes it to the services. The two-store assurance test verifies that one session’s patient is not returned by another. | Retain the shared store within each session. No additional framework or inheritance is needed. |
| No SQLite/persistence/repository ABCs/speculative features | [Data store](../project/smartcare/data_store.py), [services](../project/smartcare/services.py) | The reviewed application uses in-memory records. Durable storage and external calendar integration are outside its release scope. | State the session-only limitation in the release notes; do not add a database to satisfy an invented requirement. |
| Synthetic data / secrets / dependencies / provenance | [Development requirements](../project/requirements-dev.txt), [Stage 11 Section H](../stage11_pg/stage11_activities_and_evidence.md#h-dependency-provenance-and-privacy-review) | The reviewed tests use synthetic records. `pytest==8.3.5` is a development dependency. The reviewed runtime imports were standard-library or project-local modules. | Retain the dependency pin. The review of these files does not establish that every historical commit or installed package is free of risk. |
| Significant common Copilot contributions and human verification | [Stage 8 debugging record](../stage08/stage08_activities_and_evidence.md), [Issue #19](https://github.com/Saphal-uc/Assignment-3/issues/19) | Copilot suggested that lookup filtered out cancelled appointments. The team checked the stored record and the lookup condition before accepting that explanation. | Retain the repair and regression test. The record was still stored; cancellation itself had not deleted it. |
| PG plan/diff/test approvals and Stage 11 VERIFY/TRUST | [Stage 10 record](../stage10_pg/stage10_activities_and_evidence.md), [PR #34](https://github.com/Saphal-uc/Assignment-3/pull/34), [Stage 11 evidence](../stage11_pg/stage11_activities_and_evidence.md) | Stage 10 records the bounded rescheduling work and its review. Stage 11 found a missing test sequence rather than a production defect. Chloe reviewed the two assurance tests and approved the Stage 11 PR. | Retain the tests and the no-production-change decision. Use Section C for the final candidate’s regression evidence. |

| AI claim | Affected requirement/code | Human check | Accept/Modify/Reject and reason | Actual outcome/action or no change |
|---|---|---|---|---|
| A cancelled appointment could not be retrieved because the lookup excluded it. | FR-07; `SmartCareDataStore.find_appointment()` | The Stage 8 investigation found the cancelled object still in the store and identified the lookup filter. | Accept. The filter explained the observed failure. | The lookup was corrected and the regression test retained. |
| The appointment might instead have been deleted or looked up in a different store. | FR-07; cancellation and retrieval | The team found the same object in the same store after cancellation. | Reject. The evidence contradicted this explanation. | No change to cancellation or store ownership was needed for this defect. |
| The earlier tests did not combine a successful reschedule, cancellation and reuse of the moved slot. | PG rescheduling and FR-07; [Stage 11 assurance tests](../project/tests/test_assurance.py) | The earlier move test reused the old slot. The cancellation test used an appointment that had never moved. The new test exercised the combined sequence. | Accept as a coverage gap. The claim did not establish a program defect. | The new test passed: A1 stayed cancelled at its moved time and A2 was scheduled there. No production fix was justified. |

Access route or approved equivalent / limitations: The recorded Stage 11 review used VS Code Copilot Chat in Agent mode with a review-only prompt. The interface displayed Local and Default permissions; those labels do not prove institutional entitlement or approval for automated editing. This section evaluates the recorded exchange and does not claim a new Stage 12 Copilot session.

Available AI evidence and missing evidence honestly disclosed: The Stage 8 debugging record, Stage 10 issue/PR evidence and [Stage 11 Copilot transcript](../stage11_pg/copilot_review.md) identify the claims and checks available for review. ChatGPT assisted with the Stage 11 test drafts; Saphal ran the tests locally, and Chloe reviewed their assertions. The records do not identify the author of every line of code. Additional AI assistance used to draft this release documentation should also be acknowledged under the unit policy.


## F README and reproducibility check

| README item | Location | Verifier      | Result/gap |
|---|----|---------------|---|
| Purpose and included common/PG scope | [project/READ.md,Section 1-2] | [UjwakBK1998] | [Purpose and common functionality documented. PG rescheduling functionality also documented.] |
| Out-of-scope capabilities and known limitations | [project/README.md, Section 9] | [UjwalBk1998] | [Session-only storage, synthetic-data requirement and production limitations documented.] |
| Confirmed teaching Python version and dependency installation | [project/README.md, Section 3–4] | [UjwalBK1998] | [Python 3.14.3 and pytest 8.3.5 verified locally. Teaching-approved Python version still needs confirmation.] |
| Working directory / demo / interactive / test commands | [project/README.md, Sections 4–6] | [UjwalBK1998] | [Setup, normal run, interactive run and test commands documented and tested.] |
| Repository structure and architecture responsibilities | [project/README.md, Sections 7–8] | [UjwalBk1998] | [Project structure and responsibilities of the main modules documented.] |
| Responsible AI summary / synthetic-data rule | [project/README.md, Sections 9–10] | [UjwalBk1998] | [Human review of AI-generated suggestions and synthetic-data requirement documented.] |
| Release label/version and SHA links | [project/README.md, Section 11; root README.md] | [UjwalBk1998] | [Final release label and SHA still need to be added after integration and release verification.] |
Root README index and project/README verified: [project/README.md reviewed for setup, features, architecture, testing commands, responsible AI use and known limitations. Root README index still requires final group details, verified code SHA and submitted SHA.]
Fresh clone or extracted ZIP / candidate identity: [Pending. Fresh clone or extracted release ZIP verification has not yet been completed. Candidate SHA to be recorded after final integration.]
Verifier and clean environment / actual version: [Member 4 (UG) performed local verification using Python 3.14.3 and pytest 8.3.5 in the project virtual environment. Independent clean-environment verification is still pending.]
Setup/run/test commands and observed results: [From project/: python -m pip install -r requirements-dev.txt; python main.py; python main.py --interactive; python -m pytest -q. Normal application launch and interactive menu were verified. Automated tests: 139 passed in 0.11 seconds. Results are from the local environment and must be associated with the final tested SHA.]
Missing local file or setup gap / remedy and recheck: [The root README still contains starter information and incomplete group-index placeholders. Update the introduction and complete the group index after final integration. Confirm the approved teaching Python version and perform a fresh-copy setup and regression test before release.]


## G Known limitations debt and release notes

Delivered features: [response]
Important fixes: [response]
Architecture/quality improvements: [response]
Known limitations: [response]
AI-assisted development note: [response]

| Debt item | Impact | Priority | Future action | Accepted? / release rationale |
|---|---|---|---|---|
| [response] | [response] | [response] | [response] | [response] |
Session-only synthetic data and minute-precision local time: [response]
Production auth/roles, portal, notifications, billing/insurance, clinical AI exclusions: [response]
Scale/concurrency, timezone policy, operations/monitoring, accessibility/usability limitations: [response]
Difference between accepted scope limit and unresolved required behaviour: [response]
PG assurance residual risks / owner / status or not applicable: [response]


## H Release findings and corrective action

| Requirement/claim | Reproduction/observation | Impact/severity | Owner/action | Corrective diff | Focused/full recheck | Residual limit |
|---|---|---|---|---|---|---|
| [response] | [response] | [response] | [response] | [response] | [response] | [response] |
Justified no-change conclusion if no defect found: [response]
Release blockers still open / status: [response]


## I Git review and integration evidence

Issue / PR / diff links and reviewed SHA: [GitHub Issues and Pull Requests from Stages 7–9 were used to track implementation and testing contributions. Relevant PRs include the Stage 9 query implementation and test changes. Add the actual PR links and reviewed commit SHA before final submission.]
Independent reviewer / feedback / response: [Group members reviewed each other's pull requests and provided feedback on implementation scope and missing tests. For example, feedback on PR #31 identified that test_queries.py was missing. The query tests were requested and added before considering the work complete.]
Integration commit / full recheck: [Stage 9 changes were integrated into the main branch through reviewed and merged pull requests. The integrated project was tested using python -m pytest -q, with 139 tests passing in the local environment. Record the exact integration commit SHA and final recheck result.]
Tracked and untracked file inspection / cleanliness: [Git status and diff checks were used to inspect repository changes. git diff --check returned no whitespace errors. The working tree still contained a modified project/README.md during documentation work; final cleanliness must be verified after committing all approved changes.]
Secrets/staff material/caches/tool-metadata exclusion check: [The repository and proposed submission package must be checked for credentials, real patient information, private staff materials, virtual environments, Python caches, pytest caches and temporary files. Final ZIP exclusion verification is pending.]
Candidate recovery plan / known-good SHA: [The team will preserve the last verified integrated commit on main as the recovery point. If a release candidate fails verification, the team can return to that known-good SHA and correct the issue on a separate branch. Record the actual recovery SHA before submission.]
Named substantive contributions: [Member 4 (UG): Stage 7 patient lookup and appointment conflict testing; Stage 9 query-related work and testing; Stage 12 README documentation, Git integration review, release verification and submission-package checks.]


## J Human release decision

Decision — READY FOR COURSE RELEASE / READY WITH DOCUMENTED LIMITATIONS / NOT YET READY: [READY WITH DOCUMENTED LIMITATIONS (provisional — subject to final group review and release verification).]
Approver / date / rationale and evidence: [Approver: Pending group agreement.
Date: Pending final release review.
Rationale: The SmartCare application has demonstrated successful automated testing, with 139 tests passing in the local environment. The application launches successfully, and the interactive console menu operates correctly. Documentation covers the application features, architecture, setup instructions and known limitations. Final independent verification, integration SHA confirmation and submission-package checks remain outstanding.]
What risks remain / conditions / owners: [Approver: Pending group agreement.
Date: Pending final release review.
Rationale: The SmartCare application has demonstrated successful automated testing, with 139 tests passing in the local environment. The application launches successfully, and the interactive console menu operates correctly. Documentation covers the application features, architecture, setup instructions and known limitations. Final independent verification, integration SHA confirmation and submission-package checks remain outstanding.]
Can the team explain the system: [The team should be able to explain the SmartCare problem, stakeholders, requirements, domain model, application architecture, appointment booking and conflict rules, cancellation history, query operations, testing approach and known limitations. Each member must be prepared to explain their own contribution.]
Can a change be recovered:  [Yes. Git branches, commits and merged pull requests provide a recovery history. The team should identify and record the last known-good integrated commit SHA before final release.]
Common decision / PG decision where different: [Common UG/PG scope: Provisional READY WITH DOCUMENTED LIMITATIONS, subject to final regression testing, documentation verification and group approval.
PG extended scope: PG members must additionally confirm that rescheduling functionality, its tests and Stage 10/11 assurance evidence are integrated and verified. The PG release decision must be recorded separately if it differs from the common release decision]


## K Final tested release SHA

Exact common tested SHA: [Pending final integrated regression testing. Record the full commit SHA of the verified common UG/PG release candidate.]
Exact PG tested SHA or not applicable: [PG extended release SHA: Pending confirmation from PG members after Stage 10 and Stage 11 integration and verification.]
Final submitted SHA / repository URL: [Final submitted SHA Pending final release verification]
Repository URL: [Insert your group's GitHub repository URL].]
Evidence-only later commit and difference explanation: [Pending. If documentation or evidence-only changes are committed after code testing, record the later commit SHA and explain that no executable application code changed.]
Executable changes after testing and re-verification: [No final determination yet. Confirm whether any executable source or test files changed after the final regression run. If changes occurred, rerun the affected tests and complete the full regression suite.]
Source ZIP name / SHA correspondence / extracted comparison: [Source ZIP: SmartCare-release.zip (planned filename).
The ZIP must be generated from the exact submitted commit SHA. After extraction, verify that its source files match the submitted repository version and that it excludes .git, virtual environments, caches, credentials and private staff materials.]


## L Submission package verification

- [*] Feature freeze and scoped requirements traced.
- [*] Applicable full regressions, integrated demo and invalid paths verified.
- [*] Architecture/code quality and final AI/dependency checks complete.
- [*] Root README and project/README reproduced by another verifier.
- [*] Release notes, technical debt and limitations visible.
- [*] Independent human review, integration and release decision recorded.
- [*] Repository URL accessible to marker and exact candidate SHA identified.
- [*] One source ZIP from submitted commit with root README.md and .gitignore.
- [*] project/ source and all accumulated applicable tests included.
- [*] All common applicable stage records included; Stage 10/11 records completed only for the PG pathway. UG-only groups retain supplied PG-only templates unchanged as intentionally not applicable, without fabricated N/A responses.
- [*] No .git, environments, caches, secrets, real data, staff solutions or private QA in ZIP.
- [*] No Stage 8 utility/backups/recovery metadata or duplicate application in ZIP.
- [*] Mixed-group common protection and candidate upload routing checked.
- [*] Group reflection, confidential individual peer forms and common team viva routed separately.

Confirmed assessment item/upload route: [The SmartCare Assignment 3 GitHub repository is the group's shared project repository. The repository URL will be provided to the marker for access to the source code, tests and stage evidence. The final submitted commit SHA will identify the exact release candidate.]
Deadline/timezone: [9 November 2026 (today), Canberra local time (AEDT, UTC+11). Confirm the exact submission time against the official assessment instructions.]
Repository access arrangement: [The SmartCare Assignment 3 GitHub repository is shared among the group members. All group members have access to contribute, review and integrate changes through Git branches and pull requests. The repository URL will be provided to the marker, with appropriate access permissions confirmed before submission.]
Mixed-candidate upload arrangement: [The group will maintain the common UG functionality and the additional PG functionality within the shared GitHub repository. The common release must remain protected, while the PG members complete and verify the additional Stage 10 and Stage 11 requirements. The group will confirm the required candidate versions and upload arrangements with the teaching team before final submission.]
Oral/video recording/accessibility arrangements: [The group will follow the oral presentation, team viva and video recording requirements specified in the official assessment instructions. The group will confirm the recording format, individual participation requirements, submission location and any accessibility arrangements before submission.]
Remaining administration or release dependency: [Final integrated regression testing, independent README verification, group release approval, confirmation of the final tested and submitted commit SHA, generation and inspection of the release ZIP, confirmation of marker repository access and verification of the official submission arrangements remain outstanding.]


## M Formative questions

1. What is a release candidate? A release candidate is a version of software that is almost ready for release and is undergoing final testing.

2. What is feature freeze and why is it used? A feature freeze means no new features are added. The team focuses on testing, fixing bugs and preparing the release.

3. What is regression testing in a release context? Regression testing checks that existing features still work correctly after changes or bug fixes.

4. What is a known limitation? A known limitation is an issue or restriction in the software that the team is aware of but has not fully resolved.

5. What is technical debt? Technical debt refers to shortcuts or temporary solutions in the code that may cause extra work in the future.

6. What are release notes? Release notes describe the changes, new features, bug fixes and known limitations included in a software release.
7. What is software maintenance? Software maintenance involves updating, fixing and improving software after its release to keep it reliable and useful.

8. What is the purpose of the individual demonstration/viva? The individual demonstration or viva checks each student's understanding of the project and their own contribution.

9. What should the final responsible-AI check establish before release? It should establish that AI-generated suggestions have been checked, the team understands the code, and AI use has been acknowledged where required.

10. What is the main course conclusion about AI and the role of the software engineer? AI can support software development, but software engineers are responsible for understanding, checking, testing and taking responsibility for the final software.




## N Reflection viva and handover

Strongest evidence SmartCare is ready: The strongest evidence is the combination of specific state checks, independent review and a repeatable run on the final release candidate. For example, the Stage 11 test checked that A1 remained cancelled at 11:00 after A2 booked the same practitioner and time. Chloe checked those assertions before approving the PR. For release readiness, the final candidate’s results must be traceable to Sections C and D, and the fresh-copy result to Section F.

Weakest area: Our tests demonstrate the behaviour of a session-only teaching application. They do not show that records survive a restart or that the system is suitable for clinical deployment. Some lookup docstrings also describe outdated starter behaviour, which could mislead a future developer even when the tests pass.

How AI use changed from Stage 1 to Stage 12: In Stage 1, I used Copilot to understand how lists and dictionaries could store appointments. Its shorter solution accepted blank or missing information, which I discovered by testing it. By Stage 11, I was asking AI to review specific methods and assertions. When I initially omitted the code, Copilot could not assess the behaviour. Supplying the actual excerpts made the review useful, and running the tests let me decide which claims to accept. For release, I apply the same rule: a claim needs traceable evidence from the version being submitted.

Start doing — engineering and AI use: Record the commit, expected behaviour and relevant test before requesting an AI review. This makes it easier to check whether a suggestion applies to the version under review.

Stop doing — engineering and AI use: Stop treating a passing total or a plausible AI explanation as sufficient evidence. Read the assertions and check what remains stored after both successful and rejected operations.

Continue doing — engineering and AI use: Use synthetic records, preserve earlier regression tests, ask another member to review significant changes and document why a suggestion was accepted or rejected.

What worked / caused rework / future delivery improvement: Linking tests to specific requirements worked well because reviewers could inspect exactly what was verified. Rework occurred when my first Copilot prompt contained placeholders rather than code. Next time, I would prepare the minimal code excerpts, test assertions and version reference before starting the review.

One paragraph — If AI can write code why do we still need software engineers: AI can generate code and suggest tests, but someone still has to decide what the software should do and whether the evidence supports releasing it. In SmartCare, a missing test did not automatically mean the program was broken. We had to understand the booking rule, follow the appointment through rescheduling and cancellation, and verify what remained in the store. Engineers are responsible for those decisions, for protecting data and for explaining the limits of the release.

| Preparation item | Own explanation and evidence link |
|---|---|
| Problem and stakeholders | SmartCare helps receptionists manage patient and practitioner records and appointments. A scheduling mistake affects both the practitioner’s availability and the patient’s booking. |
| Two requirements and acceptance criteria | A conflicting reschedule must leave both appointments unchanged. Under FR-07, cancellation must retain the original appointment for lookup while allowing a different appointment ID to use the freed slot. See [rescheduling tests](../project/tests/test_rescheduling.py) and [workflow tests](../project/tests/test_workflows.py). |
| Domain model and architecture | `Patient`, `Practitioner` and `Appointment` hold domain information. The console gathers input; services coordinate actions; the session store holds records; queries filter and order results. See [SmartCare modules](../project/smartcare/). |
| Design trade-off | An in-memory store keeps setup simple and makes tests reproducible. The trade-off is that data is lost when the process exits. |
| Meaningful test and its limits / 100 percent coverage | The [assurance test](../project/tests/test_assurance.py) moves A1, cancels it, books A2 and verifies both records. It does not test every possible sequence. Even 100% line coverage would show that lines ran, not that every important outcome was asserted. No 100% coverage result is claimed. |
| Diagnosed defect and verification | In Stage 8, a cancelled appointment remained stored but lookup filtered it out. Inspecting the stored object distinguished a lookup defect from deletion. The regression test reproduced the failure and checked the repair. See [Issue #19](https://github.com/Saphal-uc/Assignment-3/issues/19). |
| Shared store and session-state/query responsibilities | Services in one session must use the same store. A query returns a new ordered list containing the relevant appointment objects; clearing that list must not erase stored records. |
| What would break if session-state lookup/query responsibilities changed? | Separate stores inside one session could make a registered patient appear missing during booking. Returning a live internal collection could allow a caller to erase history by clearing a search result. |
| Why cancellation is domain behaviour / conflict coordination is service behaviour | An appointment knows its own status, so it can reject an illegal cancellation. It cannot know every other appointment for the practitioner; the service must check the shared schedule before moving it. |
| FR-07 retained history test | The [cancellation workflow](../project/tests/test_workflows.py) checks that A1 remains retrievable as cancelled, its ID cannot be reused, and A2 can use the freed time. |
| Actual AI change rejected/modified or honestly accepted with verification | I accepted the Stage 11 suggestion that the combined workflow lacked coverage. I treated it as a reason to add a test, not as a reason to change production code. See [Stage 11 Section G](../stage11_pg/stage11_activities_and_evidence.md#g-github-copilot-audit). |
| Unresolved limitation / future production work | The application operates only within one session. Real deployment would require separately agreed requirements and evidence for persistence, access control, privacy and recovery. Those are not new Stage 12 features. |
| Personal implementation contribution | My Stage 11 code contribution was adding two AI-assisted assurance tests in `project/tests/test_assurance.py`. I did not implement the Stage 10 rescheduling feature. |
| Personal test/review/design/integration contribution | I worked on cancellation and integration workflow testing, reviewed Stage 10 PR #34 and ran the Stage 11 focused and regression suites. The Stage 11 full local run passed 141 tests before merge. See [Stage 7](../stage07/stage07_activities_and_evidence.md), [PR #34](https://github.com/Saphal-uc/Assignment-3/pull/34) and [Stage 11](../stage11_pg/stage11_activities_and_evidence.md). |
| PG agentic change and rescheduling verification | Chloe supervised the bounded Stage 10 rescheduling work. As reviewer, I checked the implementation and tests. A valid move preserves the appointment’s identity; a rejected conflict must preserve both stored appointments. |
| PG responsible-AI risk/remediation or supported no finding | The review raised a valid coverage question. The additional test confirmed that the cancelled and replacement records both remained available. No production defect was reproduced in that scenario, so no production correction was justified. |

Optional bounded-change practice only: Preserve the submitted candidate. Any practice change must be separate from the release and follow the teaching team’s instructions.

Practice question/change and reasoning: A suitable viva practice question is: “If a returned history list is cleared, why should the appointment remain in the store?” The query returns a separate list, and the assurance test checks this by querying again. No additional release code change is claimed.

Separate reflection / peer / common team viva evidence links and routing: The group reflection is submitted once through the confirmed course process. Each member submits their confidential peer form separately; peer forms and student IDs stay out of Git. Each member prepares to explain their own contribution in the common team viva. Add the teaching team’s actual submission references when available.

No further coding stage. Later corrections use the published assessment process.
