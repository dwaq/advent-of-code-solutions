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

numberOfCards = 119315717514047

# fill deck with cards
deck = [d for d in range(numberOfCards)]
# top = index 0
# bottom = index 1006

#print(deck)

# repeat the instructions this many times
for _ in range(101741582076661):
    for i in instructions:
        # check the 3x techniques
        if (i == newStack):
            #print("New")
            deck.reverse()
        elif (cut in i):
            n = int(i[len(cut):])
            #print("Cut", n)
            yourDeck = deck[n:]
            cutCards = deck[:n]
            deck = yourDeck + cutCards
        elif (increment in i):
            n = int(i[len(increment):])
            #print("Increment", n)
            newDeck = [None]*numberOfCards
            for p, d in enumerate(deck):
                #print("Position", (p*n)%numberOfCards, "Number", d)
                newDeck[(p*n)%numberOfCards] = d
            deck = newDeck

print("Card in position 2020:", deck[2020])