from collections import Counter

file = open("input.txt", "r")
# strip newlines
txt = [x.strip("\n") for x in file.readlines()]
#txt = open("input.txt", "r").readlines()
#print(txt)

hands = []
bids = []
ratings = []

# give a value to each card
# make it alphabetical to sort that way later
# joker is now lowest card
strength = {
"A": "a",
"K": "b",
"Q": "c",
"T": "d",
"9": "e",
"8": "f",
"7": "g",
"6": "h",
"5": "i",
"4": "j",
"3": "k",
"2": "l",
"J": "m"
}

# split input into hands and bids
for line in txt:
    line = line.split(" ")
    hands.append(line[0])
    bids.append(line[1])

#print(hands)

# replace cards with strength to make later steps easier
for h, hand in enumerate(hands):
    newHand = ""
    # go thru letters and replace/ append to new hand to replace
    for letter in hand:
        newHand += strength[letter]

    hands[h] = newHand

#print(hands)

# check the cards and assign a rating
# lower rating == better
def checkType(hand):
    #print(hand)

    # Five of a kind, where all five cards have the same label: AAAAA
    if len(hand) == 1:
        return 0

    numOfFirstCard = hand[0][1]

    # Four of a kind, where four cards have the same label and one card has a different label: AA8AA
    if (numOfFirstCard == 4):
        return 1

    numOfSecondCard = hand[1][1]

    # three cards matching, then check remaining two cards
    if (numOfFirstCard == 3):
        # Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
        if (numOfSecondCard == 2):
            return 2
        # Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
        else:
            return 3

    # Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
    if (numOfFirstCard == 2 and numOfSecondCard == 2):
        return 4

    # One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
    if (numOfFirstCard == 2):
        return 5

    # High card, where all cards' labels are distinct: 23456
    return 6

# check each hand's rating (what type of cards it has)
for bid, hand in enumerate(hands):
    #print(hand)
    # count how many of each card and sort from most to least common
    mc = Counter(hand).most_common()
    #print(mc, checkType(mc))

    # the most common card's value
    mcc = mc[0][0]
    # most common card can't be Joker (m)
    if (mcc == "m"):
        #print(mc)
        # so choose the second most common
        try:
            mcc = mc[1][0]
        # and if that doesn't work, it's because all the cards are Jokers
        # so just manually replace it
        except:
            mcc = "a"

    #print("most common card", mcc)

    # replace joker card with most common card
    #print(strength["J"])
    newHand =  hand.replace(strength["J"],mcc)
    #print(newHand)

    # count and sort the new newHand
    cards = Counter(newHand).most_common()

    # check cards to get their rating
    rating = checkType(cards)

    #print(cards, rating)

    # append rating, then original hand, then that hand's bid
    ratings.append((rating, hand, bids[bid]))

    #exit()
#print(ratings)

# sorting first on rating (lower = better)
# then hand alphabetically
ratings = sorted(ratings)

#print(ratings)

# higher rank is better
rank = len(hands)

winnings = 0

for r, rating in enumerate(ratings):
    bid = int(rating[2])
    #print(bid)
    # rank drops each loop
    winnings += (rank-r)*bid


print("Winnings:", winnings)