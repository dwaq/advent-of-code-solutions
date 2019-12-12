# colors
empty = None
black = 0
white = 1

# create the hull array, filling it with None
size = 1500
hull = [[empty for i in range(size)] for j in range(size)]

# pretty print the hull
def printHull(m):
    for line in m:
        for l in line:
            if(l==empty):
                l=' '
            elif(l==black):
                l='.'
            elif(l==white):
                l='#'
            print(l, end =" ")
        print()

# count number of panels that were painted
# AKA not empty
def countHull(m):
    paintedPanels = 0
    for line in m:
        for l in line:
            if(l!=empty):
                paintedPanels+=1
    return paintedPanels

# starting position (in the middle, //= not a float)
px = size//2
py = size//2

# direction the robot is facing (starts up)
d = "U"

# start on a white panel
hull[py][px] = white

# returns the color of the panel we're on
def getPanelColor():
    # only white if it's actually been painted white
    if (hull[py][px] == white):
        return white
    # otherwise it's painted black
    # (which could technically be empty or black)
    else:
        return black

# every other output does a different task
# so count each to understand where to go
outputCounter = 0

# paint the current block the correct color
# rotate then move
def paintAndMoveRobot(value):
    # use global values
    global outputCounter, py, px, d

    # even numbers paint
    if (outputCounter%2 == 0):
        hull[py][px] = value
    
    # odd numbers move
    else:
        # left 90 degrees
        if (value == 0):
            if (d=="U"):
                d="L"
                px -= 1
            elif (d=="L"):
                d="D"
                py -= 1
            elif (d=="D"):
                d="R"
                px += 1
            elif (d=="R"):
                d="U"
                py += 1
            else:
                print("Issue with left turn")
        # right 90 degrees
        else:
            if (d=="U"):
                d="R"
                px += 1
            elif (d=="R"):
                d="D"
                py -= 1
            elif (d=="D"):
                d="L"
                px -= 1
            elif (d=="L"):
                d="U"
                py += 1
            else:
                print("Issue with right turn")
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
        # take an input and store it at address given by parameter
        if (mode1 == 0):
            instructions[instructions[ip+1]] = getPanelColor()
        elif(mode1 == 1):
            instructions[ip+1] = getPanelColor()
        elif (mode1 == 2):
            instructions[instructions[ip+1]+relativeBase] = getPanelColor()
        ip += 2
    elif(i==4):
        # outputs the value of its only parameter
        #outputValue = a
        paintAndMoveRobot(a)
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

print("Painted panels:", countHull(hull))