"""
https://adventofcode.com/2024/day/5
"""
from collections import defaultdict

f = open("./input")

# rules[x] is the set of rules that must come before x
rules = defaultdict(set)
valid_updates = []
invalid_updates = []
for line in f:
    if "|" in line:
        # process rule
        left, right = line.strip().split("|")
        rules[left].add(right)
    elif "," in line:
        # process update
        nums = line.strip().split(",")
        valid = True
        for i in range(len(nums)):
            # ensure nums comes before
            for j in range(0, i):
                if nums[j] in rules[nums[i]]:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            valid_updates.append(nums)
        else:
            invalid_updates.append(nums)

# part 1 - add midpoints of valid updates
p1 = 0
for update in valid_updates:
    p1 += int(update[len(update) // 2])
print(p1)

# part 2 - topological sort invalid ones to produce valid ordering
topo_sort = []
visited = set()
def dfs(node):
    if node in visited:
        return
    visited.add(node)
    for neighbor in rules[node]:
        if neighbor not in visited:
            dfs(neighbor)
    topo_sort.append(node)
for node in rules:
    if node not in visited:
        dfs(node)
topo_sort.reverse()

# use topo sort to calculate correct ordering
fixed_updates = []
print(len(invalid_updates))
print(topo_sort)
for update in invalid_updates:
    corrected_update = []
    for num in topo_sort:
        if num in update:
            corrected_update.append(num)
    fixed_updates.append(corrected_update)

# print out middle values of correct order
p2 = 0
for update in fixed_updates:
    p2 += int(update[len(update) // 2])
print(p2)
