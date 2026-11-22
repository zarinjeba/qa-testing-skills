---
name: coverage-gap-auditor
description: Audits a set of test cases against requirements (and optionally code or a coverage report) to find uncovered requirements, missing test types, weak boundary/negative coverage, redundant tests and traceability gaps, then recommends prioritised tests to add. Use this skill whenever the user asks to check test coverage, find gaps, review a test suite or RTM, or asks "what is missing in my test cases?". Do NOT use to generate a full test suite from scratch.
---

# Coverage Gap Auditor

Compare what must be tested with what is actually tested, and report the gaps.

## Instructions
1. **Collect both sides**: requirements/features list and existing test cases. Optional: coverage report (statement/branch %), defect history. If either side is missing, ask for it.
2. **Build a mapping** Requirement -> Test Cases. A requirement with zero tests is **Uncovered**; with only positive tests is **Weakly covered**.
3. **Audit dimensions** for each requirement:
   - Positive path, negative path, boundary values, equivalence classes
   - Error handling and validation messages
   - Security and permission cases
   - Non-functional (performance, usability, compatibility) where the requirement implies it
   - Integration / data-flow and state transitions
4. **Detect quality issues**: duplicate tests, tests with no requirement link, vague expected results, missing preconditions.
5. **Score coverage**: Requirement coverage % = covered requirements / total requirements. Report separately for "fully" vs "weakly" covered.
6. **Prioritise gaps** by risk (impact x likelihood): Critical / High / Medium / Low.
7. **Recommend tests** to close each gap (title + technique only, not full cases, unless asked).

## Optional Helper Script
Run `python scripts/coverage_audit.py <requirements.csv> <testcases.csv>` to compute requirement coverage and list orphan tests.

## Output Format
### Coverage Summary
Total requirements | Fully covered | Weakly covered | Uncovered | Coverage %

### Gap Table
| Req ID | Gap Type | Missing Coverage | Risk | Recommended Test(s) |
|---|---|---|---|---|

### Quality Issues
Duplicates, orphan tests, weak expected results.

### Action Plan
Top 5 fixes in priority order.

## Rules
- Base every finding on the provided data; never claim a percentage you cannot compute.
- Distinguish "not tested" from "not provided to me".
