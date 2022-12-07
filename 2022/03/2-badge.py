txt = open("input.txt", "r").readlines()
#print(txt)

score = 0

line = 0

badge = ''

# go through each line
while (line < len(txt)):
    # group of 3
    a = txt[line+0].strip('\n')
    b = txt[line+1].strip('\n')
    c = txt[line+2].strip('\n')
    print(a, b, c)

    # common items in a & b
    ab = []
    # loop through a
    for l in a:
        # if there's a common letter between a & b
        if (l in b):
            # add to a common list
            ab.append(l)
        # loop through common items in a & b
        for x in ab:
            # if that letter is also in c
            if x in c:
                # it has to be the badge
                # (there's multiple of the same, but just set it and it can overwrite)
                badge = x


    # calculate the score
    if (badge.isupper()):
        # subtract a to get base offset
        # add 1 because it starts from 1
        # add 26 because uppercase starts after lowercase
        l_score = ord(badge)-ord('A')+1+26
    # lower case
    else:
        l_score = ord(badge)-ord('a')+1
    print(badge, l_score)
    # add letter's score to total score
    score += l_score

    # go to next group of 3
    line +=3

print(score)

