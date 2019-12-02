import math

filepath = 'input.txt'

total = 0

with open(filepath) as fp:
    for line in (fp):
        num = int(line.strip("\n"))
        total += (math.floor(num/3)-2)

print(total)