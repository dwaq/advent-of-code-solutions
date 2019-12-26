# they run a simplified assembly language called springscript.
# it can only remember at most 15 springscript instructions.
# The springdroid will move forward automatically, constantly thinking about whether to jump.
# Two registers are available: T, the temporary value register, and J, the jump register.
# If the jump register is true at the end of the springscript program, the springdroid will try to jump.
# Both of these registers start with the value false.
# Springdroids have a sensor that can detect whether there is ground at various distances in the direction it is facing;
# these values are provided in read-only registers.
# Your springdroid can detect ground at four distances: one tile away (A), two tiles away (B), three tiles away (C), and four tiles away (D).
# If there is ground at the given distance, the register will be true; if there is a hole, the register will be false.
# three instructions available in springscript:
# AND X Y sets Y to true if both X and Y are true; otherwise, it sets Y to false.
# OR X Y sets Y to true if at least one of X or Y is true; otherwise, it sets Y to false.
# NOT X Y sets Y to true if X is false; otherwise, it sets Y to false.
# The second argument (Y) needs to be a writable register (either T or J).
# The first argument (X) can be any register (including A, B, C, or D).

# store movement instructions from file
# each character as a new list item
moves = []
with open("movement2.txt", "r") as fp:
    for f in (fp):
        moves += list(f)

# convert each character from ASCII to int
moves = [ord(m) for m in moves]

# index of character to send
moveIndex = 0

# return a movement instruction
def moveDroid():
    global moves, moveIndex
    #print("moving...", moveIndex)
    instruction = moves[moveIndex]
    moveIndex+=1
    return instruction

def printOutput(o):
    # non-ASCII character is printed normally
    if (o > 255):
        print("Dust Collected:", o)
    # otherwise convert to ASCII and print
    else:
        print(chr(o), end='')

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
        printOutput(a)
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
