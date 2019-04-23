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
    # North
    if (dir == 0):
        # increease X
        pos[0] = pos[0] + length
    # East
    if (dir == 1):
        # increease Y
        pos[1] = pos[1] + length
    # South
    if (dir == 2):
        # decrease X
        pos[0] = pos[0] - length
    # West
    if (dir == 3):
        # decrease Y
        pos[1] = pos[1] - length

    return pos

# loop through dir
for d in data:
    print d
    # turn
    dir = turn(dir, d[0])
    #printDir()
    # move (could be more than 1 character)
    pos = move(dir, pos, d[1:])
    print pos

# go in straight lines to get distance
# don't do shortest distance
#distance = math.sqrt((pos[0]*pos[0]) + (pos[1]*pos[1]))
distance = abs(pos[0]) + abs(pos[1])
print "total distance:",distance