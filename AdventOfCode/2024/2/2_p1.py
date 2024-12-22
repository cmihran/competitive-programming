"""
So, a report only counts as safe if both of the following are true:

    The levels are either all increasing or all decreasing.
    Any two adjacent levels differ by at least one and at most three.

Analyze the unusual data from the engineers. How many reports are safe?
"""
def is_safe(line):
    vals = [int(x) for x in line.split()]
    increasing = vals[0] < vals[1]
    for i in range(1, len(vals)):
        prev = vals[i-1]
        curr = vals[i]
        diff = abs(prev - curr)
        if diff < 1 or diff > 3:
            return False
        if (increasing and curr < prev) or (not increasing and curr > prev):
            return False
    return True

f = open("./input")
safe_count = 0
for line in f:
    safe_count += is_safe(line)
print(safe_count)

