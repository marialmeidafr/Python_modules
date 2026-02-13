import sys


def main() -> None:
    print("=== Player Score Analytics ===")

    total_args: int = len(sys.argv)
    if total_args < 2:
        print("No scores provided. Usage: python3 ft_score_analytics.py"
              "<score1> <score2> ...")
    if total_args >= 2:
        try:
            scores: list[int] = [int(arg) for arg in sys.argv[1:]]
            print(f"Scores processed: {scores}")
            print(f"Total players: {total_args - 1}")
            print(f"Total score: {sum(scores)}")
            print(f"Average score: {sum(scores) / len(scores)}")
            print(f"High score: {max(scores)}")
            print(f"Low score: {min(scores)}")
            print(f"Score range: {max(scores) - min(scores)}")
        except ValueError:
            print("[ERROR] - All scores must be valid integers.")


if __name__ == "__main__":
    main()
