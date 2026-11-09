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
| Complete common | Python 3.14.6; pytest 8.3.5 | `project/`; `python -m pytest -q tests/test_starter.py tests/test_domain.py tests/test_services.py tests/test_regressions.py tests/test_queries.py tests/test_workflows.py` | `7e349978947726dd44a49fa50a167b097459ccba` | 106 passed in 0.03s; 0 failed | https://github.com/Saphal-uc/Assignment-3/issues/42|
| Complete PG | Python 3.14.6; pytest 8.3.5 | `project/`; `python -m pytest -q tests/test_rescheduling.py tests/test_assurance.py` | `7e349978947726dd44a49fa50a167b097459ccba` | 35 passed in 0.01s; 0 failed | https://github.com/Saphal-uc/Assignment-3/issues/42 |
| Affected focused checks after correction | None | No Stage 12 code corrections made | None | No correction-specific retest needed | None |
| Full integrated recheck | Python 3.14.6; pytest 8.3.5 | `project/`; `python -m pytest -q` | `7e349978947726dd44a49fa50a167b097459ccba` | 141 passed in 0.03s; 0 failed | https://github.com/Saphal-uc/Assignment-3/issues/42|
Prior assertions preserved / reviewed test diff: Git history shows that tests were added from Stages 7–11. The project still includes the eight original tests and the tests added in later stages. No uncommitted changes were found in the test files. All 141 tests passed.
Remaining failure / limitation: All 141 tests passed with no failures. The tests cover the required features, but they cannot guarantee that the system is completely free of bugs. SmartCare only stores data during the current session and is not designed for real healthcare use.


## D Console and end to end demonstration

