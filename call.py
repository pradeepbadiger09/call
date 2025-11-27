import sys

if len(sys.argv) < 2:
    print("Usage: python array_scores.py <score1> <score2> <score3> ...")
    sys.exit()

scores = [int(x) for x in sys.argv[1:]]

# Main branch features
total = sum(scores)
average = total / len(scores)

print("Sum of scores:", total)
print("Average of scores:", average)