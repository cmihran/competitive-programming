import sys

"""
Config
"""

sys.setrecursionlimit(10 ** 6)
test_file = 'input_a_test'
input_file = 'input_b_full'
DEBUG = True

"""
Implementation
"""


def log(s=''):
    if DEBUG:
        print(s)


def core(data):
    pass


def part1(name):
    return core(process_file(name))


def part2(name):
    return core(process_file(name))


def process_file(name):
    # with open(name) as file:
    #     content = file.read()
    f = open(name)
    lines = []
    for line in f:
        # Insert processing here
        lines.append(line)
    return lines


"""
Output
"""

print()
print(f'[Part 1] Test Result: {part1(test_file)}')
# print(f'[Part 1] Real Result: {part1(input_file)}')
# print(f'[Part 2] Test Result: {part2(test_file)}')
# print(f'[Part 2] Real Result: {part2(input_file)}')
