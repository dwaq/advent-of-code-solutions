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

# start here
location = "AAA"

# steps to get there
steps = 0

# direction index
di = 0
# max direction index
mdi = len(directions)
#print(mdi)

# keep going until we finish
while(location != "ZZZ"):
    # pick direction
    d = directions[di]

    # convert to 0 or 1 to use as index
    d = 0 if d=="L" else 1
    #print(d)

    # change location based on direction
    location = maze[location][d]
    #print(location)

    # go to next direction
    di += 1
    if (di >= mdi):
        di = 0

    steps += 1

print("Steps:", steps)
