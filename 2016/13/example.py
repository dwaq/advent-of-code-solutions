import sys

inp = 10

# http://stackoverflow.com/a/6667288/7564623
w, h = 20, 20;
Matrix = [[0 for x in range(w)] for y in range(h)] 

# postions
px, py = 1, 1

# end point
ex, ey = 7, 4

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
for y in range (7):
    for x in range(10):
        Matrix[x][y] = (parity_brute_force(form(x, y) + inp))

# this correctly prints the building
def printBuilding():
    print
    for y in range (7):
        sys.stdout.write(str(y))
        sys.stdout.write(' ')
        for x in range(10):
            sys.stdout.write(str(Matrix[x][y]))
        print

def move(px, py):
    # down
    if (py < ey):
        if (Matrix[px][py+1] == '.'):
            return px, py+1
    # up
    if (py > ey):
        if (Matrix[px][py-1] == '.'):
            return px, py-1
    
    # right
    if (px < ex):
        if (Matrix[px+1][py] == '.'):
            return px+1, py
    # left
    if (px > ex):
        if (Matrix[px-1][py] == '.'):
            return px-1, py
            
    # if you're hear, just randomly move
    # down for example
    if (Matrix[px][py+1] == '.'):
            return px, py+1


# START, try 12 steps
for s in range(12):
    print "\nstep",s,
    Matrix[px][py] = 'O'
    printBuilding()
    px, py = move(px, py)
    steps = steps + 1
    if ((px == ex) and (py == ey)):
        print steps
        break