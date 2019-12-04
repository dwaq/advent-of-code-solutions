# open file
f =  open("passwords.txt", "r")

# count how many are good
total = 0

# loop through the file of good passwords
for pw in f:
    # strip newlines
    n = pw.strip("\n")
    
    # convert to string
    s = str(n)
    # split into letters
    l = list(s)
    # convert back to ints
    i = [int(letter) for letter in l]
    
    # assume invalid until proven valid
    valid = False

    # keep a count of how many adjacent letters
    # always gonna have at least 1 adjacent letter
    count = 1
    adjacent = False

    # loop through each individual number
    q = 0
    while (q < len(i)-1):
        # if next number is the same as this one, it's true
        if (i[q+1] == i[q]):
            adjacent = True
        else:
            adjacent = False
        
        # if it's true, increase the count of adjacent letters
        if (adjacent == True):
            #print(i[q])
            count+=1
        # when the streak ends, check if there has been two in a row
        else:
            #print(i[q], "\tbroken:", count)
            if (count == 2):
                valid = True
            # reset counter
            count=1

        # go to next letter
        q+=1

        # on the last letter, check count again
        if (q == len(i)-1):
            #print(i[q], "\tend:", count)
            if (count == 2):
                valid = True

    # if it was deemed valid, add to the total
    if (valid == True):
        #print (n, 'valid')
        total+=1
    #else:
        #print(n, 'bad')
    
print("Total:", total)
