import math

empty = '.'
asteroid = '#'

# top left is 0,0
# to the right is 1,0
# an example layout:
#0,0	1,0	2,0	3,0	4,0
#0,1	1,1	2,1	3,1	4,1
#0,2	1,2	2,2	3,2	4,2
#0,3	1,3	2,3	3,3	4,3
#0,4	1,4	2,4	3,4	4,4

# pretty print the map
def printMap(m):
    for line in m:
        print(line)

wholeMap = open("map.txt", "r")

# store map here
m = []

for line in wholeMap:
    # strip newlines 
    # convert each item of the line into an item of the array
    # and add to the array
    m.append(list(line.strip('\n')))

#printMap(m)

# store each asteroids distances in a dict
d = {}

# from before:
# Best Location: (11, 13)
x, y, = 8, 3
# Number detected: 210

# loop through each point and calculate the angle
for dy in range(len(m)):
    for dx in range(len(m[0])):
        # don't check the point we're on
        if (x==dx and y==dy):
            #print("we're home!")
            continue

        # needs to be an asteroid there
        if(m[dy][dx] == asteroid):
            # calculate angle
            delta_x = dx - x
            delta_y = y - dy

            theta_radians = math.atan2(delta_x, delta_y)
            theta_degrees = math.degrees(theta_radians)

            # convert negative degrees to positive
            if(theta_degrees < 0):
                theta_degrees += 360

            #print("Asteroid found:", (dx,dy), theta_radians)

            # store that angle at the point (for display purposes)
            m[dy][dx] = round(theta_degrees,1)

            # store in dict to sort later
            d[(dx,dy)] = theta_degrees

        # for display purposes only
        else:
            m[dy][dx] = '...'

#printMap(m)

for key, value in sorted(d.items(), key=lambda item: item[1]):
    print("%s: %s" % (key, value))