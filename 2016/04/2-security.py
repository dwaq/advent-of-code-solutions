import re

data = []

with open('input.txt', 'rb') as f:
    # break into pieces
    for line in f:
        # strip bracket and newline off end
        # split the name and checksum using bracket
        l = line.strip(']\n').split('[')
        
        # split text and number (ID)
        # http://stackoverflow.com/a/430102
        # also match dash
        # http://stackoverflow.com/a/4068725
        match = re.match(r"([a-z-]+)([0-9]+)", l[0], re.I)
        if match:
            items = match.groups()

            # append room, ID, checksum
            data.append([items[0], items[1], l[1]])

# create array full of alphabet
ab = []
from string import ascii_lowercase
# loop through each character
for char in ascii_lowercase:
    ab.append(char)

# shift the character the number of times
# starting at the beginning when we hit the end
def shift(char, num):
    # find index of char in alphabet
    i = ab.index(char)

    n = 0
    while(n < int(num)):
        i = i + 1
        # when at end, loop around
        if (i == 26):
            i = 0
        n = n + 1
            
    return ab[i]

for d in data:
    fixed = ""
    for s in d[0]:
        # convert dash to space
        if (s == '-'):
            fixed = fixed + ' '
        # shift other characters
        else:
            fixed = fixed + shift(s, d[1])
    print fixed, d[1]