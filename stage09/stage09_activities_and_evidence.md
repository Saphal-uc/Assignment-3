# Stage 9 activities and evidence

Common UG and PG record. All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in `stage09/` in the existing repository. Preserve `project/`, all earlier tests, records and responses.

**Group:** Group 4, Thursday 2:30.

**Members and responsibilities:**

- `UjwalBk1998`: appointment query implementation and query tests.
- `u3330161`: practitioner appointment listing service and service tests.
- Chloe (`realllchloe`): interactive console implementation and review.
- Saphal Bhattarai (`Saphal-uc`): integrated workflow and regression tests.

**Stage 8 integrated baseline:**

- SHA: `75fa1c9c55555438f6703e284747bdeff709be96`
- Working directory: `project/`
- Command: `python -m pytest -q`
- Result before Stage 9 work: 75 tests passed.

## A. Tutorial activities

### A1 Session state classification

| Information | Required session/domain or transient state? | Requirement or reason |
|---|---|---|
| Patient identity | Required session/domain state | Patient ID and name are needed for registration, lookup and appointment booking. |
| Appointment history | Required session/domain state | Cancelled appointments must remain retrievable and listable during the session. |
| Temporary menu choice | Transient state | The choice is used only to select the current console operation. |
| Practitioner specialty | Required session/domain state | Specialty belongs to the registered practitioner record. |
| Debug print output | Transient state | Printed diagnostic information is not part of the domain model. |
| Appointment status | Required session/domain state | Status determines whether an appointment is scheduled, cancelled or completed. |

**What is intentionally lost on exit?**

SmartCare uses an in-memory data store. Patient, practitioner and appointment records are therefore lost when the program exits. Menu choices, entered text and printed output are also temporary. No database or restart persistence is required.

### A2 Interface and domain data plan

The following design describes the Stage 9 interfaces. The original pre-AI worksheet was not committed, so this table reconstructs the implemented contracts from the approved code and tests.

| Function or component | Explicit inputs and types | Outputs | Responsibility and validation | Domain source / existing constraint |
|---|---|---|---|---|
| `appointment_sort_key` | One `Appointment` | `tuple[datetime, str]` | Reads the appointment date/time and ID to create a deterministic sorting key. | Uses the existing `Appointment.date_time` and `appointment_id` properties. |
| `select_appointments` | `list[Appointment]`, practitioner ID and optional `AppointmentStatus` | New sorted `list[Appointment]` | Filters by practitioner and optional status, then sorts without modifying the source list or appointment objects. | Uses actual practitioner objects and the existing status enum. |
| Service listing | Practitioner ID and optional `AppointmentStatus` | New ordered appointment list | Confirms that the practitioner exists, validates the status and delegates filtering and sorting to the query function. | Unknown practitioners raise `LookupError`; blank IDs and invalid statuses raise `ValueError`. |
| Console | Menu choice and text entered by the user | Printed result or recoverable error | Parses input, calls the appropriate service and displays results. | Accepts date/time as `YYYY-MM-DD HH:MM` and status as scheduled, cancelled, completed or blank. |

Patient ID, name, practitioner ID, name and specialty come from the registered `Patient` and `Practitioner` objects. Appointment ID, actual participant objects, date/time and status come from the existing `Appointment` object. Stage 9 reuses these contracts rather than creating duplicate dictionaries or database records.

### A3 Responsibility violations

| Conceptual case | Violation | Correct boundary and reason |
|---|---|---|
| `Appointment.cancel` reads input | The domain object would depend on console interaction. | The console reads the appointment ID, the service finds the record and the domain object enforces the cancellation transition. |
| Service prints or reads the menu | It mixes use-case coordination with presentation. | `console.py` handles input and output. Services coordinate domain and store operations. |
| Query sorts its source in place | It changes caller-owned collection state. | `select_appointments` uses `sorted()` and returns a new list. |
| Store prints “Appointment saved” | Persistence and presentation responsibilities become mixed. | The store saves the object. The console decides what confirmation to display. |

### A4 Sorting comparison

`appointments.sort(key=appointment_sort_key)` changes the original list and returns `None`.  
`result = sorted(appointments, key=appointment_sort_key)` leaves the original list unchanged and returns a different list object.

