# RULES:
# 6 digits (automatically true in this range)
# within range of puzzle input (done)
# two adjacent digits are the same (done)
# left to right, digits never decrease (only increase or stay the same) (done)

total = 0

# open a file to store all passwords
f = open("passwords.txt", "w")

for n in range(137683, 596253+1):
    # convert to string
    s = str(n)
    # split into letters
    l = list(s)
    # convert back to ints
    i = [int(letter) for letter in l]

    # check for adjacent digits
    adjacent = False
    # don't loop through the last one because we're checking next vs current
    for x, d in enumerate(i[:-1]):
        # check if current number (d) matches the next number (index + 1)
        if (d == i[x+1]):
            #print("adjacent digits:", n)
            adjacent = True
            break

    # check that digits increase
    increase = True
    # needs to be true to continue
    if (adjacent == True):
        # check that digits increase
        for x, d in enumerate(i[:-1]):
            # problem if current number (d) is greater than next number (index + 1)
            if (d > i[x+1]):
                increase = False

        # checked everything; add to total if still true
        if (increase == True):
            #print("\tdigits increase:", n)
            # write correct number to file
            f.write(str(n)+"\n")
            total += 1

print("total: ", total)
# close it
f.close()
