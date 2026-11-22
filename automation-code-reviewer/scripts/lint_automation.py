import re
import sys

RULES = [
    ("Major",    r"(time\.sleep|Thread\.sleep|cy\.wait\(\d+\)|waitForTimeout)",
                 "Fixed sleep used",
                 "Use explicit/auto waits (WebDriverWait, Playwright auto-wait)."),
    ("Major",    r"[\"']/html/body|[\"']//\*\[@id=.*\]/.*/.*/.*",
                 "Long or absolute XPath",
                 "Use id, data-testid or a short CSS selector."),
    ("Critical", r"(password|passwd|pwd|token|secret|api[_-]?key)\s*=\s*[\"'][^\"']+[\"']",
                 "Hard-coded credential or secret",
                 "Read from environment variables or a secrets manager."),
    ("Minor",    r"https?://(localhost|127\.0\.0\.1|[\w.-]+\.\w{2,})",
                 "Hard-coded URL",
                 "Move base URL to configuration."),
    ("Minor",    r"except\s*:\s*pass|catch\s*\(\s*\w+\s*\)\s*\{\s*\}",
                 "Swallowed exception",
                 "Log the error or let the test fail."),
]

ASSERT_HINTS = re.compile(r"\b(assert|expect|should|verify|assertEquals|assertThat)\b", re.IGNORECASE)

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python lint_automation.py <file>")

    with open(sys.argv[1], encoding="utf-8") as f:
        lines = f.readlines()

    findings = []

    for number, line in enumerate(lines, start=1):
        for severity, pattern, message, fix in RULES:
            if re.search(pattern, line, flags=re.IGNORECASE):
                findings.append((severity, number, message, fix, line.strip()))

    if not any(ASSERT_HINTS.search(line) for line in lines):
        findings.append(("Critical", 0, "No assertions found in file",
                         "Add meaningful assertions with clear failure messages.", "(whole file)"))

    order = {"Critical": 0, "Major": 1, "Minor": 2}
    findings.sort(key=lambda item: (order[item[0]], item[1]))

    print("| Severity | Line | Issue | Fix | Code |")
    print("|---|---|---|---|---|")
    for severity, number, message, fix, code in findings:
        print(f"| {severity} | {number or '-'} | {message} | {fix} | `{code[:60]}` |")
    print(f"\nTotal findings: {len(findings)}")

if __name__ == "__main__":
    main()
