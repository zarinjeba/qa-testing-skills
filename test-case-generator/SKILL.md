
---
name: test-case-generator
description: Generates structured software test cases from requirements while satisfying specified coverage constraints. Use when creating test cases with functional, boundary, negative, and requirement traceability coverage.
---

# Test Case Generator with Coverage Constraints

## 1. Purpose

This skill generates high-quality software test cases from functional and non-functional requirements while following user-defined test coverage constraints.

It aims to ensure that important requirements, scenarios, and input conditions are adequately tested.

## 2. When to Use

Use this skill when:
- Generating test cases from SRS or BRD documents.
- Creating test cases for a new software feature.
- Preparing positive and negative test scenarios.
- Applying Boundary Value Analysis (BVA).
- Applying Equivalence Partitioning (EP).
- Checking requirement coverage.
- Generating test cases with specific coverage targets.

## 3. Input Requirements

The user may provide:

- Software requirements or user stories.
- Feature descriptions.
- Application type.
- Required number of test cases.
- Coverage criteria or constraints.
- Test priority requirements.
- Preconditions and test environment.

If essential information is missing, ask the user for clarification.

## 4. Test Case Generation Instructions

Follow these steps:

1. Read and understand the provided requirements.
2. Identify individual functional requirements.
3. Break complex requirements into smaller testable conditions.
4. Identify positive test scenarios.
5. Identify negative test scenarios.
6. Identify boundary conditions and invalid inputs.
7. Apply Equivalence Partitioning where appropriate.
8. Apply Boundary Value Analysis where appropriate.
9. Generate test cases for each relevant scenario.
10. Assign unique test case IDs.
11. Map each test case to its related requirement.
12. Check whether the requested coverage constraints are satisfied.
13. Identify missing scenarios and coverage gaps.
14. Revise the test suite if necessary.

## 5. Coverage Constraints

Consider the following coverage criteria:

### 5.1 Requirement Coverage
Ensure every in-scope requirement is covered by at least one test case.

### 5.2 Positive Testing
Verify that the system works correctly with valid inputs.

### 5.3 Negative Testing
Verify that the system handles invalid inputs and unexpected conditions correctly.

### 5.4 Boundary Value Coverage
Test values at, below, and above relevant boundaries.

### 5.5 Equivalence Partitioning
Divide input data into valid and invalid equivalence classes.

### 5.6 Scenario Coverage
Cover important user workflows and alternative execution paths.

Follow the user's specified coverage constraints. Do not claim complete coverage unless it has been checked.

## 6. Test Case Structure

Generate test cases using the following fields:

| Field | Description |
|---|---|
| Test Case ID | Unique identifier |
| Requirement ID | Related requirement |
| Test Scenario | What is being tested |
| Preconditions | Required initial conditions |
| Test Steps | Actions to perform |
| Test Data | Input values |
| Expected Result | Expected system behavior |
| Priority | High, Medium, or Low |
| Test Type | Positive or Negative |

## 7. Quality Rules

- Every test case must have a clear objective.
- Expected results must be specific and measurable.
- Avoid duplicate test cases.
- Use unique test case IDs.
- Maintain requirement traceability.
- Respect the user's coverage constraints.
- Do not invent system behavior that is not defined in the requirements.
- Clearly identify assumptions.
- Separate confirmed coverage from estimated coverage.

## 8. Coverage Validation

After generating test cases:

1. Count the total generated test cases.
2. Identify covered requirements.
3. Identify uncovered requirements.
4. Check whether all requested test categories are represented.
5. Calculate requirement coverage when sufficient data is available.

Requirement Coverage Formula:

Requirement Coverage (%) =
(Covered Requirements / Total In-Scope Requirements) × 100

Report any unmet coverage constraints.

## 9. Error Handling

- If requirements are missing, request the requirements.
- If coverage constraints are unclear, ask for clarification.
- If expected results cannot be determined, mark them as requiring clarification.
- If requirements conflict, report the conflict.
- If the requested number of test cases cannot satisfy the coverage constraints, explain why.

## 10. Example

Input Requirement:

"The login system shall allow users to log in using a valid email and password."

Generated Test Cases:

| ID | Scenario | Test Data | Expected Result |
|---|---|---|---|
| TC-001 | Valid login | Valid email and password | Login successful |
| TC-002 | Invalid password | Valid email and wrong password | Login rejected |
| TC-003 | Invalid email | Invalid email format | Validation error |
| TC-004 | Empty email | Blank email | Required field message |
| TC-005 | Empty password | Blank password | Required field message |

## 11. Final Output

Provide:

- Generated test case table.
- Coverage summary.
- Covered requirements.
- Uncovered requirements.
- Unmet constraints.
- Recommendations for improving test coverage.
