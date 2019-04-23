import re
import collections

data = []

with open('input.txt', 'rb') as f:
    # break into pieces
    for line in f:
        # remove dash
        # strip bracket and newline off end
        # split the name and checksum using bracket
        l = line.replace('-', "").strip(']\n').split('[')
        
        # split text and number (ID)
        # http://stackoverflow.com/a/430102
        match = re.match(r"([a-z]+)([0-9]+)", l[0], re.I)
        if match:
            items = match.groups()

            # append room, ID, checksum
            data.append([items[0], items[1], l[1]])

sum_ids = 0

for d in data:
    print d
    
    # get number of occurances of each character in the string
    occur = {}
    # http://stackoverflow.com/a/17182670
    # get all lowercase letters
    from string import ascii_lowercase
    # loop through each character
    for char in ascii_lowercase:
        occur[char] = d[0].count(char)

    # sort dict by values (alphabetize it)
    # http://stackoverflow.com/a/9001529
    occur = collections.OrderedDict(sorted(occur.items()))
    # get 5 largest values
    # http://stackoverflow.com/a/7197643
    largest5 = sorted(occur, key=occur.get, reverse=True)[:5]
    #print largest5, d[2]
    
    checksum_ok = 1
    
    # loop though each of the largest 5 values
    for e in largest5:
        # ensure that the checksum and largest values match
        if (e not in d[2]):
            checksum_ok = 0
    
    # add up the ID if room is real
    if (checksum_ok == 1):
        sum_ids = sum_ids + int(d[1])
        
print sum_ids