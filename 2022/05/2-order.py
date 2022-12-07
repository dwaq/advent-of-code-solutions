txt = open("input.txt", "r").readlines()

# get the length of the picture to later split into crates
pic_len = len(txt[0])
# get the height of the picture (hardcoded)
pic_h = 9
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


# take temporary data and format it
for t in range(len(temp)):
    #print(temp[t])
    # print(t)
    # generate keys
    if t == 0:
        for x in temp[t]:
            # print(x)
            crates[int(x)] = []
        # print(crates)
    # fill keys with data
    else:
        # print(temp[t])
        for i in range(stacks_n):
            i = int(i)
            if (temp[t][i] != ''):
                crates[i+1].append(temp[t][i])


# now a dict with the column # as key, and stacks as arrays
#print(crates)



# loop through instructions
for l, line in enumerate(txt):
    # skip the picture
    if (l > pic_h):
        # instruction
        ins = line.strip('\n').split(' ')
        # number of crates to move
        num = int(ins[1])
        # source
        s = int(ins[3])
        # destination
        d = int(ins[5])
        
        #print('\n', num, s, d)

        # crates are moved as chunks
        # start at the bottom of the stack and copy each one - keeps them in order
        for n in reversed(range(num)):
            # copy bottom item of source index to destination
            #print(crates[s][-1*n])
            crates[d].append(crates[s][-1-n])
        # remove last num items of source
        crates[s] = crates[s][:-num]

        #print(crates)

# print top of each stack
for x in range(1,10):
    print(crates[int(x)][-1], end ="")