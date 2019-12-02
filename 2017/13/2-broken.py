# open file and split into lines
with open('input.txt') as f:
    lines = f.readlines()

# current layer
cl = 0

# where to store all layers
layersFRESH = {}

# loop through them all and make nice data
for l in lines:
    # split by seperator
    l = l.split(': ')
    # convert to integers
    l = map(int, l)
    # add data to layersFRESH by key
    layersFRESH[l[0]] = l[1]

# current position of scanners
# make a copy
spFRESH = layersFRESH.copy()
# edit to start them all at 0
for s in spFRESH:
    spFRESH[s] = 0

# make a dict for direction
directionFRESH = spFRESH.copy()
# edit to make them all 1 (increase)
for d in directionFRESH:
    directionFRESH[d] = 1


# the scanner position zig zags up and down
def moveScanners():
    # loop through each
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

# total delay
delay = 0

# count of steps
steps = 0

# highest key is the number of layers
num_layers = max(layersFRESH)

# keep trying until we break out
bo = 0
while(bo < 12):

    # set to defaults at the beginning of the loop
    layers = layersFRESH.copy()
    sp = spFRESH.copy()
    direction = directionFRESH.copy()

    move = 0
    while(move < bo):
        
        # loop through each
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
        
        move +=1

    found = 0

    # go through each layer
    while (steps <= num_layers):
    
        # skip a layer if there's not a scanner there
        if steps not in layers:
            waste = 0
            #print steps, "not found"
        # else check the position
        else:
            # compare scanner position with current position
            # current position is always 0 (we're at the top)
            if(sp[steps] == 0):
                print "found at", 
                found = 1
                #break
            
                print steps
                print sp
                print layers
                print
                
        
        # loop through each
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

    if (found == 0):
        print "DIDNT FIND", bo
    print bo
    bo +=1

print "total delay:", bo
# 1300 is the correct answer