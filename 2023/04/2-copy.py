txt = open("input.txt", "r").readlines()
#print(txt)

cards = 0

# go through each line
def goToCard(cardNum):
    # number of cards
    global cards
    cards += 1

    # cards are not 0-indexed
    line = txt[cardNum-1]

    match = 0

    details = line.split(": ")
    card = details[0][4:]
    numbers = details[1].strip("\n").split(" | ")
    winning = numbers[0].split(" ")
    mynums = numbers[1].split(" ")

    #print(card)

    for num in mynums:
        if (num) in winning:
            match += 1
            #print ("\t",num)

    # win however many next cards we have
    for m in range(match):
        nextcard = cardNum + m +1
        goToCard(nextcard)


# start with one of each card
for i, c in enumerate(range(len(txt))):
    print(i)
    goToCard(c)

print("numbers of cards", cards)