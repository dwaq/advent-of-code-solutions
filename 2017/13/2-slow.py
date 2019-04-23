# open file and split into lines
with open('input.txt') as f:
    lines = f.readlines()

# current layer
cl = 0

# where to store all layers
layers = {}

# loop through them all and make nice data
for l in lines:
    # split by seperator
    l = l.split(': ')
    # convert to integers
    l = map(int, l)
    # add data to layers by key
    layers[l[0]] = l[1]

# current position of scanners
# make a copy
sp = layers.copy()
# edit to start them all at 0
for s in sp:
    sp[s] = 0

spKeep = sp.copy()

# make a dict for direction
direction = sp.copy()
# edit to make them all 1 (increase)
for d in direction:
    direction[d] = 1

dirKeep = direction.copy()

# total delay
delay = 3941460-10



# highest key is the number of layers
num_layers = max(layers)


while (delay < (3941460+10)):

    sp = spKeep.copy()
    #print "default sp ", sp
    direction = dirKeep.copy()
    #print "default dir", direction
    
    # increase by delay
    d = 0
    while (d<delay):
        # the scanner position zig zags up and down
        for s in sp:
            # add by direction
            # could be +1 or -1
            sp[s] += direction[s]
            
            # if at the top, go down
            if (sp[s] == (layers[s]-1)):
                direction[s] = -1
            # if at the bottom, go up
            # also check that we're heading downwards
            # or else you'll catch the inital state
            elif ((sp[s] == 0) and (direction[s] == -1)):
                direction[s] = +1
        
        # once more through loop
        d+=1
        
    #print d, "passes   ", sp
    
    found = 0
    
    # count of steps
    steps = 0
    
    # go through each layer
    while (steps <= num_layers):
    
        # skip a layer if there's not a scanner there
        if steps not in layers:
            whocares = 0
            #print steps, "not found"
        # else check the position
        else:
            # compare scanner position with current position
            # current position is always 0 (we're at the top)
            if(sp[steps] == 0):
                #print "found at", steps
                found = 1
            
            #print steps
        #print sp
        #print layers
        #print 
        
        # the scanner position zig zags up and down
        for s in sp:
            # add by direction
            # could be +1 or -1
            sp[s] += direction[s]
            
            # if at the top, go down
            if (sp[s] == (layers[s]-1)):
                direction[s] = -1
            # if at the bottom, go up
            # also check that we're heading downwards
            # or else you'll catch the inital state
            elif ((sp[s] == 0) and (direction[s] == -1)):
                direction[s] = +1
        
        # increase counter
        steps+=1
    
    #print "found:", found
    #print 
    
    if (found == 0):
        print "DIDNT FIND AT", d
        break
    
    # increase delay
    delay += 1

#print "total delay:", delay