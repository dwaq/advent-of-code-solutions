# open file and split into lines
with open('ins.txt') as f:
    lines = f.readlines()

# where to store all registers
regs = {}

# init all regs to 0
for l in lines:
    # split by spaces
    s = l.split()
    
    # add register to list and set to 0
    regs[s[0]] = 0

# store the highest value seen
highest = 0

# used when condition is correct
# will increment or decrement the register by the value
def do_instruction(s):
    register = s[0]
    direction = s[1]
    value = int(s[2])
    
    # add
    if (direction == "inc"):
        regs[register] = regs[register] + value
    # subtract
    else:
        regs[register] = regs[register] - value

# now let's do some math
for l in lines:
    # split by spaces
    s = l.split()
    
    # first and second values to compare
    x = regs[s[4]]  # value of the variable stated
    y = int(s[6])
    
    #print regs
    
    # do math based on operator
    # and if True, will do the operation requested
    if (s[5] == '>'):
        if (x > y):
            do_instruction(s)
    if (s[5] == '<'):
        if (x < y):
            do_instruction(s)
    if (s[5] == '=='):
        if (x == y):
            do_instruction(s)
    if (s[5] == '>='):
        if (x >= y):
            do_instruction(s)
    if (s[5] == '<='):
        if (x <= y):
            do_instruction(s)
    if (s[5] == '!='):
        if (x != y):
            do_instruction(s)
    
    # current register after doing math
    newvalue = regs[s[0]]
    # if it's higher than anything before it
    if (newvalue > highest):
        # store it as the highest seen
        highest = newvalue
    
#print
print "Largest value ever:", highest