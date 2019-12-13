# tiles
empty = 0
wall = 1
block = 2
paddle = 3
ball = 4

# create the screen array, filling it with empty (not needed)
size_x = 80
size_y = 24
screen = [[empty for i in range(size_x)] for j in range(size_y)]

# pretty print the screen
def printScreen(m):
    for line in m:
        for l in line:
            if(l==empty):
                l=' '
            elif(l==wall):
                l='▩'
            elif(l==block):
                l='▪'
            elif(l==paddle):
                l='▬'
            elif(l==ball):
                l='◍'

            print(l, end =" ")
        print()

# count number of pixels that were set as a block
# AKA not empty
def countScreen(m):
    paintedPixels = 0
    for line in m:
        for l in line:
            if(l==block):
                paintedPixels+=1
    return paintedPixels

# postions
px = None
py = None

# every other output does a different task
# so count each to understand where to go
outputCounter = 0

# set the x and y position and the tile
def drawScreen(value):
    # use global values
    global outputCounter, py, px

    # three inputs to an instruction
    sequence = outputCounter % 3

    # first is x position
    if (sequence == 0):
        px = value
    # second is y position
    elif (sequence == 1):
        py = value
    # third is tile
    elif (sequence == 2):
        screen[py][px] = value
    else:
        print("Issue with sequence")

    outputCounter += 1

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
        printScreen(screen)
        direction = input()
        print("input")
        '''
        # take an input and store it at address given by parameter
        if (mode1 == 0):
            instructions[instructions[ip+1]] = getPanelColor()
        elif(mode1 == 1):
            instructions[ip+1] = getPanelColor()
        elif (mode1 == 2):
            instructions[instructions[ip+1]+relativeBase] = getPanelColor()
        ip += 2
        '''
    elif(i==4):
        # outputs the value of its only parameter
        #outputValue = a
        drawScreen(a)
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

#print(instructions)
#print("Relative Base:", relativeBase)
#print("Output Value:", outputValue)

print("Block tiles:", countScreen(screen))