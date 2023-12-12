file = open("input.txt", "r")
# strip newlines
txt = [x.strip("\n") for x in file.readlines()]
#txt = open("input.txt", "r").readlines()
#print(txt)

# return array of differences between each item in the array
def getDifferences(seq):
    diffs = []

    # get differences between items
    for d in range(len(seq)):
        # skip the first item
        if d == 0:
            continue
        diff = seq[d] - seq[d-1]
        diffs.append(diff)
        #print (d, seq[d], diff)

    #print(diffs)

    return diffs

# combine the new last item for each line
total = 0

# decode puzzle input
for sequence in txt:
    # split into numbers
    seq = sequence.split(" ")
    # convert everything to int
    seq = [int(x) for x in seq]
    #print (seq)

    # first sequence is non-zero
    zero = False

    # store first digits
    firstDigits = []

    while (zero == False):
        # first digit is the first item (duh)
        firstDigits.append(seq[0])

        # calculate the differences between the array
        seq = getDifferences(seq)
        
        # check if everything is 0 (exit condition)
        zero = all(x == 0 for x in seq)

    #print("first digits:", firstDigits)
    
    # subtract each number from the previous (starting at the end)
    # to get the next first digit
    diff = 0

    # length of list
    l =  len(firstDigits)

    # loop through each
    for x in range(l):
        # get index of the one we want (-1 to 0-index)
        # starting at the end (-x)
        i = l-x-1

        # calculate difference from last
        diff = firstDigits[i] - diff

        #print(i, firstDigits[i], diff)
        #print(d, firstDigits[i], i)
        #diff -= d

    #print("first digit:", diff)

    # add that difference to overall total
    total += diff

print("Total:", total)