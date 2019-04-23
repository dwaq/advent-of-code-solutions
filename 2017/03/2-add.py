import numpy as np

m = 12
M = [[0 for x in range(m)] for y in range(m)] 

# throw number at x, y
def place(num):
    
    # find the first largest number
    # this is where the answer prints!!!
    # (first one is the answer)
    if(num >289326):
        #answer is 295229
        print num
        
    # reverse y so it makes sense to me
    M[-y][x] = num

# get value at location
def gv(x, y):
    return M[-y][x]

# start with a 1 in the middle
x = m/2
y = m/2
c = 1   # count
n = 1 # number to place 
place(c)


l = 0 # level
mn = 1 # max number on level
# solving for 289326
while ((mn*mn) < 100):
    # w is width
    w = mn
    print "lvl:",l, "  wid:", w
    
    # lowest and highest number on level
    low = ((mn-2)*(mn-2))+1
    high = mn*mn
    print "min:", low, "max:", high
    
    # level 0 doesn't work the same, so skip this math there
    if(l!=0):
        # corners
        c1 = low+(w-2)
        c2 = c1+(w-1)
        c3 = c2+(w-1)
        c4 = high
        print c1,c2,c3,c4
        
        c=c+1 # increase
        # first one is just to the right
        x=x+1
        # add these values
        # left, left-1up
        n= gv(x-1,y)+gv(x-1,y+1)
        place(n)
        # go up
        while (c < c1):
            c=c+1
            y=y+1
            #down, down-left, left, up-left
            n=gv(x,y-1)+gv(x-1,y-1)+gv(x-1,y)+gv(x-1,y+1)
            place(n)
        # go left
        while(c < c2):
            c=c+1
            x=x-1
            #right, down, down-right, down-left
            n=gv(x+1,y)+gv(x,y-1)+gv(x+1,y-1)+gv(x-1,y-1)
            place(n)
        # go down
        while (c < c3):
            c=c+1
            y=y-1
            #up, right-up, right, right-down
            n=gv(x,y+1)+gv(x+1,y+1)+gv(x+1,y)+gv(x+1,y-1)
            place(n)
        # go right
        while(c < c4):
            c=c+1
            x=x+1
            #left, left-up, up, up-right
            n=gv(x-1,y)+gv(x-1,y+1)+gv(x,y+1)+gv(x+1,y+1)
            place(n)


    # next level
    l = l+1
    # grows by 2 because top and bottom
    mn=mn+2
    
    #print(np.matrix(M))
    print
