# the X and Y positions to start the test
# it can't be smaller than this because it needs to fit a 100 x 100 square
x = 101
y = 101

# to switch between returning X and Y
returnXorY = 0

# when the first point is valid, test the second point
testSecondPoint = False

# return a movement instruction
def moveDrone():
    global x, y, returnXorY, testSecondPoint

    # every other movement is a different position
    # X, then Y, then repeat
    returnValue = None
    if(returnXorY%2 == 0):
        if (testSecondPoint == False):
            returnValue = x
        else:
            # test second point's X
            # index of 99 is 100 locations away (starting at 0)
            returnValue = x + 99
            print("Second point: (", returnValue, ", ", end='')
        #print('('+str(returnValue)+', ', end='')
        x+=1
    else:
        if (testSecondPoint == False):
            returnValue = y
        else:
            # test second point's Y
            returnValue = y - 99 + 1
            print(returnValue, ") ", end='')
            # after testing second point, go back a couple on X and count Y up once
            x-=5
            y+=1
    returnXorY+=1

    return returnValue

def beamOrNoBeam(o):
    global x, y, testSecondPoint
    #print((x,y))

    # find a valid first point
    if (testSecondPoint == False):
        if (o == 1):
            print("First point:", (x,y+1), "", end='')
            testSecondPoint = True
        #else:
        #    print("Tested:", (x,y))
    else:
        print("Valid?", o)
        # reset flag
        testSecondPoint = False
        if (o == 1):
            # add 4 to counteract the -5 and 1 loop
            print(((x+4)*10000)+(y-99))
            exit()

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

    # at the end, exit
    # X times Y times 2 for alternating between the two using returnXorY
    #if(returnXorY == size*size*2):
    #    exit()