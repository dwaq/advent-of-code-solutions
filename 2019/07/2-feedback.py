from itertools import permutations

# storage for the 5x stages
# index 0 of array is the phase setting (5-9, each used once)
# index 1 of array is the previous amplifier's output signal
storage = [ [9,0],
            [8,0],
            [7,0],
            [6,0],
            [5,0]
        ]
'''
# store the highest signal that is seen
highestSignal = 0

# get every permutation of the phase setting
possibilities = set(permutations(range(5), 5))
for possibility in possibilities:
    # fill the storage array with that permutation
    for i, p in enumerate(possibility):
        storage[i] = [p, 0]

    #calculate the output from that phase setting
    # there's 5x stages
    for amp in range(5):
        '''
# amplifier instructions (reset for each loop)
intcode = "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5"

listOfInstructions = intcode.split(",")

# convert all numbers to int
listOfInstructions = [int(x) for x in listOfInstructions]

# start at the first amp
amp = 0

# each amp has its own instructions
instructions = [0,0,0,0,0]
for i in range(5):
    instructions[i] = listOfInstructions

# each amp has its own instruction position
ip = [0,0,0,0,0]

# each amp has their own count of this
# multiple input instructions per stage
inputOccurrence = [0,0,0,0,0]

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

    #print(instructions)
    #print(instructions[ip], i, mode1, mode2, mode3)

    if(i==1):
        a = instructions[ip+1] if mode1 else instructions[instructions[ip+1]]
        b = instructions[ip+2] if mode2 else instructions[instructions[ip+2]]
        
        instructions[instructions[ip+3]] = a+b

        ip += 4
    elif(i==2):
        a = instructions[ip+1] if mode1 else instructions[instructions[ip+1]]
        b = instructions[ip+2] if mode2 else instructions[instructions[ip+2]]

        instructions[instructions[ip+3]] = a*b

        ip += 4
    elif(i==3):
        newPosition = instructions[ip+1]
        # take an input and store it at address given by parameter
        instructions[newPosition] = storage[amp][inputOccurrence]
        inputOccurrence+=1
        ip += 2
    elif(i==4):
        # outputs the value of its only parameter
        storage[amp+1][1] = instructions[ip+1] if mode1 else instructions[instructions[ip+1]]
        ip += 2
    elif(i==5):
        # jump if true
        a = instructions[ip+1] if mode1 else instructions[instructions[ip+1]]
        b = instructions[ip+2] if mode2 else instructions[instructions[ip+2]]
        if (a != 0):
            ip = b
        else:
            ip += 3
    elif(i==6):
        # jump if false
        a = instructions[ip+1] if mode1 else instructions[instructions[ip+1]]
        b = instructions[ip+2] if mode2 else instructions[instructions[ip+2]]
        if (a == 0):
            ip = b
        else:
            ip += 3
    elif(i==7):
        # less than
        a = instructions[ip+1] if mode1 else instructions[instructions[ip+1]]
        b = instructions[ip+2] if mode2 else instructions[instructions[ip+2]]

        if (mode3):
            instructions[ip+3] = int(a<b)
        else:
            instructions[instructions[ip+3]] = int(a<b)

        ip+=4
    elif(i==8):
        # equals
        a = instructions[ip+1] if mode1 else instructions[instructions[ip+1]]
        b = instructions[ip+2] if mode2 else instructions[instructions[ip+2]]

        if (mode3):
            instructions[ip+3] = int(a==b)
        else:
            instructions[instructions[ip+3]] = int(a==b)

        ip+=4
    else:
        print("ERROR")

'''
    # store the highest signal from all of the permutations
    if (storage[5][1] > highestSignal):
        highestSignal = storage[5][1]

    #print("Phase Setting:", possibility, "Output Signal:", storage[5][1])

print("Highest Signal:", highestSignal)
'''
