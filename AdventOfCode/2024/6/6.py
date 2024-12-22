import copy
import sys

from AdventOfCode.util import pretty_print

sys.setrecursionlimit(10 ** 6)


# build matrix
f = open("./input")
orig_matrix = []
for line in f:
    row = []
    for c in line:
        if c != '\n':
            row.append(c)
    orig_matrix.append(row)
m = len(orig_matrix)
n = len(orig_matrix[0])

# find start
UP = '^'
DOWN = 'v'
LEFT = '<'
RIGHT = '>'
MOVED = 'X'
OPEN = '.'
OBSTACLE = '#'
start = 0, 0
for row in range(m):
    for col in range(n):
        if orig_matrix[row][col] == UP:
            start = row, col
            break


# simulate guard
# If there is something directly in front of you, turn right 90 degrees.
# Otherwise, take a step forward.
def is_cycle(matrix, visited, row, col):
    # print(row, col)
    pretty_print(matrix)
    curr_dir = matrix[row][col]
    visited.add((row, col, curr_dir)) # row col dir

    # find next position
    if curr_dir == UP:
        next_row, next_col = row - 1, col
    elif curr_dir == DOWN:
        next_row, next_col = row + 1, col
    elif curr_dir == LEFT:
        next_row, next_col = row, col - 1
    elif curr_dir == RIGHT:
        next_row, next_col = row, col + 1


    if next_row < 0 or next_row >= m or next_col < 0 or next_col >= n:
        # got out of map
        return False

    next_pos = matrix[next_row][next_col]
    if next_pos == OPEN or next_pos == MOVED:
        matrix[next_row][next_col] = curr_dir
        matrix[row][col] = MOVED
        return is_cycle(matrix, visited, next_row, next_col)
    elif next_pos == OBSTACLE:
        next_dir = {
            UP: RIGHT,
            RIGHT: DOWN,
            DOWN: LEFT,
            LEFT: UP
        }
        next_char = next_dir[matrix[row][col]]
        if (row, col, next_char) in visited:
            # got into a loop
            return True
        else:
            matrix[row][col] = next_char
            return is_cycle(matrix, visited, row, col)

# try putting an obstacle in each spot
cycle_spots_count = 0
print('start', start)
print('m x n', m, n)
for i in range(m):
    for j in range(n):
        if i != start[0] or j != start[1]:
            matrix_copy = copy.deepcopy(orig_matrix)
            matrix_copy[i][j] = OBSTACLE
            visited = set()
            if is_cycle(matrix_copy, visited, start[0], start[1]):
                print(f'found good obstacle at {i} {j}')
                matrix_copy[i][j] = 'O'
                matrix_copy[start[0]][start[1]] = 'S'
                cycle_spots_count += 1
                # prettyprint(matrix_copy)
print(cycle_spots_count)

# p1 - count number of obstacles
# count = 0
# for i in range(m):
#     for j in range(n):
#         matrix_copy = copy.deepcopy(matrix)
#         matrix_copy[i][j] = OBSTACLE
#         if char == MOVED:
#             count += 1
# print(count)
