instructions = []
num_lines = 0

reg = {'a':0, 'b':0, 'c':0, 'd':0}

# open file
with open('input.txt', 'rb') as f:
    # break into pieces
    for line in f:
        # strip the newline and append
        instructions.append(line.strip(']\n').split(' '))
        # count number of lines in file
        num_lines = num_lines + 1
        
#print instructions

# loop through each instruction
#for i in instructions:
l = 0
while (l < num_lines):
    i = instructions[l]
    #print i
    
    if i[0] == 'cpy':
        # handle copying between registers
        if ((i[1] >= 'a') and (i[1] <= 'd')):
            reg[i[2]] = reg[i[1]]
        # handle copying an int
        else:
            reg[i[2]] = int(i[1])
        l = l + 1
    elif i[0] == 'inc':
        reg[i[1]] = int(reg[i[1]]) + 1
        l = l + 1
    elif i[0] == 'dec':
        reg[i[1]] = int(reg[i[1]]) - 1
        l = l + 1
    elif i[0] == 'jnz':
        if (reg[i[1]] != 0):
            # increase loop number by that many
            l = l + int(i[2])
        else:
            # else, just go to next one
            l = l + 1
    else:
        print "ERROR"
        
    #print reg

print "Final answer:", reg['a']