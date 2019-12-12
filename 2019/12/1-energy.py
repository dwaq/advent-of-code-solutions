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

# first apply gravity
# consider each pair
# each axis's velocity changes by 1 based on positions
# >  -> +1
# <  -> -1
# == -> 0

# then apply velocity
# add the velocity of each moon to its position


# pretty print the data
print("After {} steps:".format(0))
for x in range(len(position)):
    print("pos=<x={:3}, y={:3}, z={:3}>, vel=<x={:3}, y={:3}, z={:3}>".format(
        position[x][0], position[x][1], position[x][2], velocity[x][0], velocity[x][1], velocity[x][2]))
print()