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

| Review area | Code/evidence location | Finding or no finding | Correction/no change and recheck |
|---|---|---|---|
| OOP responsibilities and pure-query boundaries | [response] | [response] | [response] |
| PascalCase and snake_case naming | [response] | [response] | [response] |
| Useful type hints and meaningful docstrings | [response] | [response] | [response] |
| Four-space indentation and imports/layout | [response] | [response] | [response] |
| Focused methods / duplication / dead or commented code | [response] | [response] | [response] |
| Globals / leakage / unnecessary inheritance or frameworks | [response] | [response] | [response] |
| No SQLite/persistence/repository ABCs/speculative features | [response] | [response] | [response] |
| Synthetic data / secrets / dependencies / provenance | [response] | [response] | [response] |
| Significant common Copilot contributions and human verification | [response] | [response] | [response] |
| PG plan/diff/test approvals and Stage 11 VERIFY/TRUST | [response] | [response] | [response] |

| AI claim | Affected requirement/code | Human check | Accept/Modify/Reject and reason | Actual outcome/action or no change |
|---|---|---|---|---|
| [response] | [response] | [response] | [response] | [response] |
Access route or approved equivalent / limitations: [response]
Available AI evidence and missing evidence honestly disclosed: [response]


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

Strongest evidence SmartCare is ready: [response]
Weakest area: [response]
How AI use changed from Stage 1 to Stage 12: [response]
Start doing — engineering and AI use: [response]
Stop doing — engineering and AI use: [response]
Continue doing — engineering and AI use: [response]
What worked / caused rework / future delivery improvement: [response]
One paragraph — If AI can write code why do we still need software engineers: [response]

| Preparation item | Own explanation and evidence link |
|---|---|
| Problem and stakeholders | [response] |
| Two requirements and acceptance criteria | [response] |
| Domain model and architecture | [response] |
| Design trade-off | [response] |
| Meaningful test and its limits / 100 percent coverage | [response] |
| Diagnosed defect and verification | [response] |
| Shared store and session-state/query responsibilities | [response] |
| What would break if session-state lookup/query responsibilities changed? | [response] |
| Why cancellation is domain behaviour / conflict coordination is service behaviour | [response] |
| FR-07 retained history test | [response] |
| Actual AI change rejected/modified or honestly accepted with verification | [response] |
| Unresolved limitation / future production work | [response] |
| Personal implementation contribution | [response] |
| Personal test/review/design/integration contribution | [response] |
| PG agentic change and rescheduling verification | [response] |
| PG responsible-AI risk/remediation or supported no finding | [response] |

Optional bounded-change practice only: validation rule, focused test, safe error-message change, explicit-input query or agreed status rule with test. Explain expected impact before editing, make a small change, run the test, and identify evidence to inspect if unsure. No live AI unless explicitly permitted. Preserve the submitted candidate.

Practice question/change and reasoning: [response or not undertaken]
Separate reflection / peer / common team viva evidence links and routing: [response]
No further coding stage. Later corrections use the published assessment process.
