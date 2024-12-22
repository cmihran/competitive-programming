def eval_line(allow_concat: bool, goal: int, curr_value: int, i: int, values: [int]) -> bool:
    # for each operator place, try + or * and see if it reaches the goal
    if i == len(values):
        return curr_value == goal

    adds = eval_line(allow_concat, goal, curr_value + values[i], i + 1, values)
    multiplies = eval_line(allow_concat, goal, curr_value * values[i], i + 1, values)
    concat = False if not allow_concat else eval_line(
        True,
        goal,
        int(str(curr_value) + str(values[i])),
        i,
        values[:i] + values[i + 1:]
    )
    return adds or multiplies or concat


def process_file(name: str, allow_concat: bool):
    total_sum = 0
    f = open(name)
    for line in f:
        goal, values = line.split(':')
        goal = int(goal)
        values = [int(x) for x in values.strip().split()]
        if eval_line(allow_concat, goal, values[0], 1, values):
            total_sum += goal
    return total_sum


print('Part 1:', process_file('input_b_full', False))
print('Part 2:', process_file('input_b_full', True))