| Demo step | Synthetic setup/input | Expected requirement | Observed result | Evidence/link |
|---|---|---|---|--|
| Problem and stakeholders | SmartCare is an appointment system for clinic staff, patients and practitioners. | Support basic appointment management. | The console provides registration, lookup, booking, cancellation and appointment listing. | https://github.com/Saphal-uc/Assignment-3/issues/42 |
| Register and find Patient and two Practitioners | Register patient `p1` (Alex Example), practitioner `dr1` (Dr Smith, gp) and `dr2` (Dr Lee, gp). Find `p1` and `dr1`. | Register and find patients and practitioners. | All three records were registered successfully. Patient and practitioner lookups worked. |https://github.com/Saphal-uc/Assignment-3/issues/42 |
| Valid booking | Book `a1` for `p1` with `dr1` at `2026-12-01 09:00`. | Create a scheduled appointment. | Appointment `a1` was created with status `scheduled`. | https://github.com/Saphal-uc/Assignment-3/issues/42 |
| Same-practitioner exact-time conflict rejected | Try to book `a2` with `dr1` at the same time as `a1`. | Prevent double booking for the same practitioner. | The system rejected the booking because `dr1` already had a scheduled appointment at that time. | https://github.com/Saphal-uc/Assignment-3/issues/42 |
| Different practitioner at the same time | Book `a2` with `dr2` at `2026-12-01 09:00`. | Allow different practitioners to have appointments at the same time. | Appointment `a2` was created successfully. | https://github.com/Saphal-uc/Assignment-3/issues/42 |
| Cancellation and retained history | Cancel `a1`, then find it using appointment lookup. | Change the status to cancelled and keep the appointment record. | `a1` changed to `cancelled` and could still be found. | https://github.com/Saphal-uc/Assignment-3/issues/42 |
| Repeated cancellation rejected | Try to cancel `a1` again. | Reject cancellation of an appointment that is not scheduled. | The system displayed `Only SCHEDULED appointments may be cancelled`. | https://github.com/Saphal-uc/Assignment-3/issues/42 |
| All-status listing | List appointments for `dr1` and `dr2` with a blank status filter. | Display appointments of all statuses. | `dr1` showed cancelled `a1`. `dr2` showed scheduled `a2`. | https://github.com/Saphal-uc/Assignment-3/issues/42|
| Filtering, empty result and unknown practitioner | Filter `dr1` by `scheduled` and `cancelled`. Search for unknown practitioner `d1`. | Return matching appointments, handle empty results and reject unknown practitioners. | The scheduled filter returned no appointments. The cancelled filter returned `a1`. The unknown practitioner was rejected. |https://github.com/Saphal-uc/Assignment-3/issues/42 |
| Appointment ordering | Create `a3` for `dr2` at `2026-11-30 10:00`, then list all appointments for `dr2`. | Sort appointments by date and time. | The system displayed `a3` before `a2`, even though `a3` was created later. | https://github.com/Saphal-uc/Assignment-3/issues/42 |
| Invalid input and recovery | Enter invalid date `2026-13-01 09:00`, status `invalid` and menu option `99`. | Reject invalid inputs and continue running. | The system displayed error messages and returned to the main menu. | https://github.com/Saphal-uc/Assignment-3/issues/42|
| Session-only data and exit | Start the interactive console and select `0` to exit. | Explain temporary data storage and allow normal exit. | The console displayed a session-only warning. Option `0` was selected to exit. | https://github.com/Saphal-uc/Assignment-3/issues/42 |
| Requirement-linked pytest | Run `test_reschedule_preserves_identity_updates_lookup_listing_and_releases_old_slot`. | Verify appointment identity, updated time, lookup, listing and old-slot reuse. | The test passed and checked these requirements. | https://github.com/Saphal-uc/Assignment-3/issues/42 |
| Architecture, AI decision and limitation | Stage 10 used GitHub Copilot to add rescheduling in `domain.py` and `services.py`, with tests in `test_rescheduling.py`. | Keep the existing architecture and review AI-generated changes. | The team reviewed and accepted the changes in PR #34. A database redesign was rejected as unnecessary. The system still uses an in-memory DataStore. It does not check past dates, appointment duration or clinic opening hours. | https://github.com/Saphal-uc/Assignment-3/issues/33 |
| PG rescheduling identity and no-op | Run `python -m pytest -v tests/test_rescheduling.py`. | Keep appointment identity and participants, update the time and allow same-time rescheduling. | All relevant tests passed. The complete rescheduling suite returned 33 passed. | https://github.com/Saphal-uc/Assignment-3/issues/42|
| PG conflict, invalid status and unchanged state | Test time conflicts, invalid dates and cancelled or completed appointments. | Reject invalid rescheduling without changing the original appointment. | The tests passed. Invalid operations were rejected and appointment data stayed unchanged. | https://github.com/Saphal-uc/Assignment-3/issues/42 |
| PG old-slot reuse, lookup, sorting and assurance | Run rescheduling and assurance tests. | Release the old slot, update lookup and listing, keep history and separate session data. | All 33 rescheduling tests and 2 assurance tests passed. | https://github.com/Saphal-uc/Assignment-3/issues/42 |

**Stable demo owner / fresh process / command:**

Hong Ruan ran the interactive console from the `project/` directory using `python main.py --interactive`.

The demonstration used synthetic data in a fresh process. The complete console validation process was recorded, including successful operations, invalid inputs and error messages.

**PG demonstrations through service/tests or not applicable:**

PG rescheduling was demonstrated through service-level pytest tests because the interactive console does not include a rescheduling option.

- `python -m pytest -v tests/test_rescheduling.py` — 33 passed, 0 failed.
- `python -m pytest -v tests/test_assurance.py` — 2 passed, 0 failed.

The tests covered successful rescheduling, time conflicts, invalid inputs, unchanged state after failure, old-slot reuse, lookup, sorting, session isolation and retained appointment history.

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

Delivered features: 

SmartCare can register and find patients and practitioners. It can book, cancel, find and list appointments. It also checks booking conflicts and handles invalid inputs.
The PG version supports appointment rescheduling.

