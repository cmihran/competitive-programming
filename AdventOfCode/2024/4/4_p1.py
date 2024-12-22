"""
This word search allows words to be horizontal, vertical, diagonal, written backwards,
or even overlapping other words. It's a little unusual, though, as you don't merely
need to find one instance of XMAS - you need to find all of them
"""

# construct matrix
f = open("./input")
matrix = [[char for char in line if char != '\n'] for line in f]
m = len(matrix)
n = len(matrix[0])
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
search_word = "XMAS"

def dfs(row, col, i, vector):
    # check that the cell is in bounds
    if (row < 0 or row >= m
            or col < 0 or col >= n
            or i >= len(search_word)
            or matrix[row][col] != search_word[i]):
        return 0

    # check if we found last char
    if i == len(search_word) - 1:
        # found a path
        return 1
    else:
        # else we DFS in each direction and continue on word
        return dfs(row + vector[0], col + vector[1], i + 1, vector)

# DFS from each cell
search_count = 0
for row in range(m):
    for col in range(n):
        for vector in DIRS:
            search_count += dfs(row, col, 0, vector)
print(search_count)