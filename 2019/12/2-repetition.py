import itertools
from math import gcd

inputText = open("positions.txt", "r")

position = []
velocity = []

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

# store the location that the axis repeats
repeat = [0,0,0]

# go through x, y, and z seperately
for a in range(3):
    # reset the hash set each time
    hashes = set()

    while(True):
        ''' first apply gravity '''
        # consider each pair
        # get every permutation of the phase setting
        possibilities = itertools.permutations(range(4), 2)
        for p in possibilities:
            # p is a tuple in format (1st position, 2nd position)

            # each axis's velocity changes by 1 based on positions
            # if lower, increase velocity
            if (position[p[0]][a] < position[p[1]][a]):
                velocity[p[0]][a] += 1
            # if higher, decrease velocity
            elif (position[p[0]][a] > position[p[1]][a]):
                velocity[p[0]][a] -= 1
            # if the same, don't change

        # store the "hash"
        thisHash = ""

        ''' then apply velocity '''
        # add the velocity of each moon to its position
        for p in range(4):
            position[p][a] += velocity[p][a]

            # append position and velocity to hash
            # (reusing this loop because data is already calculated)
            thisHash += str(position[p][a]) + str(velocity[p][a])

        ''' Find when all of the moons' positions and velocities exactly match a previous point in time. '''
        # has this happened before?
        if (thisHash in hashes):
            print(a, 'occurred at:', len(hashes))
            repeat[a] = len(hashes)
            break
        # otherwise add to the list
        else:
            hashes.add(thisHash)

# get least common multiple
# https://stackoverflow.com/a/42472824/7564623
lcm = repeat[0]
for i in repeat[1:]:
    lcm = lcm*i//gcd(lcm, i)

print("Occurred at", lcm)