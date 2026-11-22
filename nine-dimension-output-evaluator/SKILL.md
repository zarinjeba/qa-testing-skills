---
name: nine-dimension-output-evaluator
description: Evaluates an AI-generated or human-written software testing output (test cases, test plan, requirements analysis, bug report, automation script, test report) across nine quality dimensions and returns a scored scorecard with evidence and improvement actions. Use this skill whenever the user asks to evaluate, grade, rate, validate or quality-check an AI output, or asks for a "scorecard", "rubric" or "nine dimensions". If the course or instructor gave their own nine dimensions, use those instead of the defaults.
---

# Nine-Dimension Output Evaluator

Score any testing artefact on nine dimensions with evidence, not opinion.

## Default Nine Dimensions
(Replace with the instructor's list if the user provides one.)

| # | Dimension | Question Asked |
|---|---|---|
| 1 | Correctness | Is the content technically and factually right? |
| 2 | Completeness | Are all required parts and scenarios present? |
| 3 | Relevance | Does it answer the actual task, without off-topic content? |
| 4 | Clarity | Is it unambiguous and easy to understand? |
| 5 | Consistency | Is it free of contradictions and uniform in format and terms? |
| 6 | Traceability | Can each item be linked to a requirement or source? |
| 7 | Testability / Actionability | Can someone execute or verify it directly? |
| 8 | Groundedness | Is it free of hallucinated facts, features or data? |
| 9 | Professional Structure | Does it follow standard format, naming and presentation? |

## Instructions
1. Confirm the artefact type and the original task/prompt it should satisfy. Ask if the original task is missing.
2. Score each dimension 1-5 (1 = poor, 3 = acceptable, 5 = excellent).
3. For every score give **evidence**: a quote or specific location from the output. A score without evidence is invalid.
4. Give a concrete **improvement action** for each dimension scored 3 or lower.
5. Compute: Total = sum (max 45); Percentage = Total / 45 x 100.
6. Final verdict: 90%+ Excellent | 75-89% Good | 60-74% Needs Improvement | below 60% Poor.
7. Check for **critical failures** (hallucination, wrong logic, missing core requirement). Any critical failure caps the verdict at "Needs Improvement".

## Optional Helper Script
Run `python scripts/score_calculator.py <9 scores> [--critical]` to compute total, percentage and verdict.

## Output Format
### Scorecard
| # | Dimension | Score (1-5) | Evidence | Improvement Action |
|---|---|---|---|---|

### Result
Total /45 | Percentage | Verdict

### Critical Failures
List or "None found".

### Top 3 Fixes
Priority actions to raise the score.

## Rules
- Be strict and consistent; do not inflate scores.
- Evaluate only what is provided.
