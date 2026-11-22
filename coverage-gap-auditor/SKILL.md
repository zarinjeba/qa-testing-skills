
---
name: coverage-gap-auditor
description: Audits software test suites to identify requirement coverage gaps, missing test scenarios, untested conditions, and traceability issues. Use when evaluating the completeness of an existing test suite.
---

# Coverage Gap Auditor

## 1. Purpose

This skill evaluates an existing software test suite against software requirements to identify missing test coverage.

It helps testers discover untested requirements, missing scenarios, and weaknesses in test coverage.

## 2. When to Use

Use this skill when:
- Reviewing an existing test suite.
- Checking requirement coverage.
- Identifying missing test cases.
- Evaluating test completeness.
- Reviewing Requirement Traceability Matrices (RTM).
- Preparing test coverage reports.

## 3. Input Requirements

The user may provide:

- Software Requirements Specification (SRS).
- Functional requirements.
- Test cases.
- Requirement Traceability Matrix (RTM).
- Test execution results.
- Coverage targets.

If test cases or requirements are missing, request the necessary information.

## 4. Audit Instructions

Follow these steps:

1. Read and understand the provided requirements.
2. Review all available test cases.
3. Identify unique requirement IDs.
4. Map each test case to its related requirement.
5. Check whether every in-scope requirement has at least one test case.
6. Identify requirements without test coverage.
7. Identify missing positive and negative scenarios.
8. Check boundary conditions where applicable.
9. Detect duplicate or irrelevant test cases.
10. Identify incomplete requirement traceability.
11. Calculate coverage metrics using available data.
12. Recommend additional test cases to close identified gaps.

## 5. Types of Coverage Gaps

### 5.1 Requirement Coverage Gap
A requirement has no associated test case.

### 5.2 Scenario Coverage Gap
Important user scenarios are not tested.

### 5.3 Positive Testing Gap
Valid input conditions are not adequately tested.

### 5.4 Negative Testing Gap
Invalid input conditions and error handling are not tested.

### 5.5 Boundary Coverage Gap
Important boundary values are missing.

### 5.6 Traceability Gap
A test case cannot be mapped to a specific requirement.

## 6. Coverage Calculation

Calculate requirement coverage using:

Requirement Coverage (%) =
(Covered Requirements / Total In-Scope Requirements) × 100

Uncovered Requirements (%) =
(Uncovered Requirements / Total In-Scope Requirements) × 100

Only count unique in-scope requirements.

Do not count excluded requirements as uncovered.

If the input data is insufficient, explain the limitation instead of inventing metrics.

## 7. Output Format

Present the audit results using the following structure.

### 7.1 Coverage Summary

| Metric | Result |
|---|---|
| Total Requirements | Number |
| Covered Requirements | Number |
| Uncovered Requirements | Number |
| Requirement Coverage | Percentage |
| Total Test Cases | Number |

### 7.2 Coverage Gap Report

| Requirement ID | Requirement | Existing Test Coverage | Identified Gap | Priority |

### 7.3 Recommended Test Cases

| Test Case ID | Requirement ID | Scenario | Expected Result | Priority |

### 7.4 Final Audit Result

Include:
- Overall coverage status.
- Major coverage gaps.
- Missing test scenarios.
- Recommendations for improvement.

## 8. Quality Rules

- Do not assume that a requirement is covered without evidence.
- Maintain requirement-to-test-case traceability.
- Avoid counting duplicate test cases as additional requirement coverage.
- Distinguish requirement coverage from code coverage.
- Do not invent missing test execution results.
- Clearly identify assumptions and limitations.
- Prioritize critical and high-risk coverage gaps.

## 9. Error Handling

- If requirements are missing, request them.
- If test cases are missing, request the test suite.
- If requirement IDs are inconsistent, report the issue.
- If coverage cannot be calculated, explain why.
- If a requirement is ambiguous, flag it for clarification.

## 10. Example

Requirements:

| Requirement ID | Description |
|---|---|
| REQ-01 | User can log in with valid credentials. |
| REQ-02 | User receives an error for invalid credentials. |
| REQ-03 | User account is locked after five failed attempts. |

Existing Test Cases:

| Test Case ID | Requirement ID | Scenario |
|---|---|---|
| TC-01 | REQ-01 | Valid login |
| TC-02 | REQ-02 | Invalid password |

Audit Findings:

- REQ-01: Covered.
- REQ-02: Covered.
- REQ-03: Uncovered.

Coverage Calculation:

Requirement Coverage = (2 / 3) × 100 = 66.67%

Recommended Test Case:

TC-03: Verify that the account is locked after five consecutive failed login attempts.

Expected Result: The system locks the account according to the specified requirement.

## 11. Final Output

Provide a structured coverage audit report containing:

1. Coverage summary.
2. Identified coverage gaps.
3. Uncovered requirements.
4. Recommended test cases.
5. Improvement recommendations.
