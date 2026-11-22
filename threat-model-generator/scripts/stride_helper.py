import argparse

STRIDE = {
    "Spoofing":               ("Authentication",   "Can someone pretend to be another user or system?",      "Strong auth, MFA, token validation"),
    "Tampering":              ("Integrity",        "Can data be modified in transit or at rest?",            "Input validation, TLS, digital signatures"),
    "Repudiation":            ("Non-repudiation",  "Can a user deny an action with no proof?",               "Audit logs, timestamps, log protection"),
    "Information Disclosure": ("Confidentiality",  "Can sensitive data leak to unauthorised parties?",       "Encryption, access control, error masking"),
    "Denial of Service":      ("Availability",     "Can the service be made unavailable?",                   "Rate limiting, quotas, redundancy"),
    "Elevation of Privilege": ("Authorisation",    "Can a user gain rights they should not have?",           "Least privilege, role checks on server side"),
}

def rate(likelihood, impact):
    score = likelihood * impact
    if score <= 4:
        label = "Low"
    elif score <= 9:
        label = "Medium"
    elif score <= 16:
        label = "High"
    else:
        label = "Critical"
    return score, label

def main():
    parser = argparse.ArgumentParser(description="STRIDE helper (defensive)")
    parser.add_argument("--checklist", action="store_true", help="print STRIDE checklist")
    parser.add_argument("--likelihood", type=int, choices=range(1, 6), help="1 (rare) .. 5 (almost certain)")
    parser.add_argument("--impact", type=int, choices=range(1, 6), help="1 (minor) .. 5 (severe)")
    args = parser.parse_args()

    if args.checklist:
        print("| STRIDE | Property | Question | Typical Defence |")
        print("|---|---|---|---|")
        for name, (prop, question, defence) in STRIDE.items():
            print(f"| {name} | {prop} | {question} | {defence} |")

    if args.likelihood and args.impact:
        score, label = rate(args.likelihood, args.impact)
        print(f"\nRisk score = {args.likelihood} x {args.impact} = {score}  ->  {label}")

    if not args.checklist and not (args.likelihood and args.impact):
        parser.print_help()

if __name__ == "__main__":
    main()
