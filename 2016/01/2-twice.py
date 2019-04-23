import math

# open file
import csv
with open('input.txt', 'rb') as f:
    # break into pieces
    input = csv.reader(f, delimiter=',')
    for direction in input:
        # each piece
        data = direction
        #print dir
        
# list to store current position (x, y)
pos = [0, 0]
# store current direction
# 0 = North
# 1 = East
# 2 = South
# 3 = West
#     N
#     0
# W 3   1 E
#     2
#     S
dir = 0

def turn(dir, way):
    # turn right
    if (way == 'R'):
        dir = dir + 1
        # loop back around
        if (dir == 4):
            dir = 0
    # turn left
    if (way == 'L'):
        dir = dir - 1
        # loop back around
        if (dir == -1):
            dir = 3

    return dir
    
def printDir():
    if (dir == 0): print "North"
    if (dir == 1): print "East"
    if (dir == 2): print "South"
    if (dir == 3): print "West"
    
def move(dir, pos, length):
    length = int(length)
    print length
    # need to track every step we take to find the first point we cross
    l = 0
    while (l < length):
        # North
        if (dir == 0):
            # increease X
            pos[0] = pos[0] + 1
        # East
        if (dir == 1):
            # increease Y
            pos[1] = pos[1] + 1
        # South
        if (dir == 2):
            # decrease X
            pos[0] = pos[0] - 1
        # West
        if (dir == 3):
            # decrease Y
            pos[1] = pos[1] - 1
        
        # check if position has been hit before
        if (pos in all_pos):
            print "found!", pos
            getDistance()
            while(1):
                var = 0
        # add each location (value NOT reference) traveled to the list
        # http://stackoverflow.com/a/8744133
        all_pos.append(pos[:])
        print all_pos
        
        # increase l
        l = l + 1

    return pos

# keep a list of all positions visited
all_pos = []

# go in straight lines to get distance
# don't do shortest distance
#distance = math.sqrt((pos[0]*pos[0]) + (pos[1]*pos[1]))
def getDistance():
    distance = abs(pos[0]) + abs(pos[1])
    print "total distance:",distance

# loop through dir
for d in data:
    print d
    # turn
    dir = turn(dir, d[0])
    #printDir()
    # move (could be more than 1 character)
    pos = move(dir, pos, d[1:])
    print pos
