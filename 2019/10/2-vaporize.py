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
        for l in line:
            if(l=='.'):
                l=' .'
            elif(l=='#'):
                l=' #'
            elif(l=='X'):
                l=' X'
            elif(int(l) < 10):
                l=' '+str(l)
            print(l, end =" ")
        print()

wholeMap = open("map.txt", "r")

# store map here
m = []

for line in wholeMap:
    # strip newlines 
    # convert each item of the line into an item of the array
    # and add to the array
    m.append(list(line.strip('\n')))

#printMap(m)

# store each asteroids degrees & distances in a dict
degrees = {}
distance = {}

# from before:
# Best Location: (11, 13)
x, y, = 11,13
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
            #m[dy][dx] = round(theta_degrees,1)

            # calculate distance away
            dist = math.sqrt((dx - x)**2 + (dy - y)**2)  

            #m[dy][dx] = round(dist,1)

            # store in dict to sort later
            degrees[(dx,dy)] = theta_degrees
            distance[(dx,dy)] = dist

#printMap(m)

# sort all asteroids based on angle
sortedKeys = list({k: v for k, v in sorted(degrees.items(), key=lambda item: item[1])})

#print(sortedKeys)

numberVaporized=0

# keep track of when multiple angles are the same
sameAngleStorage = 370

# reset that counter when we make a full rotation
lastAngle = 370

# loop through list and vaporize some asteroids
for i, key in enumerate(sortedKeys):
    #print(i)
    try:
        # reset the angle storage after a full rotation
        if (degrees[sortedKeys[i]] < lastAngle):
            sameAngleStorage = 370
    # key has been erased
    except KeyError:
        continue
    lastAngle = degrees[sortedKeys[i]]

    #print(i, degrees[sortedKeys[i]], distance[sortedKeys[i]])

    # stop checking if we've already dealt with this angle
    if (degrees[sortedKeys[i]] == sameAngleStorage):
        #print("Saw already:", key, degrees[sortedKeys[i]])
        continue
    # else store angle to skip it next time
    else:
        #print("Didn't see:", key, degrees[sortedKeys[i]])
        sameAngleStorage = degrees[sortedKeys[i]]

    # if angle is the same, choose the lowest distance one
    # then skip that angle until the next revolution

    try:    # so you don't pass the end of the list
        # if the angle is the same as next
        if (degrees[sortedKeys[i+1]] == degrees[sortedKeys[i]]):
            # get all points that have that angle
            points = []
            for point, angle in degrees.items():
                if angle == degrees[sortedKeys[i]]:
                    points.append(point)

            #print("Same points:", points)

            # get the point that has the shortest distance
            minDistance = 100000
            minDistPoint = (0,0)
            for point in points:
                #print(point, distance[point])
                if (distance[point] < minDistance):
                    minDistance = distance[point]
                    minDistPoint = point

            #print("Minimum distance point:", minDistPoint)
            
            # vaporize the closest one
            numberVaporized+=1
            m[minDistPoint[1]][minDistPoint[0]] = numberVaporized

            print(numberVaporized, (minDistPoint[0],minDistPoint[1]))

            # delete from degrees and distance so it can't be used again
            del degrees[point]
            del distance[point]

            # then move to next one
            continue

    except IndexError:
        pass
    #print(i, d[key])

    #if(i>12 and i<33):
    #if(i<25):
        # FYI, sortedKeys[i] == key
        #print(i, degrees[key], distance[key])
    numberVaporized+=1
    m[key[1]][key[0]] = numberVaporized

    print(numberVaporized, (key[0],key[1]))


#printMap(m)
