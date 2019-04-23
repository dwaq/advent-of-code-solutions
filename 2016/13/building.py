import sys

inp = 10

# http://stackoverflow.com/a/6667288/7564623
w, h = 8, 5;
Matrix = [[0 for x in range(w)] for y in range(h)] 

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
    #sys.stdout.write(str(y))
    #sys.stdout.write(' ')
    for x in range(10):
        # prints the number
        #sys.stdout.write(str(x))
        Matrix[x][y] = (parity_brute_force(form(x, y) + inp))

for y in range (7):
    sys.stdout.write(str(y))
    sys.stdout.write(' ')
    for x in range(10):
        sys.stdout.write(str(Matrix[x][y]))

        