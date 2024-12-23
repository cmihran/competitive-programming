import itertools
import sys
from collections import deque

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
FREE_SPACE = '.'


def log(s=''):
    if DEBUG:
        print(s)


def find_next_free(data, start, end, min_len):
    for i in range(start, end):
        char, length = data[i]
        if char == FREE_SPACE and length >= min_len:
            return i
    return -1


def find_next_id(data, right, target):
    for i in range(right, -1, -1):
        char, length = data[i]
        if char != FREE_SPACE and int(char) == int(target):
            return i
    return -1


def checksum(formatted_string):
    res = 0
    for i in range(len(formatted_string)):
        if formatted_string[i] != FREE_SPACE:
            res += (i * int(formatted_string[i]))
    return res


def format_disk(data):
    s = ""
    for char, length in data:
        s += str(char) * length
    return s


# [i - 1][i][i + 1] --> [i]
def merge_free(data, i, length):
    if i < len(data) - 1 and data[i + 1][0] == FREE_SPACE:
        length += data[i + 1][1]
        del data[i + 1]
    if i > 0 and data[i - 1][0] == FREE_SPACE:
        length += data[i - 1][1]
        data[i - 1] = (FREE_SPACE, length)
        del data[i]
    else:
        data[i] = (FREE_SPACE, length)

    # if i < len(data) - 1 and data[i + 1][0] == FREE_SPACE:
    #     data[i + 1] = (FREE_SPACE, data[i + 1][1] + length)
    #     if delete: del data[i]
    # elif i > 0 and data[i - 1][0] == FREE_SPACE:
    #     data[i - 1] = (FREE_SPACE, data[i - 1][1] + length)
    #     if delete: del data[i]
    # else:
    #     data[i] = (FREE_SPACE, length)


def core(disk_map, fragment):
    next_id = 0
    data = []  # [(char, len)]
    for i in range(0, len(disk_map), 2):
        block_len = int(disk_map[i])
        if fragment:
            data += [(next_id, 1)] * block_len
        else:
            data.append((next_id, block_len))

        if i < len(disk_map) - 1:
            free_space = int(disk_map[i + 1])
            if free_space > 0:
                if fragment:
                    data += [(FREE_SPACE, 1)] * int(free_space)
                else:
                    data.append((FREE_SPACE, int(free_space)))

        next_id += 1
    target_id = next_id - 1
    log(data)
    log(format_disk(data))
    log()
    while target_id >= 0:
        curr_id_idx = find_next_id(data, len(data) - 1, target_id)
        id_data = data[curr_id_idx]
        id_val, id_len = id_data
        log(f'attempting to swap {str(id_val) * id_len}')

        free_idx = find_next_free(data, 0, curr_id_idx, id_len)
        if free_idx != -1:
            free_data = data[free_idx]
            _, free_len = free_data
            log(f'swapping with free spot at {free_idx} of len {free_len}')
            rem = free_len - id_len
            if rem == 0:
                # just swap
                merge_free(data, curr_id_idx, free_len)
                data[free_idx] = id_data
            else:
                # reduce len of free slot
                data[free_idx] = (FREE_SPACE, rem)

                # set space where id was to empty
                merge_free(data, curr_id_idx, id_len)

                # insert id data where the free spot was
                data.insert(free_idx, id_data)

            log(data)
            log(format_disk(data))
        else:
            log('no swap found')

        target_id -= 1
        log()
    log(data)
    log(format_disk(data))

    print(data)
    for a, b in itertools.pairwise(data):
        assert a[0] != b[0]

    return checksum(format_disk(data))


def part1(name):
    return core(process_file(name), True)


def part2(name):
    return core(process_file(name), False)


def process_file(name):
    with open(name) as file:
        content = file.read()
        return content


"""
Output
"""

print()
print(f'[Part 1] Test Result: {part1(test_file)}')
print(f'[Part 1] Real Result: {part1(input_file)}')
print(f'[Part 2] Test Result: {part2(test_file)}')
print(f'[Part 2] Real Result: {part2(input_file)}')
