import csv
import sys
from collections import defaultdict

def read_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python coverage_audit.py requirements.csv testcases.csv")

    requirements = read_csv(sys.argv[1])
    testcases = read_csv(sys.argv[2])

    types_by_req = defaultdict(set)
    for tc in testcases:
        types_by_req[tc["req_id"].strip()].add(tc["type"].strip().lower())

    uncovered, weak, full = [], [], []
    known_ids = set()
    for req in requirements:
        rid = req["req_id"].strip()
        known_ids.add(rid)
        kinds = types_by_req.get(rid, set())
        if not kinds:
            uncovered.append(rid)
        elif kinds == {"positive"}:
            weak.append(rid)
        else:
            full.append(rid)

    orphans = [tc["tc_id"] for tc in testcases if tc["req_id"].strip() not in known_ids]

    total = len(requirements)
    covered = len(full) + len(weak)
    pct = (covered / total * 100) if total else 0.0

    print("| Metric | Value |")
    print("|---|---|")
    print(f"| Total requirements | {total} |")
    print(f"| Fully covered | {len(full)} |")
    print(f"| Weakly covered (positive only) | {len(weak)} |")
    print(f"| Uncovered | {len(uncovered)} |")
    print(f"| Requirement coverage | {pct:.1f}% |")
    print(f"\nUncovered : {', '.join(uncovered) or 'None'}")
    print(f"Weak      : {', '.join(weak) or 'None'}")
    print(f"Orphan TCs: {', '.join(orphans) or 'None'}")

if __name__ == "__main__":
    main()