Important fixes: We fixed the appointment capacity bug in Stage 8. We also added tests to check that the existing features still work. No new bugs were found during our Stage 12 tests.
Architecture/quality improvements: The code is separated into Domain, Service, DataStore, Query and Console modules. This makes the code easier to understand and test. We added more tests during the project. All 141 tests passed in Stage 12.
Known limitations: SmartCare only saves data during the current session. All data is lost when the program exits. The system does not check past appointment dates, appointment duration or clinic opening hours. It only uses minute-level appointment times. It is a student project, not a real healthcare system. It does not include user login, notifications, billing or a database.
AI-assisted development note: We used GitHub Copilot to help develop the PG rescheduling feature in Stage 10. We reviewed the AI plan, code and tests before accepting the changes. We also rejected unnecessary database changes. In Stage 11, our team reviewed the PG features and added assurance tests to check their reliability. All AI-assisted changes were checked by team members and tested before release.


| Debt item | Impact | Priority | Future action | Accepted? / release rationale |
|---|---|---|---|---|
| No database | Data is lost after exit | Low | Add persistent storage | Yes, outside assignment scope |
| No user login | No access control | Low | Add authentication | Yes, outside assignment scope |
| No clinic hours check | Bookings may be outside clinic hours | Low | Add working-hour checks | Yes, not required |
| No notifications | Users do not receive reminders | Low | Add notifications | Yes, not required |
| Limited production checks | Not ready for real healthcare use | Low | Add security and reliability checks | Yes, student project only |

Session-only synthetic data and minute-precision local time: SmartCare uses synthetic data for testing. Data is only stored during the current session and is lost when the program exits. Appointment times use local date and time with minute precision.
Production auth/roles, portal, notifications, billing/insurance, clinical AI exclusions: SmartCare does not include user login, role-based access, an online portal, notifications, billing, insurance or clinical AI. These features are outside the assignment scope.
Scale/concurrency, timezone policy, operations/monitoring, accessibility/usability limitations: SmartCare is designed for a small demonstration. It has not been tested for many users at the same time. It does not support different timezones or production monitoring. Accessibility and usability testing is also limited.
Difference between accepted scope limit and unresolved required behaviour: Accepted scope limits are features that the assignment does not require, such as a database or user login. Unresolved required behaviour means a required feature is still not working. All 141 tests passed, and no unresolved required behaviour was found during our Stage 12 checks.
PG assurance residual risks / owner / status or not applicable: Some risks remain, such as invalid real-world booking times and limited production security. These are outside the assignment scope. The PG assurance tests passed (2/2). No new PG assurance failures were found. Owner: PG team. Status: Accepted for assignment release.


## H Release findings and corrective action

| Requirement/claim | Reproduction/observation | Impact/severity | Owner/action | Corrective diff | Focused/full recheck | Residual limit |
|---|---|---|---|---|---|---|
| Common features work correctly | 106 common tests passed. Console registration, booking, cancellation, lookup and listing worked. | No issue found | Hong Ruan / verified | None | 106 common tests passed; 141 full tests passed | Tests do not cover every possible case |
| PG rescheduling works correctly | 33 rescheduling tests passed. Valid and invalid rescheduling cases were checked. | No issue found | Hong Ruan / verified | None | 33 rescheduling tests passed; 141 full tests passed | Rescheduling does not check clinic hours or past dates |
| PG assurance requirements | 2 assurance tests passed, including session isolation and retained appointment history. | No issue found | PG team / verified | None | 2 assurance tests passed; 141 full tests passed | Data is only stored during the current session |
| Console error handling | Invalid dates, status filters, menu options and practitioner IDs were rejected. The console continued running. | No issue found | Hong Ruan / verified | None | Console demonstration completed; 141 full tests passed | Console only supports the required basic features |
| Test environment | Python 3.14.6 and pytest 8.3.5 were used. All 141 tests passed. | No issue found | Hong Ruan / verified | None | `python -m pytest -q` — 141 passed | Other environments were not tested |

Justified no-change conclusion if no defect found: All 141 tests passed, and the Console demonstration worked. No new defects were found during our Stage 12 checks. Therefore, no code changes were needed.
Release blockers still open / status: No functional release blockers were found in our tests. Final documentation, Git review and release packaging are handled by the other team members.


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
