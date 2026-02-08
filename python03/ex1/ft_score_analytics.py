"""
Player Score Analytics

This program processes player scores passed as command-line arguments
and displays basic statistics such as total, average, highest, lowest,
and score range.
"""
import sys

if __name__ == "__main__":
    scores: list = []
    error: bool = 0
    print("=== Player Score Analytics ===")
    if (len(sys.argv)) < 2:
        print("No scores provided. Usage: python3", end=" ")
        print("ft_score_analytics.py <score1> <score2> ...")
    else:
        try:
            for a in sys.argv[1:]:
                scores.append(int(a))
        except ValueError as e:
            error = 1
            print("Error:", e)
        if (error == 0):
            print(f"Scores processed: {scores}")
            print("Total playesr: ", len(sys.argv) - 1)
            print("Total score:", sum(scores))
            print("Average score:", sum(scores) / (len(sys.argv) - 1))
            print("High score:", max(scores))
            print("Low score:", min(scores))
            print("Score range:", max(scores) - min(scores))