Both lists may contain references to the same `Appointment` objects. A meaningful mutation check records the original list order, object identities and appointment fields before the query, then verifies that they remain unchanged afterward. It also verifies that the returned list is not the source list.

For example, if A2 is at 10:00, A1 is at 09:00 and A0 is also at 09:00, the result is A0, A1 and A2. Date/time is the primary key and appointment ID breaks equal-time ties. The function itself is passed as `key=appointment_sort_key`; Python calls it for each appointment.

### A5 Exit question

Cancellation changes an appointment’s status to `CANCELLED`; it does not delete the record. The cancelled appointment remains available through appointment lookup and an all-status practitioner listing. A `SCHEDULED` filter excludes it because its status no longer matches. Its old practitioner time slot can be reused with a new appointment ID because conflict checking considers scheduled appointments only.

## B. Human design and contracts

The table below records the final Stage 9 contracts. It was reconstructed from the implementation, tests, issues and pull requests because the original human-design worksheet was not committed before the Copilot review.

| Requirement | Input/session data | Operation and responsible component | Expected result or error | Test/evidence |
|---|---|---|---|---|
| QRY-01 | One appointment | `appointment_sort_key` returns date/time and appointment ID. | A deterministic tuple is returned. | `test_appointment_sort_key` |
| QRY-02 | Appointment list and practitioner ID | `select_appointments` selects appointments belonging to that practitioner. | Other practitioners are excluded. | `test_select_appointments_filters_by_practitioner` |
| QRY-03 | Optional `AppointmentStatus` | Query includes every status when omitted or only the selected status when supplied. | Correct filtered new list. | Status tests in `test_queries.py` |
| QRY-04 | Practitioner ID and optional status | `AppointmentService.list_practitioner_appointments` validates inputs and delegates to the query. | Sorted list, empty list, `LookupError` or `ValueError` as appropriate. | Listing tests in `test_services.py` |
| FP-01 | Source appointment collection | Query reads the source without changing its order or fields. | Source remains unchanged. | `test_select_appointments_does_not_change_source_list` |
| FP-02 | Empty, sorted or unsorted source | Query always returns a new list. | Result is not the source list. | New-list, repeated-call and already-sorted tests |
| FP-03 | Equal date/time appointments | Named key sorts by date/time and then ID. | Stable deterministic order. | Tie-break test |
| UI-01 | Menu choice from 0–8 | `run_menu` routes the operation to the correct helper and service. | Operation completes or the user exits. | Issue #26 and PR #27 |
| UI-02 | Invalid choice, ID, status or date/time | Console catches expected `ValueError` and `LookupError`. | Error is displayed and the menu continues. | Issue #26 and PR #27; no saved full transcript |
| FR-01–02 | Patient and practitioner details | Registration and lookup services use the shared store. | Actual registered object is returned; invalid or unknown IDs are rejected. | Service and starter tests |
| FR-03–04 | Appointment ID, participant IDs and date/time | Booking service finds registered participants and creates the appointment. | Scheduled appointment is stored. | Starter and workflow tests |
| FR-05–07 | Existing appointment ID | Lookup and cancellation use the same stored appointment object. | Cancellation changes status while retaining history. | Cancellation service and workflow tests |
| FR-08–09 | Practitioner and date/time | Store checks scheduled appointment conflicts before insertion. | Conflict is rejected without modifying existing state. | Workflow conflict test |

A blank or non-string ID raises `ValueError`. A valid but unknown ID raises `LookupError` at the service layer. An invalid status value raises `ValueError`. The console converts approved status text into `AppointmentStatus`. Lookup and listing reuse the actual stored objects. Rejected operations are checked against before-and-after state to confirm that existing records remain unchanged.

## C. Implementation and query verification

