import numpy as np

# open file and split into lines
with open('blocks.txt') as f:
    lines = f.readlines()
    
# go through each in list
for p in lines:
    # split by whitespace
    bank = p.split()
    # convert to int
    bank = map(int, bank)

# number of times looped
t = 0
# store array of seen arrays
seen = np.vstack([bank])

# length of the bank
l = len(bank)

# start without a match
match = False
# end when you get a match
while (match==False):
    # find largest value in bank
    big = max(bank)
    # store the value that is getting redistributed
    redist = big
    # store index of the biggest number
    # (whichever one comes first in the list)
    i = bank.index(big)
    # remove all blocks from that bank
    bank[i]=0

    # until you've redistributed everything
    while (redist > 0):
        # do next unless it's at the end
        if ((i+1)<l):
            i=i+1
        # then loop to beginning instead
        else:
            i=0
        # incease the block by 1
        bank[i] = bank[i]+1
        # reduce the value that is getting redistributed
        redist = redist-1
    
    # append new bank to list of seen values
    seen = np.vstack([seen,bank])
    
    # detects when a value has been seen before
    '''
    # don't need to do this way because I'm only comparing if last has been seen before
    # don't need to detect every possible combination
    x=0
    while(x<len(seen)):
        # start comparing against the next
        y=x+1
        while(y<len(seen)):
            # detect when all elements of the arrays match
            if((seen[x] == seen[y]).all()):
                # break when true
                match = True
            y=y+1
        x=x+1
    '''
    x=0
    # skip the last one because that's 'bank'
    while(x<len(seen)-1):
        # detect when all elements of the arrays match
        if((seen[x] == bank).all()):
            # break when true
            match = True
            # x is first occurance
            # length-1 is last occurance (offsetting the index of 0)
            print "Cycles between same state:", (len(seen)-1)-x
            
        x=x+1
    
    # increase times through loop
    t=t+1
    #print t
print "Times through loop:",t