"""
The computer appears to be trying to run a program, but its memory (your puzzle input_b_full) is corrupted.
All of the instructions have been jumbled up!

It seems like the goal of the program is just to multiply some numbers.
It does that with instructions like mul(X,Y), where X and Y are each 1-3 digit numbers.
For instance, mul(44,46) multiplies 44 by 46 to get a result of 2024. Similarly, mul(123,4)
would multiply 123 by 4.

However, because the program's memory has been corrupted, there are also many invalid characters
that should be ignored, even if they look like part of a mul instruction.
Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.
"""
import re

regex_p1 = "mul\\(\\d+,\\d+\\)"
regex_p2 = "mul\\(\\d+,\\d+\\)|do\\(\\)|don't\\(\\)"

with open('./input') as file:
    product_sum = 0
    content = file.read()
    list = re.findall(regex_p2, content)
    enabled = True
    for pair in list:
        if pair == "do()":
            enabled = True
        elif pair == "don't()":
            enabled = False
        elif enabled:
            tokens = pair.split(',')
            a = int(tokens[0].split('(')[1])
            b = int(tokens[1].split(')')[0])
            product_sum += (a * b)
    print(product_sum)