| Requirement/test ID | Code location | Case and meaningful assertion | Actual result | Evidence |
|---|---|---|---|---|
| QRY-01 | `project/smartcare/queries.py` | Sort key equals `(appointment.date_time, appointment.appointment_id)`. | Passed. | [Query tests](../project/tests/test_queries.py) |
| QRY-02 | `select_appointments` | Only appointments for the requested practitioner are returned. | Passed. | [Query tests](../project/tests/test_queries.py) |
| QRY-03 | `select_appointments` | Omitted status includes scheduled, cancelled and completed records; explicit status filters correctly. | Passed. | [Query tests](../project/tests/test_queries.py) |
| FP-01 | `select_appointments` | Original order and appointment fields are recorded and compared after the query. | Passed. | [Query tests](../project/tests/test_queries.py) |
| FP-02 | `select_appointments` | Empty, repeated and already-sorted calls return new list objects. | Passed. | [Query tests](../project/tests/test_queries.py) |
| FP-03 | `appointment_sort_key` | Equal date/time appointments are ordered by appointment ID. | Passed. | [Query tests](../project/tests/test_queries.py) |
| QRY-04 | `AppointmentService.list_practitioner_appointments` | All-status and each enum-status listing return correct sorted results. | Passed. | [Service tests](../project/tests/test_services.py) |
| QRY-04 errors | `AppointmentService.list_practitioner_appointments` | Unknown practitioner raises `LookupError`; blank ID and invalid status raise `ValueError`. | Passed. | [Service tests](../project/tests/test_services.py) |
| Retained history | Service and store | Cancelled record remains returned by all-status listing while the scheduled filter excludes it. | Passed. | [Workflow tests](../project/tests/test_workflows.py) |

`select_appointments` is pure with respect to the supplied collection. It has explicit inputs, uses no global store, performs no input/output and returns `sorted(selected, key=appointment_sort_key)`. It creates a new list while safely reusing the stored appointment objects. Tests verify that source order and appointment fields are unchanged.

The tests establish filtering, ordering, fresh-list behaviour, repeated-call consistency, service validation and state preservation for the tested examples. They do not prove permanent persistence, thread safety, authorisation or behaviour for every possible value. Those features are outside the Stage 9 requirements.

Repository review evidence records:

- PR #31 final query review: 16 query tests and 94 total tests passed.
- PR #30 service review: 37 service tests and 106 total tests passed.

## D. Integrated console and workflow evidence

| Scenario/acceptance ID | Reproducible inputs/artefact | Expected result | Observed result and state check | Evidence |
|---|---|---|---|---|
| UI-01 menu workflow | Run `python main.py --interactive` and use options 1–7 for registration, lookup, booking, cancellation and retrieval. | Each choice calls the correct shared-session service. | PR #27 records manual testing of options 1–7. Option 8 was implemented, but its final manual demonstration was not recorded in the PR. | [PR #27](https://github.com/Saphal-uc/Assignment-3/pull/27) |
| UI-02 invalid-input recovery | Enter an unknown menu choice, invalid ID, impossible date/time, conflict or invalid status. | Display an error without ending the session or changing valid records. | PR #27 records booking-conflict and error-recovery checks. A complete input/output transcript was not committed. | [Issue #26](https://github.com/Saphal-uc/Assignment-3/issues/26) |
| Automated workflow — booking conflict | Book A1 for P1 with D1 at 09:00. Try A2 with D1 at the same time, then retry A2 with D2. | Reject the conflict, keep A1 unchanged and allow the retry with D2. | Passed. The conflict raised `ValueError`. A1 kept its original patient, practitioner, time and scheduled status. A2 was not stored until the successful retry. | [Workflow tests](../project/tests/test_workflows.py) |
| Automated workflow — cancellation and history | Cancel A1, try to reuse ID A1, then book A2 with the same practitioner at the freed time. | Keep A1 as cancelled, reject reuse of its ID and allow A2 to use the slot. | Passed. Lookup returned the same cancelled A1. Reusing its ID raised `ValueError`. A2 was scheduled and both records remained stored. | [Workflow tests](../project/tests/test_workflows.py) |
| Automated workflow — unknown patient and retry | Register D1. Try to book A1 for unknown P1. Register P1 and retry with the same appointment details. | First attempt raises `LookupError` and stores nothing; retry succeeds. | Passed. The appointment list stayed empty after rejection. After registration, A1 was scheduled with the correct objects and time. | [Workflow tests](../project/tests/test_workflows.py) |

**Recorded workflow test evidence:**

- Working directory: `project/`
- Focused command: `python -m pytest -v tests/test_workflows.py`
- Result: 3 passed.
- Full suite at PR #25: 78 passed.
- Final service review at PR #30: 106 passed.

## E. GitHub Copilot review and human decisions

