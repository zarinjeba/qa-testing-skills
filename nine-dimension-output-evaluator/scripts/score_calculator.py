import argparse

DIMENSIONS = [
    "Correctness", "Completeness", "Relevance", "Clarity", "Consistency",
    "Traceability", "Testability/Actionability", "Groundedness", "Professional Structure",
]

def verdict(percentage, has_critical):
    if percentage >= 90:
        result = "Excellent"
    elif percentage >= 75:
        result = "Good"
    elif percentage >= 60:
        result = "Needs Improvement"
    else:
        result = "Poor"

    if has_critical and result in ("Excellent", "Good"):
        result = "Needs Improvement (capped by critical failure)"
    return result

def main():
    parser = argparse.ArgumentParser(description="Nine-dimension score calculator")
    parser.add_argument("scores", type=int, nargs=9, help="nine scores from 1 to 5")
    parser.add_argument("--critical", action="store_true", help="a critical failure was found")
    args = parser.parse_args()

    if any(s < 1 or s > 5 for s in args.scores):
        parser.error("every score must be between 1 and 5")

    total = sum(args.scores)
    max_total = 5 * len(DIMENSIONS)
    percentage = total / max_total * 100

    print("| # | Dimension | Score |")
    print("|---|---|---|")
    for i, (name, score) in enumerate(zip(DIMENSIONS, args.scores), start=1):
        print(f"| {i} | {name} | {score}/5 |")

    print(f"\nTotal      : {total}/{max_total}")
    print(f"Percentage : {percentage:.1f}%")
    print(f"Verdict    : {verdict(percentage, args.critical)}")

    weak = [n for n, s in zip(DIMENSIONS, args.scores) if s <= 3]
    print(f"Needs improvement action: {', '.join(weak) if weak else 'None'}")

if __name__ == "__main__":
    main()
