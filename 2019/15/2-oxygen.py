import random

# Accept a movement command via an input instruction.
north = 1
south = 2
west = 3
east = 4
# Send the movement command to the repair droid.
# Wait for the repair droid to finish the movement operation.
# Report on the status of the repair droid via an output instruction.
# 0: The repair droid hit a wall. Its position has not changed.
unsuccessful = 0
# 1: The repair droid has moved one step in the requested direction.
successful = 1
# 2: The repair droid has moved one step in the requested direction; its new position is the location of the oxygen system.
complete = 2

# for drawing the area:
droid = 'D'
wall = '#'
valid = '.'

# create the ship's map array, filling it with None
size = 50
ship = [[None for i in range(size)] for j in range(size)]

# starting position (in the middle, //= not a float)
px = size//2
py = size//2

# desired position
dx, dy = px, py

# start at the center
ship[py][px] = valid

# count number of valid positions in the map
def countMoves(m):
    numberOfMoves = 0
    for line in m:
        for l in line:
            if(l == valid):
                numberOfMoves+=1
    return numberOfMoves

# pretty print the map
def printShip(m):
    global ship, dx, dy, px, py
    for y, line in enumerate(m):
        for x, l in enumerate(line):
            # change the way things are displayed
            if(l == None):
                l=' '
            if((y == size//2) and (x == size//2)):
                l = '*'
            if((y == py) and (x == px)):
                l = droid
            print(l, end =" ")
        print()
    print("-"*size)

# return a direction to move
def moveDroid():
    global ship, dx, dy, px, py

    # an array filled with the four directions in a random order
    random_directions = random.sample(range(1, 5, 1), 4)

    # try each direction
    for direction in random_directions:
        # if the next tile in that direction is unexplored,
        # then move there
        if (direction == north):
            if(ship[py+1][px] != wall):
                #print("Try north")
                dy = py+1
                return north
        elif(direction == east):
            if(ship[py][px+1] != wall):
                #print("Try east")
                dx = px+1
                return east
        elif(direction == south):
            if(ship[py-1][px] != wall):
                #print("Try south")
                dy = py-1
                return south
        elif(direction == west):
            if(ship[py][px-1] != wall):
                #print("Try west")
                dx = px-1
                return west
    
    print("Droid is stuck!")

numberOfMoves = 0

foundOxygenSystem = False

# see where the Droid is
def checkDroidStatus(a):
    global ship, dx, dy, px, py, numberOfMoves, foundOxygenSystem
    if(a == unsuccessful):
        #print("Unsuccessful")
        # mark desired position as invalid
        ship[dy][dx] = wall
        # reset desired position
        dx, dy = px, py
    elif(a == successful):
        #print("Successful")
        # for part 2, we don't want to start counting until we find the Oxygen System
        if(foundOxygenSystem):    
            # mark position as valid if it was previously undiscovered
            if (ship[dy][dx] == None):
                ship[dy][dx] = valid
            # otherwise moving back into a valid position
            # so make the last position invalid
            elif(ship[dy][dx] == valid):
                ship[py][px] = None

            # how many moves did it take to get here?
            moves = countMoves(ship)

            # get the furthest distance
            if (moves > numberOfMoves):
                numberOfMoves = moves
                print("Number of moves:", moves)

                # print map to show status
                printShip(ship)
        
        # update current position
        px, py = dx, dy
    # complete means we found the oxygen system,
    # so start counting from that point    
    elif(a == complete):
        foundOxygenSystem = True

        # update current position
        px, py = dx, dy

# relative base
relativeBase = 0

intcode =[]
with open("intcode.txt", "r") as fp:
    for line in (fp):
        instructions = line.split(",")

# convert all numbers to int
instructions = [int(x) for x in instructions]

# append a bunch of stuff to instructions so it doesn't get overrun
for i in range(800):
    instructions.append(0)

# current instruction pointer
ip = 0

# end at 99
while(instructions[ip] != 99):
    # current op code (lowest 2 digits)
    i = instructions[ip]%100
    
    # get mode of each parameter
    # // does floor division (no floats)
    # %10 only gets that digit
    mode1 = (instructions[ip]//  100)%10
    mode2 = (instructions[ip]// 1000)%10
    mode3 = (instructions[ip]//10000)%10

    if (mode1 == 0):
        try:
            a = instructions[instructions[ip+1]]
        except:
            a = None
    elif(mode1 == 1):
        try:
            a = instructions[ip+1]
        except:
            a = None
    elif (mode1 == 2):
        try:
            a = instructions[instructions[ip+1]+relativeBase]
        except:
            a = None
    else:
        print("Mode1 Error")

    if (mode2 == 0):
        try:
            b = instructions[instructions[ip+2]]
        except:
            b = None
    elif(mode2 == 1):
        try:
            b = instructions[ip+2]
        except:
            b = None
    elif (mode2 == 2):
        try:
            b = instructions[instructions[ip+2]+relativeBase]
        except:
            b = None
    else:
        print("Mode2 Error")

    if (mode3 == 0):
        try:
            c = 0
        except:
            c = None
    elif(mode3 == 1):
        try:
            # issue
            print("Mode3==1 not accounted for!")
            break
            #c = instructions[ip+3]
        except:
            c = None
    elif (mode3 == 2):
        try:
            c = relativeBase
        except:
            c = None
    else:
        print("Mode3 Error")

    #if(mode3):
    #    print(instructions[ip], i, (mode1, mode2, mode3), (a, b), relativeBase)
    #print( i, (a, b), relativeBase)
    #print(instructions)

    if(i==1):
        instructions[instructions[ip+3]+c] = a+b

        ip += 4
    elif(i==2):
        instructions[instructions[ip+3]+c] = a*b

        ip += 4
    elif(i==3):
        # take an input and store it at address given by parameter
        if (mode1 == 0):
            instructions[instructions[ip+1]] = moveDroid()
        elif(mode1 == 1):
            instructions[ip+1] = moveDroid()
        elif (mode1 == 2):
            instructions[instructions[ip+1]+relativeBase] = moveDroid()
        ip += 2
    elif(i==4):
        # outputs the value of its only parameter
        #outputValue = a
        checkDroidStatus(a)
        #print("Output at", ip, "is", a)
        ip += 2
    elif(i==5):
        # jump if true
        if (a != 0):
            ip = b
        else:
            ip += 3
    elif(i==6):
        # jump if false
        if (a == 0):
            ip = b
        else:
            ip += 3
    elif(i==7):
        # less than
        instructions[instructions[ip+3]+c] = int(a<b)

        ip+=4
    elif(i==8):
        # equals
        instructions[instructions[ip+3]+c] = int(a==b)

        ip+=4
    elif(i==9):
        # adjusts the relative base by the value of its only parameter
        relativeBase += a
        ip += 2
    else:
        print("ERROR")
