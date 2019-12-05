#intcode = "1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50"
#intcode = "1,0,0,0,99"
#intcode = "2,3,0,3,99"
#intcode = "2,4,4,5,99,0"
#intcode = "1,1,1,4,99,5,6,0,99"
#intcode = "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,6,23,2,23,13,27,1,27,5,31,2,31,10,35,1,9,35,39,1,39,9,43,2,9,43,47,1,5,47,51,2,13,51,55,1,55,9,59,2,6,59,63,1,63,5,67,1,10,67,71,1,71,10,75,2,75,13,79,2,79,13,83,1,5,83,87,1,87,6,91,2,91,13,95,1,5,95,99,1,99,2,103,1,103,6,0,99,2,14,0,0"
intcode = "3,0,4,0,99"

instructions = intcode.split(",")

# convert all numbers to int
instructions = [int(x) for x in instructions]

# current instruction position
position = 0

# input to computer
inputValue = 1

#output to user
outputValue = 0

# end at 99
while(instructions[position] != 99):
    # current instruction
    i = instructions[position]

    if(i==1):
        a = instructions[instructions[position+1]]
        b = instructions[instructions[position+2]]
        instructions[instructions[position+3]] = a+b
        position += 4
    elif(i==2):
        a = instructions[instructions[position+1]]
        b = instructions[instructions[position+2]]
        instructions[instructions[position+3]] = a*b
        position += 4
    elif(i==3):
        newPosition = instructions[position+1]
        # take an input and store it at address given by parameter
        instructions[newPosition] = inputValue
        position += 2
    elif(i==4):
        newPosition = instructions[position+1]
        # outputs the value of its only parameter
        outputValue = instructions[newPosition]
        position += 2
    else:
        print("ERROR")

print("Output Value:", outputValue)
