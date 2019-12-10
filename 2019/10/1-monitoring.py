from fractions import Fraction

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

# loop through the map to measure from each point
for y in range(len(m)):
    for x in range(len(m[0])):
        # if we're on an asteroid
        if (m[y][x] == asteroid):

            # how many asteroids can we detect?
            count = 0

            # loop through the remaining map and determine if we can see it
            for dy in range(len(m)):
                for dx in range(len(m[0])):
                    # don't check the point we're on
                    if (x==dx and y==dy):
                        #print("we're home!")
                        continue

                    # needs to be an asteroid there
                    if(m[dy][dx] == asteroid):
                        #print("Asteroid found:", (dx,dy))

                        # check if something is in the slope of that line
                        mx = abs(x-dx)
                        my = abs(y-dy)
                        #print(mx, my)
                        
                        # reduce to smallest numbers
                        # slope of 8,6 -> 4,3
                        try:
                            frac = Fraction(mx, my)
                            mx = abs(frac.numerator)
                            my = abs(frac.denominator)
                        # when one side is zero, the other side is a straight line
                        # so reduce it to 1 to check every point in between
                        except ZeroDivisionError:
                            if(mx==0):
                                my=1
                            if(my==0):
                                mx=1

                        #print("Slope:", (mx, my))

                        # check along the slope of the line

                        # test points starting at the asteroid we're checkind
                        tx = dx
                        ty = dy

                        #print("Test point:", (tx,ty), (x,y))

                        # loop until we get back home
                        while (tx != x or ty != y):
                            #print("Original:", (x,y), "Test:", (dx,dy))
                            
                            # test in the correct direction
                            # if greater, reduce
                            if (dx>x):
                                tx-=mx
                            # otherwise, increase
                            else:
                                tx+=mx
                            
                            if (dy>y):
                                ty-=my
                            else:
                                ty+=my

                            #print("Test point:", (tx,ty))

                            # if this location is an asteroid, it's blocking your view, so leave
                            if(m[ty][tx] == asteroid):
                                break

                        # if we made it home without blocking, add to count
                        if (tx == x and ty == y):
                            count += 1

                        #print(count, "\n")

            # store asteroid counts to that location
            #print("count:", count)
            d[(x,y)] = count

# the point with the largest value
best = max(d, key=d.get)
print("Best Location:", best)
print("Number detected:", d[best])