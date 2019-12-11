# input to computer
inputValue = 5

#intcode = "1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50"
#intcode = "1,0,0,0,99"
#intcode = "2,3,0,3,99"
#intcode = "2,4,4,5,99,0"
#intcode = "1,1,1,4,99,5,6,0,99"
#intcode = "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,6,23,2,23,13,27,1,27,5,31,2,31,10,35,1,9,35,39,1,39,9,43,2,9,43,47,1,5,47,51,2,13,51,55,1,55,9,59,2,6,59,63,1,63,5,67,1,10,67,71,1,71,10,75,2,75,13,79,2,79,13,83,1,5,83,87,1,87,6,91,2,91,13,95,1,5,95,99,1,99,2,103,1,103,6,0,99,2,14,0,0"
#intcode = "3,0,4,0,99"
#intcode = "1002,4,3,4,33"
intcode = "3,225,1,225,6,6,1100,1,238,225,104,0,1102,57,23,224,101,-1311,224,224,4,224,1002,223,8,223,101,6,224,224,1,223,224,223,1102,57,67,225,102,67,150,224,1001,224,-2613,224,4,224,1002,223,8,223,101,5,224,224,1,224,223,223,2,179,213,224,1001,224,-469,224,4,224,102,8,223,223,101,7,224,224,1,223,224,223,1001,188,27,224,101,-119,224,224,4,224,1002,223,8,223,1001,224,7,224,1,223,224,223,1,184,218,224,1001,224,-155,224,4,224,1002,223,8,223,1001,224,7,224,1,224,223,223,1101,21,80,224,1001,224,-101,224,4,224,102,8,223,223,1001,224,1,224,1,224,223,223,1101,67,39,225,1101,89,68,225,101,69,35,224,1001,224,-126,224,4,224,1002,223,8,223,1001,224,1,224,1,224,223,223,1102,7,52,225,1102,18,90,225,1101,65,92,225,1002,153,78,224,101,-6942,224,224,4,224,102,8,223,223,101,6,224,224,1,223,224,223,1101,67,83,225,1102,31,65,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1007,226,226,224,102,2,223,223,1005,224,329,1001,223,1,223,108,677,226,224,1002,223,2,223,1005,224,344,1001,223,1,223,1007,677,677,224,1002,223,2,223,1005,224,359,1001,223,1,223,1107,677,226,224,102,2,223,223,1006,224,374,1001,223,1,223,8,226,677,224,1002,223,2,223,1006,224,389,101,1,223,223,8,677,677,224,102,2,223,223,1006,224,404,1001,223,1,223,1008,226,226,224,102,2,223,223,1006,224,419,1001,223,1,223,107,677,226,224,102,2,223,223,1006,224,434,101,1,223,223,7,226,226,224,1002,223,2,223,1005,224,449,1001,223,1,223,1107,226,226,224,1002,223,2,223,1006,224,464,1001,223,1,223,1107,226,677,224,1002,223,2,223,1005,224,479,1001,223,1,223,8,677,226,224,1002,223,2,223,1006,224,494,1001,223,1,223,1108,226,677,224,1002,223,2,223,1006,224,509,101,1,223,223,1008,677,677,224,1002,223,2,223,1006,224,524,1001,223,1,223,1008,677,226,224,102,2,223,223,1006,224,539,1001,223,1,223,1108,677,677,224,102,2,223,223,1005,224,554,101,1,223,223,108,677,677,224,102,2,223,223,1006,224,569,101,1,223,223,1108,677,226,224,102,2,223,223,1005,224,584,1001,223,1,223,108,226,226,224,1002,223,2,223,1005,224,599,1001,223,1,223,1007,226,677,224,102,2,223,223,1005,224,614,1001,223,1,223,7,226,677,224,102,2,223,223,1006,224,629,1001,223,1,223,107,226,226,224,102,2,223,223,1005,224,644,101,1,223,223,7,677,226,224,102,2,223,223,1005,224,659,101,1,223,223,107,677,677,224,1002,223,2,223,1005,224,674,1001,223,1,223,4,223,99,226"
#intcode, inputValue = "3,9,8,9,10,9,4,9,99,-1,8", 8
#intcode, inputValue = "3,9,7,9,10,9,4,9,99,-1,8", 7
#intcode, inputValue = "3,3,1108,-1,8,3,4,3,99", 8
#intcode, inputValue = "3,3,1107,-1,8,3,4,3,99", 7
#intcode, inputValue = "3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9", 1
#intcode, inputValue = "3,3,1105,-1,9,1101,0,0,12,4,12,99,1", 0
#intcode, inputValue = "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99", 8

instructions = intcode.split(",")

# convert all numbers to int
instructions = [int(x) for x in instructions]

# current instruction pointer
ip = 0

#output to user
outputValue = 0

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
        instructions[newPosition] = inputValue
        ip += 2
    elif(i==4):
        # outputs the value of its only parameter
        outputValue = instructions[ip+1] if mode1 else instructions[instructions[ip+1]]
        #print("Output at", ip, "is", outputValue)
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

#print(instructions)
print("Output Value:", outputValue)
