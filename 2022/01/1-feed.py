txt = open("input.txt", "r").readlines()
#print(txt)

# store each elf's calories
elf = []
count = 0

for line in txt:
    # when not a newline
    if (line != '\n'):
        # add that to the elf's count
        count += int(line)
    else:
        # put that elf's count into the list
        elf.append(count)
        # reset count
        count = 0

#print(elf)
# the elf with the most calories
print(max(elf))
#print(elf.index(max(elf)))