**Human design before AI:** The implementation used the supplied Stage 9 contracts and existing domain design. However, the completed pre-AI worksheet was not committed, so the repository does not independently prove its completion.

**Actual prompt/context supplied:** The exact Copilot prompt was not stored. PR #31 records that Copilot was asked to review the Stage 9 appointment query implementation and tests.

**Actual response available:** The reviewer recorded that Copilot found no implementation problem but suggested tests for repeated calls and already-sorted input. The complete Copilot transcript is not available.

| AI finding | Code/test evidence | Severity | Decision and reason | Change or no change | Actual verification |
|---|---|---|---|---|---|
| Add a test for repeated calls. | `test_select_appointments_repeated_calls_return_consistent_results` | Low coverage improvement | Accepted because repeated calls should return consistent fresh lists without changing the source. | Test added. | Query suite passed 16 tests. |
| Add a test for already-sorted input. | `test_select_appointments_already_sorted_input` | Low coverage improvement | Accepted because FP-02 requires a new list even when the source is already ordered. | Test added. | Query suite passed 16 tests and full suite passed 94 tests at that review point. |
| No implementation defect identified. | Query code uses explicit inputs, a named key and `sorted()`. | No confirmed defect | Accepted only after human inspection and test execution. | No production-code correction required from this review. | Chloe reviewed and approved PR #31. |

The domain model protects appointment status transitions. `SmartCareDataStore` owns the session collections and conflict checks. Services coordinate lookup, validation and use cases. `queries.py` performs collection selection and ordering without input/output. `console.py` owns user interaction and recoverable messages. These boundaries keep domain rules, storage, workflow, query processing and presentation separate.

## F. Required reflections

1. **Which integration concern was architectural rather than a filtering or sorting detail?**

   The main architectural concern was ensuring that the console, services, query functions and domain objects used one shared `SmartCareDataStore`. Creating a new store inside each operation would make registered objects and appointment history disappear between menu choices. This concern involved dependency and session design rather than sorting logic.

2. **Which Copilot suggestion did you reject as over-engineering, and why?**

   No rejected Copilot suggestion is recorded in PR #31. The two documented suggestions were small test improvements and were accepted. Database persistence, external calendar integration and a new query framework were not introduced because they were outside Stage 9 requirements.

3. **How did you prove cancelled appointments remain retrievable and listable in the same session?**

   The workflow test cancels A1, confirms lookup returns the same A1 object with `CANCELLED` status, rejects reuse of A1’s ID and books A2 into the freed slot. Both A1 and A2 remain in the store. Service listing tests also confirm that all-status listing includes cancelled records while a scheduled-only filter excludes them.

## G. Ten formative answers

1. **What makes `select_appointments` pure, and what side effect breaks purity?**

   It uses only explicit inputs, returns a new list and performs no input/output. Sorting the source list in place or changing appointment fields would break purity.

2. **Which explicit inputs are needed, and why avoid a global store?**

   The query needs the appointment list, practitioner ID and optional status. A global store would hide the dependency and make testing and session isolation harder.

3. **How can a new list reuse `Appointment` objects safely?**

   The new list may contain references to the same appointment objects as long as the query does not mutate those objects.

4. **Why use a named key, and what breaks equal-time ties?**

   A named key makes the ordering rule reusable and testable. Appointment ID breaks ties when two appointments have the same date/time.

5. **How do default and explicit status filters differ?**

   `None` includes every appointment status. An explicit enum value includes only appointments with that status.

6. **How do empty, unknown-practitioner and invalid-filter cases differ?**

   A known practitioner with no matches returns an empty list. An unknown practitioner raises `LookupError`. A blank ID or invalid status raises `ValueError`.

7. **Which console errors recover, and how is unchanged state checked?**

   Expected `ValueError` and `LookupError` exceptions are displayed and the menu continues. Tests compare stored objects and fields before and after rejected operations.

8. **What is data integrity for registered participants, conflicts and history?**

   Appointments must use the actual registered patient and practitioner objects. Conflicting scheduled bookings are rejected, and cancelled appointments remain stored as history.

9. **What is Copilot’s review role, and who verifies findings?**

   Copilot can suggest possible issues or missing tests. A group member must compare each suggestion with the requirements, inspect the code and run tests before accepting it.

