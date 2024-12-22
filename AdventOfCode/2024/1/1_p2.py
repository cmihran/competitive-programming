"""
https://adventofcode.com/2024/day/1

Calculate a total similarity score by adding up each number in the left list
after multiplying it by the number of times that number appears in the right list
"""
from collections import Counter

f = open("./input", "r")
left = []
right = []
for line in f:
    res = line.split()
    left.append(int(res[0]))
    right.append(int(res[1]))

right_count = Counter(right)

score = 0
for num in left:
    score += (num * right_count[num])
print(score)