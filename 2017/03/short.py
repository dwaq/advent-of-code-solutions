import numpy as np

inp = 12

m = 8
Matrix = [[0 for x in range(m)] for y in range(m)] 

# throw number at x, y
def place(num):
    # reverse y so it makes sense to me
    Matrix[-y][x] = num

# start with a 1 in the middle
x = m/2
y = m/2
c = 1   # count
place(c)


l = 0 # level
n = 1 # max number on level
# solving for 289326
while ((n*n) < 26):
    # w is width
    w = n
    print "lvl:",l, "  wid:", w
    
    # lowest and highest number on level
    low = ((n-2)*(n-2))+1
    high = n*n
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
        place(c)
        # go up
        while (c < c1):
            c=c+1
            y=y+1
            place(c)
        # go left
        while(c < c2):
            c=c+1
            x=x-1
            place(c)
        # go down
        while (c < c3):
            c=c+1
            y=y-1
            place(c)
        # go right
        while(c < c4):
            c=c+1
            x=x+1
            place(c)


    # next level
    l = l+1
    # grows by 2 because top and bottom
    n = n+2
    
    print(np.matrix(Matrix))
    print


x1 = m/2
y1 = m/2
print 'The index of the origin is',(x1,y1)

# find location of value
# https://stackoverflow.com/a/6518412

to_find = 289326
x = [x for x in Matrix if to_find in x][0]

x2 = Matrix.index(x)
y2 = x.index(to_find)

print 'The index of', to_find, 'is',(x2,y2)

d = abs(x2-x1) + abs(y2-y1)

print "Distance is", d
# answer is 419