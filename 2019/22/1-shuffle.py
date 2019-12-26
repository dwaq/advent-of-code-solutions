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

numberOfCards = 10#007

# fill deck with cards
deck = [d for d in range(numberOfCards)]
# top = index 0
# bottom = index 1006

print(deck)
print('\n')

for i in instructions:
    # check the 3x techniques
    if (i == newStack):
        print("New")
        deck.reverse()
    elif (increment in i):
        n = int(i[len(increment):])
        print("Increment", n)
    elif (cut in i):
        n = int(i[len(cut):])
        print("Cut", n)
        yourDeck = deck[n:]
        cutCards = deck[:n]
        deck = yourDeck + cutCards

print(deck)