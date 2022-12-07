txt = open("input.txt", "r").readlines()

fully_contain = 0

def isInside(x, y):
    #print(x,y)
    # if x starts first and ends second
    # really checks if y is inside x
    if (x[0] <= y[0] and x[1] >= y[1]):
        return True
    else:
        return False


for line in txt:
    # split the text into the 2 pairs
    pairs = line.strip('\n').split(',')
    # split the pairs into their assignments
    for p in range(len(pairs)):
        pairs[p] = pairs[p].split('-')

        # convert letters to numbers
        pairs[p] = [int(z) for z in pairs[p]]
    
    # check if first is inside second
    fully_contain1 = isInside(pairs[0], pairs[1])
    # check if second is inside first
    fully_contain2 = isInside(pairs[1], pairs[0])

    # if either were True
    if (fully_contain1 or fully_contain2):
        # up the count
        fully_contain += 1

print(fully_contain)