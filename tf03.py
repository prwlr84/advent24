from math import prod
from re import findall, sub
from tf03i import inputString

# 1
valid = findall(r"mul\((\d{1,3}),(\d{1,3})\)", inputString)
total = sum(prod(map(int, v)) for v in valid)
print('First:', total)

# 2
commands = findall("mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", inputString)
switch = True
valid = []
for command in commands:
    switch = False if "don't" in command else True if 'do' in command else switch
    if 'mul' in command and switch:
        valid.append(command)

total2 = sum([prod(list(map(int, sub("mul\((.*)\)", r'\1', v).split(',')))) for v in valid])
print('Second', total2)

# pattern = r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)"
# commands = findall(pattern, inputString)
#
# switch = True
# total = 0
#
# for cmd in commands:
#     if cmd == ('', '',):  # This happens for do() or don't()
#         raw = search(r"do\(\)|don't\(\)", inputString).group()
#         switch = raw == "do()"
#     elif all(cmd):  # Both numbers are present → it's a mul()
#         if switch:
#             nums = map(int, cmd)
#             total += prod(nums)
#
# print("Second", total)