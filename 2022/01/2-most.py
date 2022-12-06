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

# remember the final elf
elf.append(count)

#print(elf)
sorted_elfs = (sorted(elf))
num = len(sorted_elfs)

print(sorted_elfs)

top3 = 0

for i in range(3):
    #print(sorted_elfs[num-1-i])
    top3 += sorted_elfs[num-1-i]


print(top3)