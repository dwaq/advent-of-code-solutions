import itertools

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

''' pretty print the starting data '''
print("After {} steps:".format(0))
for x in range(len(position)):
    print("pos=<x={:3}, y={:3}, z={:3}>, vel=<x={:3}, y={:3}, z={:3}>".format(
        position[x][0], position[x][1], position[x][2], velocity[x][0], velocity[x][1], velocity[x][2]))
print()

for step in range(1000):
    ''' first apply gravity '''
    # consider each pair
    # get every permutation of the phase setting
    possibilities = itertools.permutations(range(len(position)), 2)
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
    for p in range(len(position)):
        # go through x, y, and z
        for a in range(3):
            position[p][a] += velocity[p][a]

    ''' pretty print the data '''
    print("After {} steps:".format(step+1))
    for x in range(len(position)):
        print("pos=<x={:3}, y={:3}, z={:3}>, vel=<x={:3}, y={:3}, z={:3}>".format(
            position[x][0], position[x][1], position[x][2], velocity[x][0], velocity[x][1], velocity[x][2]))
    print()

''' calculate the total energy in the system '''
totalEnergy = 0

for moon in range(len(position)):
    potentialEnergy = 0
    kineticEnergy = 0
    # go through x, y, and z
    for a in range(3):
        # potential energy is absolute value sum of positions
        potentialEnergy += abs(position[moon][a])
        # kinetic energy is the absolute value sum of velocity
        kineticEnergy += abs(velocity[moon][a])

    # energy of moon is potential energy times kinetic energy
    totalEnergy += (potentialEnergy * kineticEnergy)

print("Total energy:", totalEnergy)