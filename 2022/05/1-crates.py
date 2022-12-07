txt = open("input.txt", "r").readlines()

# get the length of the picture to later split into crates
pic_len = len(txt[0])
# get the height of the picture (hardcoded)
pic_h = 4
# a stack is 4 chars wide
crate_len = 4
# number of stacks
stacks_n = pic_len//crate_len

temp = []
crates = {}
# print(crates)


# loop through the picture from bottom to top
for h in reversed(range(pic_h)):
    # current line text
    line = txt[h]

    # split line into stacks
    stacks = [ line[i:i+crate_len].strip('\n\[ ]') for i in range(0, pic_len, crate_len) ]

    #print(stacks)

    # for c in range(len(crates)):
    #     crates[c].append(stacks[c])
    temp.append(stacks)

for t in range(len(temp)):
    #print(temp[t])
    # print(t)
    # generate keys
    if t == 0:
        for x in temp[t]:
            # print(x)
            crates[int(x)] = []
    else:
        # print(temp[t])
        for i in range(stacks_n):
            if (temp[t][i] != ''):
                crates[i+1].append(temp[t][i])


# now a dict with the column # as key, and crates as arrays
print(crates)




# for line in txt:
#     # between the picture and the instructions is a newline
#     if (line == '\n'):
#         break