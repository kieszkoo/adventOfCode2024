import re

program = open("day3.txt").read()

mul_pattern = r"mul\((\d+),\s*(\d+)\)"
control_pattern = r"do\(\)|don't\(\)"

enabled = True
total_sum = 0

tokens = re.split(f"({control_pattern})", program)
print(tokens)
for token in tokens:
    token = token.strip()
    if token == "do()":
        enabled = True
    elif token == "don't()":
        enabled = False
    else:
        # Check for mul instructions in the token if mul is enabled
        mul_matches = re.findall(mul_pattern, token)
        for x, y in mul_matches:
            if enabled:
                total_sum += int(x) * int(y)

print(total_sum)

# Sample input string from the image

# Evaluate the enabled multiplications and print the result
