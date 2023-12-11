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

# start at locations that end with "A"
starting = []
# list of all locations
locations = list(maze.keys())

# loop through all locations
for l in locations:
    # if it ends with "A", add it to list
    if l[2] == "A":
        starting.append(l)

#print(starting)

# steps to get there
steps = 0

# direction index
di = 0
# max direction index
mdi = len(directions)
#print(mdi)

foundExit = 0

# keep going until we finish
while(foundExit == 0):
    # pick direction
    d = directions[di]

    # convert to 0 or 1 to use as index
    d = 0 if d=="L" else 1
    #print(d)

    # change location based on direction FOR EACH starting point
    for i, s in enumerate(starting):
        starting[i] = maze[s][d]
    #print(starting)

    # assume we exit
    foundExit = 1

    # check if we made it to the exit
    for s in starting:
        #print(starting, s)
        # if it doesn't end with "Z", we didn't exit
        if s[2] != "Z":
            foundExit = 0
            break

    # go to next direction
    di += 1
    if (di >= mdi):
        di = 0

    steps += 1

print("Steps:", steps)
