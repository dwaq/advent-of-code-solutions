import itertools

inputText = open("positions.txt", "r")

position = []
velocity = []
hashes = set()

for line in inputText:
    # remove extra characters
    line = line.strip("<>\n")

    # split into x, y, z
    line = line.split(", ")

    data = []

    # remove x=, y=, and z= text
    # and convert to int
    for c in line:
        data.append(int(c[2:]))

    position.append(data)
    # each position also has a velocity starting at 0
    velocity.append([0,0,0])

#print(position)
#print(velocity)

while(True):
    ''' first apply gravity '''
    # consider each pair
    # get every permutation of the phase setting
    possibilities = itertools.permutations(range(4), 2)
    for p in possibilities:
        # p is a tuple in format (1st position, 2nd position)
        #print(p, p[0], p[1])

        # each axis's velocity changes by 1 based on positions
        # go through x, y, and z
        for a in range(3):
            # if lower, increase velocity
            if (position[p[0]][a] < position[p[1]][a]):
                velocity[p[0]][a] += 1
            # if higher, decrease velocity
            elif (position[p[0]][a] > position[p[1]][a]):
                velocity[p[0]][a] -= 1
            # if the same, don't change

    ''' then apply velocity '''
    # add the velocity of each moon to its position
    for p in range(4):
        # go through x, y, and z
        for a in range(3):
            position[p][a] += velocity[p][a]

    ''' Find when all of the moons' positions and velocities exactly match a previous point in time. '''
    # hash the data
    thisHash = (str(position) + str(velocity))
    #thisHash = hash(combine)
    #thisHash = hashids.encode(combine)
    #print(thisHash)

    # has this happened before?
    if (thisHash in hashes):
        print('Occurred at:', len(hashes))
        break
    # otherwise add to the list
    else:
        hashes.add(thisHash)
