data = []

with open('input.txt', 'rb') as f:
    # break into pieces
    for piece in f:
        data.append([int(piece[1:5]), int(piece[6:11]), int(piece[11:16])])

possible = 0

# loop through every line
for d in data:
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
