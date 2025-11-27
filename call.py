import sys

# Check if at least one score is provided
if len(sys.argv) < 2:
    print("Usage: python array_scores.py <score1> <score2> <score3> ...")
    sys.exit()

# Convert input arguments to integers
scores = [int(x) for x in sys.argv[1:]]

# Main branch features: Sum & Average
total = sum(scores)
average = total / len(scores)

maximum = max(scores)
minimum = min(scores)

print("Sum of scores:", total)
print("Average of scores:", average)
print("Maximum score:", maximum)
print("Minimum score:", minimum)