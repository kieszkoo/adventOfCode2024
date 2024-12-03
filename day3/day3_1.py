import re

def mul(x, y):
    return x * y

pattern = r"mul[(][0-9]{1,3},[0-9]{1,3}[)]"
functions = []
sum = 0

with open("day3.txt", "r") as file:
    for line in file:
        match = re.findall(pattern, line)
        functions.append(match)

for i in functions:
    for function in i:
        sum += eval(function)

print(sum)
