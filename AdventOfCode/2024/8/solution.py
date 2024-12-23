import itertools
import sys
from collections import defaultdict

from AdventOfCode.util import build_matrix, pretty_print

"""
Config
"""

sys.setrecursionlimit(10 ** 6)
test_file = 'input_a_test'
input_file = 'input_b_full'

"""
Implementation
"""
ANTI_NODE = '#'
EMPTY = '.'


def core(m, n, matrix, limit_anti):
    # create sets of antennas within same frequency
    freqs = defaultdict(list)
    for i in range(m):
        for j in range(n):
            if matrix[i][j] != EMPTY:
                freqs[matrix[i][j]].append((i, j))

    # for each unique pair of antennas, calculate the antinodes
    anti_nodes = set()
    for freq, nodes in freqs.items():
        for i in range(len(nodes)):
            for j in range(i + 1, len(nodes)):
                # pair of nodes
                a_row, a_col = nodes[i]
                b_row, b_col = nodes[j]
                # calculate slope
                d_row = a_row - b_row
                d_col = a_col - b_col
                # mark anti nodes on the map, if they are not an antenna
                if not limit_anti:
                    anti_nodes.add(nodes[i])
                    anti_nodes.add(nodes[j])
                # find points going one direction
                anti_a_row = a_row + d_row
                anti_a_col = a_col + d_col
                while 0 <= anti_a_row < m and 0 <= anti_a_col < n:
                    if matrix[anti_a_row][anti_a_col] == EMPTY:
                        matrix[anti_a_row][anti_a_col] = ANTI_NODE
                    anti_nodes.add((anti_a_row, anti_a_col))
                    anti_a_row += d_row
                    anti_a_col += d_col
                    if limit_anti:
                        break
                # find points going other direction
                anti_b_row = b_row - d_row
                anti_b_col = b_col - d_col
                while 0 <= anti_b_row < m and 0 <= anti_b_col < n:
                    if matrix[anti_b_row][anti_b_col] == EMPTY:
                        matrix[anti_b_row][anti_b_col] = ANTI_NODE
                    anti_nodes.add((anti_b_row, anti_b_col))
                    anti_b_row -= d_row
                    anti_b_col -= d_col
                    if limit_anti:
                        break
    pretty_print(matrix)
    # count number of anti nodes
    return len(anti_nodes)


def part1(name):
    m, n, matrix, = process_file(name)
    return core(m, n, matrix, True)


def part2(name):
    m, n, matrix, = process_file(name)
    return core(m, n, matrix, False)


def process_file(name):
    f = open(name)
    # lines = []
    # for line in f:
    #     # Insert processing here
    #     lines.append(line)
    # return lines
    return build_matrix(f)


"""
Output
"""

print(f'[Part 1] Test Result: {part1(test_file)}')
print(f'[Part 1] Real Result: {part1(input_file)}')
print(f'[Part 2] Test Result: {part2(test_file)}')
print(f'[Part 2] Real Result: {part2(input_file)}')
