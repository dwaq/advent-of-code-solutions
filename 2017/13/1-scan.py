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

# make a dict for direction
direction = sp.copy()
# edit to make them all 1 (increase)
for d in direction:
    direction[d] = 1

# total severity
severity = 0

# count of steps
steps = 0

# highest key is the number of layers
num_layers = max(layers)

# go through each layer
while (steps <= num_layers):

    # skip a layer if there's not a scanner there
    if steps not in layers:
        print steps, "not found"
    # else check the position
    else:
        # compare scanner position with current position
        # current position is always 0 (we're at the top)
        if(sp[steps] == 0):
            print "found at", steps, "with depth", layers[steps]
            # increase severity
            severity += (steps * layers[steps])
        
        print steps
    print sp
    print layers
    print 
    
    # the scanner position zig zaps up and down
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

print "total severity:", severity
# 1300 is the correct answer