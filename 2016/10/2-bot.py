instructions = []

# open file
with open('input.txt', 'rb') as f:
    # break into pieces
    for line in f:
        # strip the newline and append
        instructions.append(line.strip(']\n'))
        
#print instructions

# what bots are holding which values
data = {}
# giving instructions once bot holds 2 data
giving = {}
# the outputs and which values are stored there
output = {}


# evaluate the give instuction's data
def giveToBot(bot, value):
    # convert inputs to integers
    bot = int(bot)
    value = int(value)
    
    # add value to bot
    # http://stackoverflow.com/a/20585947
    data.setdefault(bot, [])
    data[bot].append(value)
    
    # check if it contains 2 and go back?

def splitToBots(bot, who_low, low, who_high, high):
    #print bot, low, high
    # convert inputs to integers
    bot = int(bot)
    low = int(low)
    high = int(high)
    
    # add value to bot
    # http://stackoverflow.com/a/20585947
    giving.setdefault(bot, [])
    giving[bot].append(who_low)
    giving[bot].append(low)
    giving[bot].append(who_high)
    giving[bot].append(high)

# understand instruction:
# bot gets value
def getValues(instruction):
    #print instruction
    # split instruction using spaces
    i = instruction.split(' ')
    if i[0] == "value":
        giveToBot(i[5], i[1])
    elif i[0] == "bot":
        # there's an instuction for each bot
        splitToBots(i[1], i[5], i[6], i[10], i[11])

# loop though once to get initial values
for i in instructions:
    getValues(i)

# loop through again to give values
# this puts it into a infinite loop; but does give you the correct answer
while (len(output) < 21):
    print len(output)
    # go through each data looking for the one that has 2 data
    for d in data.keys():
        # contains 2 data
        if (len(data[d]) == 2):
            #shorthand
            gd = giving[d]

            #print d, data[d], gd
            
            # REAL SOLUTION RIGHT HERE
            if data[d] == [61, 17]:
                print "BOT", d
            
            # get low and high values
            low = min(data[d][0], data[d][1])
            high = max(data[d][0], data[d][1])
            
            # apply giving formula
            # (decide to give to bot or output)

            # low value
            if gd[0] == "bot":
                try:
                    data[gd[1]].append(low)
                except:
                    data.setdefault(gd[1], [])
                    data[gd[1]].append(low)
            elif gd[0] == "output":
                try:
                    output[gd[1]].append(low)
                except:
                    output.setdefault(gd[1], [])
                    output[gd[1]].append(low)
            
            # high value
            if gd[2] == "bot":
                try:
                    data[gd[3]].append(high)
                except:
                    data.setdefault(gd[3], [])
                    data[gd[3]].append(high)
            elif gd[2] == "output":
                try:
                    output[gd[3]].append(high)
                except:
                    output.setdefault(gd[3], [])
                    output[gd[3]].append(high)
            
            # remove values from original bot
            data[d].remove(low)
            data[d].remove(high)
            
print
print "data:", data
print "giving:", giving
print "output", output
print
print "answer to part2:", output[0][0]*output[1][0]*output[2][0]

'''
# printing how many data's have 2 keys
for d in data:
    print data[d], '\t', len(data[d])
'''
