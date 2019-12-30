from itertools import combinations

responseBuffer = ""
# get instructions to gather all items
# and drop all items
with open("items.txt", "r") as fp:
    for line in (fp):
        responseBuffer += line

options = [
    "fuel cell",
    "cake",
    "pointer",
    "boulder",
    "mutex",
    "antenna",
    "tambourine",
    "coin"
]
# get all possibilities with any number of items
possibilities = []
for numItems in range(len(options)):
    possibilities += list(combinations(options, numItems+1))

# for choosing each possibility
index = 0
# for storing response
response = ""

# return a movement instruction
def moveDroid():
    global responseBuffer, possibilities, index, response

    # when empty, get more input
    if (len(responseBuffer) == 0):
        # tested something, drop it, move to next one
        if ("heavier" in response):
            print("too light:", possibilities[index])

            responseBuffer = ""
            for thing in possibilities[index]:
                responseBuffer += "drop "
                responseBuffer += thing
                responseBuffer += '\n'

            index+=1
        elif ("lighter" in response):
            print("too heavy", possibilities[index])

            responseBuffer = ""
            for thing in possibilities[index]:
                responseBuffer += "drop "
                responseBuffer += thing
                responseBuffer += '\n'
        
            index+=1

        # take the new things
        for thing in possibilities[index]:
            responseBuffer += "take "
            responseBuffer += thing
            responseBuffer += '\n'
        
        # try it by moving onto the scale
        responseBuffer += 'east\n'

        # reset for next check 
        response = ""

    # send one character
    returnChar = responseBuffer[0]
    responseBuffer = responseBuffer[1:]
    
    return ord(returnChar)

def printOutput(o):
    # otherwise convert to ASCII and print
    #print(chr(o), end='')
    # throw data into response instead of printing it
    global response
    response += chr(o)

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

# found it! print results
print(response)