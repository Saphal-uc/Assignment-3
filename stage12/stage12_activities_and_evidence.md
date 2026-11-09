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
