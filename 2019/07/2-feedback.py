from itertools import permutations

# storage for the 5x stages
# index 0 of array is the phase setting (5-9, each used once)
# index 1 of array is previous amp's output
# following this solution: https://www.reddit.com/r/adventofcode/comments/e7eezs/day_7_part_2_implementation_struggles/f9yk4c5/
# on second round, machine A produces 119 when it should get 115
# seems like there's some other bug in my code that is causing this
storage = [ [5,0],
            [6,0],
            [7,0],
            [8,0],
            [9,0]
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

# multiple input instructions per stage
# each amplifier has its own input occurrence
inputOccurrence = [0,0,0,0,0]

# end at 99
while(instructions[amp][ip[amp]] != 99):
    # current op code (lowest 2 digits)
    i = instructions[amp][ip[amp]]%100

    # get mode of each parameter
    # // does floor division (no floats)
    # %10 only gets that digit
    mode1 = (instructions[amp][ip[amp]]//  100)%10
    mode2 = (instructions[amp][ip[amp]]// 1000)%10
    mode3 = (instructions[amp][ip[amp]]//10000)%10

    try:
        a = instructions[amp][ip[amp]+1] if mode1 else instructions[amp][instructions[amp][ip[amp]+1]]
    except IndexError:
        pass

    try:
        b = instructions[amp][ip[amp]+2] if mode2 else instructions[amp][instructions[amp][ip[amp]+2]]
    except IndexError:
        pass

    #print(instructions[amp])
    #print(instructions[amp][ip[amp]], i, mode1, mode2, mode3)

    if(i==1):
        instructions[amp][instructions[amp][ip[amp]+3]] = a+b

        ip[amp] += 4
    elif(i==2):
        instructions[amp][instructions[amp][ip[amp]+3]] = a*b

        ip[amp] += 4
    elif(i==3):
        print(amp, ip[amp], storage[amp][0 if inputOccurrence[amp]==0 else 1])
        #print(amp, 0 if inputOccurrence[amp]==0 else 1)
        # take an input and store it at address given by parameter
        inputData = storage[amp][0 if inputOccurrence[amp]==0 else 1]
        #print(amp, inputData, inputOccurrence[amp])
        instructions[amp][instructions[amp][ip[amp]+1]] = inputData
        inputOccurrence[amp]+=1
        ip[amp] += 2
    elif(i==4):
        # outputs the value of its only parameter
        # store the output to the next amp (using modulo to feed back the last amp to the first)
        nextAmp = (amp+1)%5
        #print(amp, nextAmp)
        # set the next amp's input to this one's output 
        storage[nextAmp][1] = a
        print(amp, ip[amp], storage[nextAmp][1], instructions[amp])
        ip[amp] += 2
        # move to next amp
        amp = nextAmp
    elif(i==5):
        # jump if true
        if (a != 0):
            ip[amp] = b
        else:
            ip[amp] += 3
    elif(i==6):
        # jump if false
        if (a == 0):
            ip[amp] = b
        else:
            ip[amp] += 3
    elif(i==7):
        # less than
        if (mode3):
            instructions[amp][ip[amp]+3] = int(a<b)
        else:
            instructions[amp][instructions[amp][ip[amp]+3]] = int(a<b)

        ip[amp]+=4
    elif(i==8):
        # equals
        if (mode3):
            instructions[amp][ip[amp]+3] = int(a==b)
        else:
            instructions[amp][instructions[amp][ip[amp]+3]] = int(a==b)

        ip[amp]+=4
    else:
        print("ERROR")

'''
    # store the highest signal from all of the permutations
    if (storage[5][1] > highestSignal):
        highestSignal = storage[5][1]

    #print("Phase Setting:", possibility, "Output Signal:", storage[5][1])

print("Highest Signal:", highestSignal)
'''

print(amp, storage[amp][1])