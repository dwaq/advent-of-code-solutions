import math

filepath = 'input.txt'

total = 0

with open(filepath) as fp:
    for line in (fp):
        num = int(line.strip("\n"))

        while(num > 0):
            num = (math.floor(num/3)-2)

            if (num > 0):
                total += num

print(total)
