---
name: workload-model-builder
description: Builds a performance test workload model (user profiles, scenarios, transaction mix, think time, load/stress/spike/soak profiles, ramp-up, SLAs and metrics) from a system description or usage data, with Little's Law sizing and a JMeter/k6 mapping. Use this skill whenever the user asks for a workload model, load test plan, performance scenarios, concurrent user estimation, or how to design JMeter/k6/LoadRunner tests. Do NOT use for functional test design or security threat modelling.
---

# Workload Model Builder

Turn a system description into a realistic, defensible performance workload model.

## Instructions
1. **Collect inputs** (ask once for anything missing, else state assumptions): application type, key user journeys, total users, peak-hour traffic, business goals, SLAs, environment.
2. **Define user profiles/personas** and the percentage of users in each.
3. **Define scenarios**: ordered transactions per persona, with business-critical ones flagged.
4. **Build the transaction mix table**: share of total load per transaction.
5. **Size the load**:
   - Concurrent users = Throughput (users/s) x Session duration (s)   (Little's Law: N = X x R)
   - Pacing/think time per step; throughput target in requests/s or transactions/h.
6. **Choose load profiles** and define each: Baseline, Load (expected peak), Stress (above peak until break), Spike (sudden surge), Endurance/Soak (long duration), Scalability.
7. **Set ramp-up, steady-state and ramp-down** durations.
8. **Define acceptance criteria**: response time (e.g., p95), error rate, throughput, CPU/memory/DB thresholds.
9. **Define monitoring**: client metrics and server/DB/network metrics.
10. **Map to a tool** (JMeter thread group / k6 stages) using the example below.

## Tool Mapping Example (k6)
```javascript
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  stages: [
    { duration: '2m',  target: 100 },
    { duration: '10m', target: 100 },
    { duration: '1m',  target: 0   },
  ],

  thresholds: {
    http_req_duration: ['p(95)<800'],
    http_req_failed:   ['rate<0.01'],
  },
};

export default function () {

  const res = http.get(`${__ENV.BASE_URL}/`);
  check(res, { 'status is 200': (r) => r.status === 200 });

  sleep(Math.random() * 3 + 2);
}
```

## Optional Helper Script
Run `python scripts/littles_law.py --help` to calculate concurrent users and throughput.

## Output Format
### 1. Assumptions
### 2. User Profiles
| Persona | % of Users | Description |
### 3. Scenarios & Transaction Mix
| Scenario | Steps | Think Time | % of Load | Critical? |
### 4. Load Calculation
Show formulas and numbers.
### 5. Load Profiles
| Test Type | Users | Ramp-up | Duration | Goal |
### 6. Acceptance Criteria (SLA)
### 7. Monitoring Plan
### 8. Tool Mapping Example

## Rules
- Show the calculation, not just the result.
- Mark every invented number as an assumption.
