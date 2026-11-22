---
name: requirement-ambiguity-analyser
description: Analyses software requirements (BRD, SRS, user stories, acceptance criteria) and finds ambiguous, vague, incomplete, conflicting or untestable statements, then proposes measurable rewrites. Use this skill whenever the user asks to review, validate, clean up or "check quality of" requirements, or shares a BRD/SRS/user story and wants it tested before test design. Do NOT use for writing test cases or reviewing code.
---

# Requirement Ambiguity Analyser

Find requirement defects early, before they become test and code defects.

## When to Use
- User shares a BRD, SRS, user story, feature description or acceptance criteria.
- User asks: "review requirements", "find ambiguity", "is this testable?", "static testing of SRS".

## Instructions
1. Split the input into individual requirements. Assign an ID (use the original ID if present, else R1, R2, ...).
2. Check every requirement against these defect types:
   - **Vague term**: fast, easy, user-friendly, secure, efficient, appropriate, etc., and so on, as needed.
   - **Missing quantification**: no number, unit, limit or threshold.
   - **Incomplete**: missing actor, trigger, condition, data, error case or boundary.
   - **Ambiguous reference**: unclear "it", "they", "the system", passive voice without actor.
   - **Conflict**: contradicts another requirement or the stated scope.
   - **Untestable**: no objective pass/fail criterion.
   - **Compound**: several requirements joined by "and/or" in one statement.
3. Rate severity: **High** (blocks testing or causes wrong build), **Medium**, **Low**.
4. Write a measurable rewrite for each defect. Never invent business facts; if a value is unknown, mark it `[TBD - confirm with stakeholder]`.
5. List clarification questions for the BA/stakeholder.

## Optional Helper Script
Run `python scripts/ambiguity_scan.py <requirements.txt>` for a fast first-pass list of vague words, then add judgement-based findings (conflicts, missing conditions).

## Output Format
### 1. Summary
Total requirements reviewed, defects found, count by severity.

### 2. Defect Table
| Req ID | Original Statement | Defect Type | Why It Is a Problem | Severity | Suggested Rewrite |
|---|---|---|---|---|---|

### 3. Clarification Questions
Numbered list, each linked to a Req ID.

### 4. Testability Verdict
One line per requirement: Testable / Needs Clarification / Untestable.

## Rules
- Quote the exact problem words from the original text.
- Report only real defects; do not pad the table.
- If no requirement text is provided, ask the user to paste or upload it.
