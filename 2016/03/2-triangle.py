data = []

# hacky way of getting it in columns
# go through the first column
with open('input.txt', 'rb') as f:
    # break into pieces
    for piece in f:
        data.append(int(piece[1:5]))
# then the second
with open('input.txt', 'rb') as f:
    # break into pieces
    for piece in f:
        data.append(int(piece[6:11]))
# then the third
with open('input.txt', 'rb') as f:
    # break into pieces
    for piece in f:
        data.append(int(piece[11:16]))


col = []
i = 0
while (i < len(data)-2):
    col.append([data[i], data[i+1], data[i+2]])
    i = i + 3

#print col

possible = 0

# loop through every line
for d in col:
    #print d
    good_so_far = 1

    # test each combo
    if (d[0]+d[1]<=d[2]):
        good_so_far = 0
    if (d[1]+d[2]<=d[0]):
        good_so_far = 0
    if (d[0]+d[2]<=d[1]):
        good_so_far = 0
    
    if (good_so_far == 1):
        possible = possible + 1

print possible
