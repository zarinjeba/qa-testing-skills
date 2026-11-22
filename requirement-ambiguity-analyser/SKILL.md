
---
name: requirement-ambiguity-analyser
description: Analyzes software requirements to identify ambiguity, incompleteness, inconsistency, and testability issues. Use when reviewing or refining software requirements before test case design.
---

# Requirement Ambiguity Analyser

## 1. Purpose

This skill analyzes software requirements and identifies unclear, incomplete, vague, conflicting, and untestable statements.

Its goal is to improve requirement quality before software development and testing.

## 2. When to Use

Use this skill when:
- Reviewing software requirement documents.
- Analyzing SRS or BRD documents.
- Identifying ambiguous requirement statements.
- Improving unclear requirements.
- Preparing requirements for test case generation.

## 3. Input Requirements

The user may provide:
- Individual requirement statements.
- SRS documents.
- BRD documents.
- Functional requirements.
- Non-functional requirements.

If no requirement is provided, ask the user to share one.

## 4. Analysis Instructions

Follow these steps:

1. Read and understand each requirement.
2. Identify vague words such as "fast", "easy", "user-friendly", and "appropriate".
3. Check whether the requirement is complete.
4. Identify missing conditions, values, and expected outcomes.
5. Check for conflicting statements.
6. Evaluate whether the requirement is measurable and testable.
7. Explain why each identified issue is problematic.
8. Suggest an improved version of each unclear requirement.
9. Do not invent missing business rules or assumptions.

## 5. Ambiguity Categories

Analyze requirements using these categories:

- Vagueness: Unclear or subjective wording.
- Incompleteness: Missing information.
- Inconsistency: Conflicting requirements.
- Unverifiability: Cannot be objectively tested.
- Multiple Interpretations: Can be understood in different ways.

## 6. Output Format

Present the results in a table:

| Requirement ID | Original Requirement | Issue Type | Explanation | Suggested Improvement |

After the table, provide:
- Total requirements analyzed.
- Total issues identified.
- High-priority issues.
- Clarification questions for stakeholders.

## 7. Quality Rules

- Preserve the original meaning.
- Use clear and simple language.
- Make suggestions measurable and testable.
- Never assume missing business rules.
- Explain uncertainty explicitly.

## 8. Error Handling

- If requirements are missing, ask for input.
- If a requirement is incomplete, identify the missing information.
- If conflicting requirements exist, report both statements.
- If context is insufficient, ask clarification questions.

## 9. Example

Input:
"The system should respond quickly to user requests."

Analysis:
- Issue Type: Vagueness.
- Explanation: "Quickly" does not define an acceptable response time.

Suggested Improvement:
"The system shall respond to 95% of user requests within 2 seconds under the specified normal workload."

Note: The proposed threshold is an example and must be confirmed by stakeholders.
