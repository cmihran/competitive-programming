"""
https://adventofcode.com/2024/day/1

Pair up the smallest number in the left list with the smallest number in the right list,
then the second-smallest left number with the second-smallest right number, and so on

Within each pair, figure out how far apart the two numbers are;
you'll need to add up all of those distances and return the sum.
"""
f = open("./input", "r")
left = []
right = []
for line in f:
    res = line.split()
    left.append(int(res[0]))
    right.append(int(res[1]))
left.sort()
right.sort()
dist = 0
for i in range(len(left)):
    dist += abs(left[i] - right[i])
print(dist)
