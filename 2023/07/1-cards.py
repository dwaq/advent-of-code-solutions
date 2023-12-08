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
strength = {
"A": "a",
"K": "b",
"Q": "c",
"J": "d",
"T": "e",
"9": "f",
"8": "g",
"7": "h",
"6": "i",
"5": "j",
"4": "k",
"3": "l",
"2": "m"
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
    # count how many of each card and sort from most to least common
    cards = Counter(hand).most_common()

    # check cards to get their rating
    rating = checkType(cards)

    # append rating, then hand, then that hand's bid
    ratings.append((rating, hand, bids[bid]))

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