10. **How do pure functions and OOP responsibilities work together?**

    Domain objects protect their own valid state, services coordinate use cases, the store owns collections, and pure query functions transform collection views without changing domain state.

## H. Review, completion and common handover

**Issues and bounded branches:**

- [Issue #24 — workflow and console recovery verification](https://github.com/Saphal-uc/Assignment-3/issues/24)
- [Issue #26 — interactive console](https://github.com/Saphal-uc/Assignment-3/issues/26)
- [Issue #32 — practitioner appointment listing](https://github.com/Saphal-uc/Assignment-3/issues/32)
- `feature/stage9-integration`
- `feature/stage9-task1-clean`
- `stage9-services`
- `feature/stage9-console`

**Pull requests and review:**

- [PR #25 — workflow verification](https://github.com/Saphal-uc/Assignment-3/pull/25): authored by Saphal and approved by Chloe. Three workflow tests and 78 total tests passed.
- [PR #31 — appointment queries](https://github.com/Saphal-uc/Assignment-3/pull/31): authored by `UjwalBk1998` and approved by Chloe. Copilot suggestions led to two additional tests; 16 query tests and 94 total tests passed.
- [PR #30 — listing service](https://github.com/Saphal-uc/Assignment-3/pull/30): authored by `u3330161` and approved by Chloe. Thirty-seven service tests and 106 total tests passed.
- [PR #27 — interactive console](https://github.com/Saphal-uc/Assignment-3/pull/27): authored by Chloe. The PR records manual testing of menu options 1–7 and error recovery. No separate GitHub approval was recorded.
- [PR #29](https://github.com/Saphal-uc/Assignment-3/pull/29) remains open and appears to overlap the work later merged through PRs #31, #30 and #27. The repository owner should confirm that it contains no unique change and then close it.

**Copilot comparison:**

The recorded Copilot review suggested repeated-call and already-sorted-input tests. Chloe compared the suggestions with FP-02, asked for the tests, inspected the changes and reran the suite before approving PR #31. The exact prompt and complete Copilot transcript were not committed.

**Integrated common Stage 9 SHA:**

`d4556d25090d48ebf993a85ec5d57343c0ac6c6f`

Protected tag: `stage9-common-baseline`

**Regression evidence:**

- Working directory: `project/`
- Query review: 16 query tests and 94 total tests passed.
- Service review: 37 service tests and 106 total tests passed.
- Workflow review: 3 workflow tests and 78 total tests passed.
- The repository does not contain a separate full-suite result recorded immediately after PR #27 produced the final Stage 9 SHA.

**README and limitations:**

The [README](../project/README.md) contains the commands `python main.py` and `python -m pytest` and explains session-only storage. At the protected Stage 9 SHA, some starter TODO wording was still outdated even though the functions had been implemented. This is recorded as a documentation limitation rather than being hidden.

**Unresolved issues and action:**

- Confirm and close the superseded open PR #29 if it contains no unique change.
- The final option 8 console demonstration was not recorded in PR #27.
- A complete Copilot transcript and original pre-AI worksheet were not committed.
- The README at the Stage 9 baseline retained outdated TODO wording.
- The final full-suite run at the exact protected SHA was not recorded in the Stage 9 PR evidence.

**UG common candidate and PG plan:**

The common Stage 9 candidate is protected at `d4556d25090d48ebf993a85ec5d57343c0ac6c6f`. PG Stage 10 rescheduling and Stage 11 assurance work were completed later on separate branches and are not treated as Stage 9 implementation evidence.

- [x] Query contracts, purity, new lists and named-key ordering verified.
- [x] Service empty, unknown and invalid cases and cancellation history verified.
- [ ] Every console command and invalid-input recovery independently demonstrated.
- [x] Query and workflow tests plus previous tests passed at their recorded review points.
- [ ] Original human design and complete Copilot transcript recorded.
- [x] Reflections and ten formative responses completed.
- [ ] README fully updated at the protected Stage 9 SHA.
- [x] Common SHA protected for UG Stage 12; PG Stage 10 and Stage 11 work remained separate.

No persistence, rescheduling or assurance implementation is part of Stage 9. UG progression is 6 → 7 → 8 → 9 → 12. PG progression is 6 → 7 → 8 → 9 → 10 → 11 → 12. The mixed group uses one repository and protects the common Stage 9 candidate.