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

#print layers

'''
make formula that counts when each is not at zero
and we can pass
keep in mind that the one at position x is x places further ahead than position 0
'''

def calculatePosition(time):
    
    # default to True, will change if ever false
    madeItThrough = True
    
    # go through each layer
    for layer in layers:
    
        # scanner is at position 0 when the time is a mutiple of this
        hits = (2+(layers[layer]-2))
        
        position = layer+time+1
    
        # 
        try:
            atZero = position%hits
        except ZeroDivisionError:
            #print "divided by 0"
            atZero = 0
        
        # if any are zero, it didn't make it though
        if (atZero == 0):
            madeItThrough = False
            
        print layer, ":", layers[layer], "time:", time, "\thits:", hits, "position:", position, "\tatZero:", atZero, madeItThrough
    
    return madeItThrough
    
x = 0
while(x < 13):
    
    madeItThrough = calculatePosition(x)
    x=x+1

    print x, madeItThrough
    print 