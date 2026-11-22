import sys

def boundary_values(lo, hi):
    return [
        (lo - 1, False, "Just below minimum"),
        (lo,     True,  "Minimum boundary"),
        (lo + 1, True,  "Just above minimum"),
        (hi - 1, True,  "Just below maximum"),
        (hi,     True,  "Maximum boundary"),
        (hi + 1, False, "Just above maximum"),
    ]

def equivalence_classes(lo, hi):
    mid = (lo + hi) // 2
    return [
        ("Invalid (below range)", lo - 10, False),
        ("Valid (inside range)",  mid,     True),
        ("Invalid (above range)", hi + 10, False),
    ]

def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python boundary_values.py <min> <max>")

    lo, hi = int(sys.argv[1]), int(sys.argv[2])
    if lo >= hi:
        sys.exit("min must be smaller than max")

    print(f"## Boundary Value Analysis for range [{lo}, {hi}]")
    print("| Value | Expected | Reason |")
    print("|---|---|---|")
    for value, valid, label in boundary_values(lo, hi):
        print(f"| {value} | {'Accept' if valid else 'Reject'} | {label} |")

    print("\n## Equivalence Partitions")
    print("| Class | Representative Value | Expected |")
    print("|---|---|---|")
    for name, value, valid in equivalence_classes(lo, hi):
        print(f"| {name} | {value} | {'Accept' if valid else 'Reject'} |")

    print("\nAlso test: empty value, non-numeric text, decimal, negative, very large number, special characters.")

if __name__ == "__main__":
    main()
