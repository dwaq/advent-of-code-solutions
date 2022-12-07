txt = open("input.txt", "r").readlines()
#print(txt)

# store each elf's calories
elf = []
score = 0


# go through each line
for line in txt:
    items = line.strip('\n')
    # split into lower and upper half
    a = items[:len(items)//2]
    b = items[len(items)//2:]
    print(a, b)
    # loop through the letters
    for l in a:
        # if there's a common letter
        if (l in b):
            # calculate the score
            if (l.isupper()):
                # subtract a to get base offset
                # add 1 because it starts from 1
                # add 26 because uppercase starts after lowercase
                l_score = ord(l)-ord('A')+1+26
            # lower case
            else:
                l_score = ord(l)-ord('a')+1
            print(l, l_score)
            # add letter's score to total score
            score += l_score

            # only care about the first match, so exit early
            break

print(score)

