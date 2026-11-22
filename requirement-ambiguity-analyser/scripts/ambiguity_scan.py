import re
import sys

WEAK_WORDS = {
    r"\b(fast|quick(ly)?|slow|responsive)\b":          "Vague performance term (no number/unit)",
    r"\b(easy|simple|user[- ]friendly|intuitive)\b":   "Vague usability term (not measurable)",
    r"\b(secure|safe|robust|reliable)\b":              "Vague quality term (no criteria)",
    r"\b(etc\.?|and so on|and/or|as needed|if necessary)": "Open-ended / unclear scope",
    r"\b(appropriate|adequate|suitable|reasonable)\b": "Subjective term",
    r"\b(some|several|many|few|various)\b":            "Missing quantification",
    r"\b(should|may|might|could)\b":                   "Weak modal verb (is it mandatory?)",
}

def split_requirement(line, index):
    match = re.match(r"^\s*([A-Za-z]+-?\d+)\s*[:.)-]\s*(.+)$", line)
    if match:
        return match.group(1), match.group(2)
    return f"R{index}", line.strip()

def scan(text):
    for pattern, label in WEAK_WORDS.items():
        for m in re.finditer(pattern, text, flags=re.IGNORECASE):
            yield m.group(0), label

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python ambiguity_scan.py requirements.txt")

    with open(sys.argv[1], encoding="utf-8") as f:
        lines = [ln for ln in f if ln.strip()]

    print("| Req ID | Flagged Word | Defect | Statement |")
    print("|---|---|---|---|")

    total = 0
    for i, line in enumerate(lines, start=1):
        req_id, text = split_requirement(line, i)
        for word, label in scan(text):
            print(f"| {req_id} | {word} | {label} | {text} |")
            total += 1

    print(f"\nRequirements scanned: {len(lines)} | Keyword defects: {total}")

if __name__ == "__main__":
    main()
