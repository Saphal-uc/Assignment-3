# Stage 12 activities and evidence

BLANK student response template. Supplied from the beginning in stage12/ in your EXISTING repository; complete it only when you reach Stage 12 after the previous applicable stage is integrated, verified and recorded; preserve project/, tests, earlier records and Git history. UG/common and PG/extended scope must be explicit. Use concise results and versioned links, not copied logs or source. No staff answers or fabricated approvals.

Group/tutorial: [response]
Members and UG/PG applicability: [response]


## A Release scope and starting SHA

Release label/version and requirements baseline: [response]
Common starting SHA / branch / applicable members: [response]
PG starting SHA / branch / applicable members or not applicable: [response]
Working-state review and approved integration: [response]
Protected common candidate and PG differences: [response]
Feature freeze / owner / verifier: [response]


## B Requirements and release readiness matrix

Tutorial activity 1: All tests pass, README setup is incomplete, one dependency is unreviewed and a known limitation is undocumented. Decide Release / Release with conditions / Do not release and justify: [response]

Tutorial activity 2 and actual readiness matrix. Add exact requirement/acceptance IDs, evidence and reviewer; distinguish common/PG applicability.

| Release claim / requirement / scope | Evidence | Location/link and SHA | Reviewer | Sufficient? | Gap/action |
|---|---|---|---|---|---|
| Cancellation history works | [response] | [response] | [response] | [response] | [response] |
| Architecture responsibilities are appropriate | [response] | [response] | [response] | [response] | [response] |
| Rescheduling is safe — PG only | [response] | [response] | [response] | [response] | [response] |
| AI use is responsible — common recheck / PG assurance | [response] | [response] | [response] | [response] | [response] |
| System is maintainable | [response] | [response] | [response] | [response] | [response] |
| FR-01–03 register/find and validation | [response] | [response] | [response] | [response] | [response] |
| FR-04–05 booking/conflict rules | [response] | [response] | [response] | [response] | [response] |
| FR-06–08 cancellation/history/find | [response] | [response] | [response] | [response] | [response] |
| FR-09 and QRY/FP listing/filter/order/purity | [response] | [response] | [response] | [response] | [response] |
| UI full console sequence and error recovery | [response] | [response] | [response] | [response] | [response] |
| Session-only scope / FR-10 retired | [response] | [response] | [response] | [response] | [response] |
| PG RES and assurance integration | [response] | [response] | [response] | [response] | [response] |


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

| README item | Location | Verifier | Result/gap |
|---|---|---|---|
| Purpose and included common/PG scope | [response] | [response] | [response] |
| Out-of-scope capabilities and known limitations | [response] | [response] | [response] |
| Confirmed teaching Python version and dependency installation | [response] | [response] | [response] |
| Working directory / demo / interactive / test commands | [response] | [response] | [response] |
| Repository structure and architecture responsibilities | [response] | [response] | [response] |
| Responsible AI summary / synthetic-data rule | [response] | [response] | [response] |
| Release label/version and SHA links | [response] | [response] | [response] |
Root README index and project/README verified: [response]
Fresh clone or extracted ZIP / candidate identity: [response]
Verifier and clean environment / actual version: [response]
Setup/run/test commands and observed results: [response]
Missing local file or setup gap / remedy and recheck: [response]


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

Issue / PR / diff links and reviewed SHA: [response]
Independent reviewer / feedback / response: [response]
Integration commit / full recheck: [response]
Tracked and untracked file inspection / cleanliness: [response]
Secrets/staff material/caches/tool-metadata exclusion check: [response]
Candidate recovery plan / known-good SHA: [response]
Named substantive contributions: [response]


## J Human release decision

Decision — READY FOR COURSE RELEASE / READY WITH DOCUMENTED LIMITATIONS / NOT YET READY: [response]
Approver / date / rationale and evidence: [response]
What risks remain / conditions / owners: [response]
Can the team explain the system: [response]
Can a change be recovered: [response]
Common decision / PG decision where different: [response]


## K Final tested release SHA

Exact common tested SHA: [response]
Exact PG tested SHA or not applicable: [response]
Final submitted SHA / repository URL: [response]
Evidence-only later commit and difference explanation: [response]
Executable changes after testing and re-verification: [response]
Source ZIP name / SHA correspondence / extracted comparison: [response]


## L Submission package verification

- [ ] Feature freeze and scoped requirements traced.
- [ ] Applicable full regressions, integrated demo and invalid paths verified.
- [ ] Architecture/code quality and final AI/dependency checks complete.
- [ ] Root README and project/README reproduced by another verifier.
- [ ] Release notes, technical debt and limitations visible.
- [ ] Independent human review, integration and release decision recorded.
- [ ] Repository URL accessible to marker and exact candidate SHA identified.
- [ ] One source ZIP from submitted commit with root README.md and .gitignore.
- [ ] project/ source and all accumulated applicable tests included.
- [ ] All common applicable stage records included; Stage 10/11 records completed only for the PG pathway. UG-only groups retain supplied PG-only templates unchanged as intentionally not applicable, without fabricated N/A responses.
- [ ] No .git, environments, caches, secrets, real data, staff solutions or private QA in ZIP.
- [ ] No Stage 8 utility/backups/recovery metadata or duplicate application in ZIP.
- [ ] Mixed-group common protection and candidate upload routing checked.
- [ ] Group reflection, confidential individual peer forms and common team viva routed separately.

Confirmed assessment item/upload route: [response]
Deadline/timezone: [response]
Repository access arrangement: [response]
Mixed-candidate upload arrangement: [response]
Oral/video recording/accessibility arrangements: [response]
Remaining administration or release dependency: [response]


## M Formative questions

1. What is a release candidate? [response]

2. What is feature freeze and why is it used? [response]

3. What is regression testing in a release context? [response]

4. What is a known limitation? [response]

5. What is technical debt? [response]

6. What are release notes? [response]

7. What is software maintenance? [response]

8. What is the purpose of the individual demonstration/viva? [response]

9. What should the final responsible-AI check establish before release? [response]

10. What is the main course conclusion about AI and the role of the software engineer? [response]




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
