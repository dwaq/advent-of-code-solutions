from itertools import permutations

# storage for the 5x stages
# index 0 of array is the phase setting (0-4, each used once)
# index 1 of array is the previous amplifier's output signal
storage = [ [0,0],
            [1,0],
            [2,0],
            [3,0],
            [4,0],
            [0,0]   # only used for final output
        ]

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
    for amplifierStage in range(5):
        # amplifier instructions (reset for each loop)
        intcode = "3,8,1001,8,10,8,105,1,0,0,21,34,43,60,81,94,175,256,337,418,99999,3,9,101,2,9,9,102,4,9,9,4,9,99,3,9,102,2,9,9,4,9,99,3,9,102,4,9,9,1001,9,4,9,102,3,9,9,4,9,99,3,9,102,4,9,9,1001,9,2,9,1002,9,3,9,101,4,9,9,4,9,99,3,9,1001,9,4,9,102,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,99"

        instructions = intcode.split(",")

        # convert all numbers to int
        instructions = [int(x) for x in instructions]

        # current instruction position
        position = 0

        # multiple input instructions per stage
        inputOccurrence = 0

        # end at 99
        while(instructions[position] != 99):
            # current op code (lowest 2 digits)
            i = instructions[position]%100
            
            # get mode of each parameter
            # // does floor division (no floats)
            # %10 only gets that digit
            mode1 = (instructions[position]//  100)%10
            mode2 = (instructions[position]// 1000)%10
            mode3 = (instructions[position]//10000)%10

            try:
                a = instructions[position+1] if mode1 else instructions[instructions[position+1]]
            except IndexError:
                pass

            try:
                b = instructions[position+2] if mode2 else instructions[instructions[position+2]]
            except IndexError:
                pass

            #print(instructions)
            #print(instructions[position], i, mode1, mode2, mode3)

            if(i==1):
                instructions[instructions[position+3]] = a+b

                position += 4
            elif(i==2):
                instructions[instructions[position+3]] = a*b

                position += 4
            elif(i==3):
                # take an input and store it at address given by parameter
                instructions[instructions[position+1]] = storage[amplifierStage][inputOccurrence]
                inputOccurrence+=1
                position += 2
            elif(i==4):
                # outputs the value of its only parameter
                storage[amplifierStage+1][1] = a
                position += 2
            elif(i==5):
                # jump if true
                if (a != 0):
                    position = b
                else:
                    position += 3
            elif(i==6):
                # jump if false
                if (a == 0):
                    position = b
                else:
                    position += 3
            elif(i==7):
                # less than
                if (mode3):
                    instructions[position+3] = int(a<b)
                else:
                    instructions[instructions[position+3]] = int(a<b)

                position+=4
            elif(i==8):
                # equals
                if (mode3):
                    instructions[position+3] = int(a==b)
                else:
                    instructions[instructions[position+3]] = int(a==b)

                position+=4
            else:
                print("ERROR")

    # store the highest signal from all of the permutations
    if (storage[5][1] > highestSignal):
        highestSignal = storage[5][1]

    #print("Phase Setting:", possibility, "Output Signal:", storage[5][1])

print("Highest Signal:", highestSignal)
