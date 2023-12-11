from math import lcm

file = open("input.txt", "r")
# strip newlines
txt = [x.strip("\n") for x in file.readlines()]
#txt = open("input.txt", "r").readlines()
#print(txt)


directions = ""

maze = dict()

# decode puzzle input
for l, line in enumerate(txt):
    # first line is directions
    if (l == 0):
        directions = line
    # after break is maze input
    elif (l > 1):
        # formatting
        line = line.strip(")")
        line = line.split(" = (")
        
        # key
        k = line[0]

        # value
        v = line[1].split(", ")

        maze[k] = v

#print(maze)

# start at locations that end with "A"
starting = []
# list of all locations
locations = list(maze.keys())
# end at locations that end with "Z"
ending = []

# loop through all locations
for l in locations:
    # if it ends with "A", add it to list
    if l[2] == "A":
        starting.append(l)

#print("starting locations:", starting)

# loop through all locations
for l in locations:
    # if it ends with "Z", add it to list
    if l[2] == "Z":
        ending.append(l)

#print("ending locations:", ending)

# direction index
di = 0
# max direction index
mdi = len(directions)
#print(mdi)

# steps needed for each ending
ending_steps = []

# change location based on direction FOR EACH starting point
for location in starting:
    start = location
    #print(location)

    # reset steps for each one
    steps = 0
    # did we find the exit
    foundExit = 0

    # keep going until we find an exit
    while(foundExit == 0):
        # steps to get there
        steps += 1

        # pick direction
        d = directions[di]

        # convert to 0 or 1 to use as index
        d = 0 if d=="L" else 1
        #print(d)

        # change location based on direction
        location = maze[location][d]
        #print(location)

        # if we make it to an ending location
        if location in ending:
            #print("location found:", start, location, steps)
            # remove from possible ending
            ending.remove(location)
            # keep track here of the steps needed here
            ending_steps.append(steps)
            # only need to find one exit per start
            foundExit = 1

        # go to next direction
        di += 1
        if (di >= mdi):
            di = 0

#print(ending_steps)
# break the 6 endings amounts into 6 variables
a, b, c, d, e, f = ending_steps
#print(a, b, c, d, e, f )
# get the least common multiple
total_steps = lcm(a, b, c, d, e, f )
# that's how many steps needed
print("total steps needed:", total_steps)