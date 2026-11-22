---
name: threat-model-generator
description: Generates a structured security threat model for an application or feature using STRIDE, data flow analysis, trust boundaries, attack surface and DREAD/risk rating, with mitigations and security test ideas mapped to OWASP Top 10. Use this skill whenever the user asks for a threat model, STRIDE analysis, attack surface, security risk assessment or security test planning for a system, even if they do not use the word "STRIDE". Do NOT use to write exploit code or attack tools; this skill is defensive only.
---

# Threat Model Generator

Defensive threat modelling to support secure design and security test planning.

## Instructions
1. **Understand the system**: purpose, actors, components, data stored, external integrations, tech stack. Ask once if missing; otherwise state assumptions.
2. **Describe the architecture** as a text data-flow: external entities, processes, data stores, data flows.
3. **Mark trust boundaries** (e.g., Internet / App server / Database / Third-party API).
4. **Apply STRIDE** to each component and data flow:
   - **S**poofing -> authentication
   - **T**ampering -> integrity
   - **R**epudiation -> logging / non-repudiation
   - **I**nformation disclosure -> confidentiality
   - **D**enial of service -> availability
   - **E**levation of privilege -> authorisation
5. **Rate risk**: Likelihood (1-5) x Impact (1-5) = Risk score; map to Low / Medium / High / Critical.
6. **Propose mitigations** (preventive and detective) for each threat.
7. **Map to OWASP Top 10** categories where relevant.
8. **Write security test cases** to verify each mitigation (what to test, not how to exploit).

## Optional Helper Script
Run `python scripts/stride_helper.py --checklist` for the STRIDE question list, or pass `--likelihood` and `--impact` to rate a threat.

## Output Format
### 1. System Overview & Assumptions
### 2. Data Flow & Trust Boundaries
### 3. Threat Table
| ID | Component / Flow | STRIDE | Threat Description | Likelihood | Impact | Risk | OWASP Ref |
### 4. Mitigations
| Threat ID | Mitigation | Type (Preventive/Detective) |
### 5. Security Test Ideas
| Threat ID | Test Objective | Expected Secure Behaviour |
### 6. Top 5 Priority Risks

## Rules
- Describe threats and defences at design level; never output working exploits or payload strings.
- Every threat needs at least one mitigation.
- Do not claim a system is secure; state residual risk.
