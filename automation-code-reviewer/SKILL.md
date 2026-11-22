---
name: automation-code-reviewer
description: Reviews test automation code (Selenium, Playwright, Cypress, Postman/Newman, REST Assured, Cucumber/BDD, pytest, JUnit/TestNG) for reliability, maintainability, flakiness, locator quality, waits, assertions, data handling and framework design, and returns prioritised findings with fixed code. Use this skill whenever the user pastes or uploads automation scripts or step definitions and asks for review, refactoring, or "why is my test flaky". Do NOT use for application source code review or for writing manual test cases.
---

# Automation Code Reviewer

Review test scripts like a senior SDET and give fixes, not just complaints.

## Instructions
1. Identify the tool, language and framework pattern (POM, BDD, data-driven, keyword).
2. Review against this checklist:
   - **Locators**: prefer id / data-testid / stable CSS; flag brittle absolute XPath and index-based selectors.
   - **Waits**: flag `sleep`/`Thread.sleep`; require explicit or auto-waiting.
   - **Assertions**: every test must assert something meaningful; flag missing, weak or multiple unrelated assertions.
   - **Independence**: tests must not depend on execution order or shared state.
   - **Test data**: no hard-coded credentials/URLs; use config, fixtures or data files.
   - **Design**: Page Object / step reuse, no duplication, single responsibility per test.
   - **Reporting & logging**: clear names, failure messages, screenshots on failure.
   - **Cleanup**: teardown and data reset.
   - **Security hygiene**: secrets in code, tokens in logs.
   - **BDD** (if Cucumber): declarative steps, no UI detail in feature files, no duplicate steps.
   - **API tests** (if Postman/REST Assured): status, schema, response time and negative cases are checked.
3. Classify each finding: **Critical** (false pass/fail or security), **Major** (flaky/unmaintainable), **Minor** (style).
4. Provide a corrected code snippet for every Critical and Major finding.
5. Give an overall verdict and a score out of 10 with a one-line reason.

## Worked Example (Before / After)
**Before (problematic):** fixed sleep, absolute XPath, hard-coded password, no assertion.
```python
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://example.com/login")
time.sleep(5)
driver.find_element("xpath", "/html/body/div[2]/form/input[1]").send_keys("admin")
driver.find_element("xpath", "/html/body/div[2]/form/input[2]").send_keys("admin123")
driver.find_element("xpath", "/html/body/div[2]/form/button").click()
```

**After (fixed):** explicit wait, stable locators, secrets from environment, meaningful assertion, guaranteed cleanup.
```python
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_valid_login():
    driver = webdriver.Chrome()
    try:
        driver.get(os.environ["BASE_URL"] + "/login")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(os.environ["TEST_USER"])
        driver.find_element(By.ID, "password").send_keys(os.environ["TEST_PASS"])
        driver.find_element(By.CSS_SELECTOR, "[data-testid='login-btn']").click()
        wait.until(EC.url_contains("/dashboard"))
        assert "Dashboard" in driver.title, "User was not redirected to the dashboard after login"
    finally:
        driver.quit()
```

## Optional Helper Script
Run `python scripts/lint_automation.py <file>` for a fast anti-pattern scan, then add deeper findings by hand.

## Output Format
### Verdict
Score /10 and 2-line summary.

### Findings
| # | Severity | Location (file/line) | Issue | Why It Matters | Fix |
|---|---|---|---|---|---|

### Improved Code
Fenced code blocks, one per major fix.

### Quick Wins
3-5 bullet improvements.

## Rules
- Cite the exact line or snippet for each finding.
- Do not rewrite the whole script unless asked; fix only what is wrong.
- If the code is incomplete, say what you could not assess.
