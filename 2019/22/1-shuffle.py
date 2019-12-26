# store shuffle instructions from file
instructions = []
with open("input.txt", "r") as fp:
    for f in (fp):
        instructions.append(f.strip('\n'))

#print(instructions)

# techniques
newStack = 'deal into new stack'
increment = 'deal with increment '
cut = 'cut '

numberOfCards = 10007

for i in instructions:
    # check the 3x techniques
    if (i == newStack):
        print("New")
    elif (increment in i):
        n = i[len(increment):]
        print("Increment", n)
    elif (cut in i):
        n = i[len(cut):]
        print("Cut", n)