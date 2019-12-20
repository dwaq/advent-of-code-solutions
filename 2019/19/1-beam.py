# The program uses two input instructions to request the X and Y position to which the drone should be deployed.
# Negative numbers are invalid and will confuse the drone; all numbers should be zero or positive.

# Then, the program will output whether the drone is stationary (0) or being pulled by something (1).

# create an array for the beam's pattern, filling it with None
size = 50
picture = [[None for i in range(size)] for j in range(size)]

# the X and Y positions to test
x = 0
y = 0

# to switch between returning X and Y
returnXorY = 0

# return a movement instruction
def moveDrone():
    global x, y, returnXorY, size

    # every other movement is a different position
    # X, then Y, then repeat
    returnValue = None
    if(returnXorY%2 == 0):
        returnValue = x
        #print('('+str(returnValue)+', ', end='')
        x+=1
    else:
        returnValue = y
        #print(str(returnValue)+'): ',end='')
        # at the end of X, reset it and count Y up
        if (x == size):
            x=0
            y+=1
    returnXorY+=1

    return returnValue

# set location to output of drone
pointsAffected = 0
def beamOrNoBeam(o):
    #print(o)
    global pointsAffected
    # just add location (1 when seen) to count
    pointsAffected += o
    #global picture, x, y
    #picture[y][x] = o

# reset and repeat machine
# because need to run fresh instructions for each position
while(True):
    # relative base
    relativeBase = 0

    intcode =[]
    with open("intcode.txt", "r") as fp:
        for f in (fp):
            instructions = f.split(",")

    # convert all numbers to int
    instructions = [int(x) for x in instructions]

    # append a bunch of stuff to instructions so it doesn't get overrun
    for i in range(8000):
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
        #print(instructions[ip], i, (mode1, mode2, mode3), (a, b), relativeBase)
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
                instructions[instructions[ip+1]] = moveDrone()
            elif(mode1 == 1):
                instructions[ip+1] = moveDrone()
            elif (mode1 == 2):
                instructions[instructions[ip+1]+relativeBase] = moveDrone()
            ip += 2
        elif(i==4):
            # outputs the value of its only parameter
            #outputValue = a
            beamOrNoBeam(a)
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

    # at the end, print the count
    # X times Y times 2 for alternating between the two using returnXorY
    if(returnXorY == size*size*2):
        print("Points affected:", pointsAffected)
        exit()