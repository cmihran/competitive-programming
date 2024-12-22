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

# search for these 4 shapes
up_left = (-1, -1)
up_right = (-1, 1)
down_left = (1, -1)
down_right = (1, 1)
shapes = [
    # m,n = 3
    #   012
    # 0 M M
    # 1  A
    # 2 S S
    [(*up_left, 'M'), (*up_right, 'M'), (*down_left, 'S'), (*down_right, 'S')],
    # M S
    #  A
    # M S
    [(*up_left, 'M'), (*up_right, 'S'), (*down_left, 'M'), (*down_right, 'S')],
    # S M
    #  A
    # S M
    [(*up_left, 'S'), (*up_right, 'M'), (*down_left, 'S'), (*down_right, 'M')],
    # S S
    #  A
    # M M
    [(*up_left, 'S'), (*up_right, 'S'), (*down_left, 'M'), (*down_right, 'M')],
]

def matches_shape(row, col, shape):
    for d_x, d_y, char in shape:
        if not safe_check(row + d_x, col + d_y, char):
            return False
    return True

def safe_check(row, col, char):
    return 0 <= row < m and 0 <= col < n and matrix[row][col] == char

search_count = 0
for row in range(1, m - 1):
    for col in range(1, n - 1):
        if matrix[row][col] == 'A':
            search_count += any(matches_shape(row, col, shape) for shape in shapes)
print(search_count)