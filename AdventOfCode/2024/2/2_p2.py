"""
So, a report only counts as safe if both of the following are true:

    The levels are either all increasing or all decreasing.
    Any two adjacent levels differ by at least one and at most three.

Analyze the unusual data from the engineers. How many reports are safe?
"""
# def is_safe(line):
#     vals = [int(x) for x in line.split()]
#     increasing = vals[0] < vals[1]
#     p_i = 0
#     c_i = 1
#     removed_problem = False
#     while c_i < len(vals):
#         prev = vals[p_i]
#         curr = vals[c_i]
#         diff = abs(prev - curr)
#         if (diff == 0 or diff > 3) or (increasing and curr < prev) or (not increasing and curr > prev):
#             # problem level - try to remove
#             if removed_problem:
#                 # already removed, not safe
#                 return False
#             else:
#                 # try to remove this one by keeping prev as-is and incrementing curr
#                 removed_problem = True
#                 c_i += 1
#         else:
#             # valid, continue
#             p_i += 1
#             c_i += 1
#     return True

def is_safe(vals):
    increasing = vals[0] < vals[1]
    for i in range(1, len(vals)):
        prev = vals[i-1]
        curr = vals[i]
        diff = abs(prev - curr)
        if (diff < 1 or diff > 3) or (increasing and curr < prev) or (not increasing and curr > prev):
            return False
    return True

f = open("./input")
safe_count = 0
for line in f:
    row = [int(x) for x in line.split()]
    safe_count += any([is_safe(row[:i] + row[i + 1:]) for i in range(len(row))])
print(safe_count)

