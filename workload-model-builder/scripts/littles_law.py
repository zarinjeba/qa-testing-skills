import argparse

def main():
    parser = argparse.ArgumentParser(description="Little's Law workload sizing")
    parser.add_argument("--arrival-rate", type=float, help="users arriving per second (X)")
    parser.add_argument("--daily-users", type=float, help="total users per day")
    parser.add_argument("--peak-hour-percent", type=float, default=10.0,
                        help="percent of daily users arriving in the peak hour (default 10)")
    parser.add_argument("--session-seconds", type=float, required=True,
                        help="average session duration in seconds (R)")
    parser.add_argument("--safety-factor", type=float, default=1.0,
                        help="multiplier for growth/headroom, e.g. 1.5 = +50%%")
    args = parser.parse_args()

    if args.arrival_rate is not None:
        x = args.arrival_rate
    elif args.daily_users is not None:
        peak_hour_users = args.daily_users * args.peak_hour_percent / 100.0
        x = peak_hour_users / 3600.0
    else:
        parser.error("Provide --arrival-rate OR --daily-users")

    n = x * args.session_seconds
    n_with_headroom = n * args.safety_factor

    print(f"Arrival rate X          = {x:.3f} users/second")
    print(f"Session duration R      = {args.session_seconds:.0f} seconds")
    print(f"Concurrent users N=X*R  = {n:.0f}")
    print(f"With safety factor {args.safety_factor}x = {n_with_headroom:.0f} virtual users to simulate")

if __name__ == "__main__":
    main()
