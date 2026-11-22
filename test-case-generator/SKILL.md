---
name: test-case-generator
description: Generates structured, traceable test cases from requirements, user stories or features, using explicit coverage constraints (equivalence partitioning, boundary value analysis, decision tables, state transition, negative and edge cases). Use this skill whenever the user asks to write, generate, design or expand test cases, test scenarios or a test suite, even if they do not name a technique. Do NOT use for reviewing existing automation code or for performance/security test design.
---

# Test Case Generator (with Coverage Constraints)

Produce test cases that are traceable, technique-based and complete against a stated coverage target.

## Instructions
1. **Identify inputs**: requirements/feature, actors, input fields, business rules, states. If missing, ask once; otherwise state assumptions.
2. **Choose coverage constraints** (state them explicitly at the top):
   - Every requirement has at least 1 positive and 1 negative test.
   - Every input field: valid and invalid equivalence classes.
   - Every numeric/length limit: boundary values (min-1, min, min+1, max-1, max, max+1).
   - Every business rule combination: decision table row.
   - Every state/transition: state transition coverage when states exist.
3. **Design tests** using the techniques above. Add edge cases: empty, null, special characters, duplicates, session timeout, permission denied.
4. **Write each test case** in the format below. Keep steps atomic and expected results observable.
5. **Build a traceability matrix** (Requirement -> Test Case IDs).
6. **Self-check**: confirm every constraint in step 2 is met; list any gap explicitly.

## Optional Helper Script
Run `python scripts/boundary_values.py <min> <max>` to get exact boundary values and equivalence classes for a numeric field.

## Output Format
**Coverage constraints applied:** (bullet list)

| TC ID | Req ID | Title | Technique | Type (Pos/Neg/Boundary/Edge) | Priority | Preconditions | Test Data | Steps | Expected Result |
|---|---|---|---|---|---|---|---|---|---|

**Traceability Matrix**
| Req ID | Test Case IDs | Coverage Status |
|---|---|---|

**Assumptions & Gaps**

## Rules
- One objective per test case; no vague results such as "works correctly".
- Use concrete test data, not "valid value".
- IDs are sequential (TC_001, TC_002, ...).
- Do not invent requirements; mark assumptions clearly.
