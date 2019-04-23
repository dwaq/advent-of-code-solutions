import sys
import random

inp = 1358

# http://stackoverflow.com/a/6667288/7564623
w, h = 50, 50;
Matrix = [[0 for x in range(w)] for y in range(h)] 

# postions
#global px
#global py
px, py = 1, 1

# end point
ex, ey = 31, 39

# number of steps to get there
steps = 0

# http://p-nand-q.com/python/algorithms/math/bit-parity.html
def parity_brute_force(x):
    bit = 0
    num_bits = 0
    while x:
        bitmask = 1 << bit
        bit += 1
        if x & bitmask:
            num_bits += 1
        x &= ~bitmask

    #return num_bits % 2
    if (num_bits % 2):
        return '#'
    else:
        return '.'

def form(x, y):
    return x*x + 3*x + 2*x*y + y + y*y

# this correctly generates the building
for y in range (45):
    for x in range(45):
        Matrix[x][y] = (parity_brute_force(form(x, y) + inp))

# this correctly prints the building
def printBuilding():
    print
    for y in range (45):
        sys.stdout.write(str(y))
        sys.stdout.write(' ')
        for x in range(45):
            sys.stdout.write(str(Matrix[x][y]))
        print


def move():
    r = random.randint(0, 3)
    
    # down
    if (r == 0):
        if (Matrix[px][py+1] == '.'):
            global py 
            py = py+1
    # up
    elif (r == 1):
        if (Matrix[px][py-1] == '.'):
            global py 
            py= py-1
    
    # right
    elif (r == 2):
        if (Matrix[px+1][py] == '.'):
            global px 
            px= px+1
    # left
    elif (r == 3):
        if (Matrix[px-1][py] == '.'):
           global px 
           px= px-1
    
    # if you're here, it didn't work, try again
    else:
        return move()


# START
for tr in range(10000):
    for s in range(1000):
        #print "\nstep",s,
        Matrix[px][py] = 'O'
        #printBuilding()
        move()
        steps = steps + 1
        if ((px == ex) and (py == ey)):
            print steps
            printBuilding()
            break