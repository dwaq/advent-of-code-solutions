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

    # store last digits
    lastDigits = []

    while (zero == False):
        # last digit is the last item (duh)
        lastDigits.append(seq[-1])

        # calculate the differences between the array
        seq = getDifferences(seq)
        
        # check if everything is 0 (exit condition)
        zero = all(x == 0 for x in seq)

    #print("last digits:", lastDigits)
    
    # add all last digits to get next digit (add to get puzzle total)
    total += sum(lastDigits)

    #print("next digit:", diff)

    #print("next digit:", lastDigits[0] + lastDigits[1])

print("Total:", total)