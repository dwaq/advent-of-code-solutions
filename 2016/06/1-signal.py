import collections

data = [[], [], [], [], [], [], [], []]

# hacky way of getting it in columns
r = 0
while (r < 8):
    # go through each column
    with open('input.txt', 'rb') as f:
        # break into pieces
        for piece in f:
            data[r].append(piece[r])
    # go to next column
    r = r +1

# loop through each character
for d in data:
    
    # get number of occurances of each character in the string
    occur = {}
    # http://stackoverflow.com/a/17182670
    # get all lowercase letters
    from string import ascii_lowercase
    # loop through each character
    for char in ascii_lowercase:
        occur[char] = d.count(char)

    # sort dict by values (alphabetize it)
    # http://stackoverflow.com/a/9001529
    occur = collections.OrderedDict(sorted(occur.items()))

    # get largest value
    # http://stackoverflow.com/a/7197643
    most_often = sorted(occur, key=occur.get, reverse=True)[:1]
    print most_often