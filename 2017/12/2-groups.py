# open file and split into lines
with open('list.txt') as f:
    lines = f.readlines()

# where to store all pipes
pipes = {}

# loop through them all and make nice data
for l in lines:
    # split data by seperator
    l = l.split(' <-> ')
    # split connections by comma
    connections = l[1].split(',')
    # convert to integers
    connections = map(int, connections)
    # add connections to pipe key
    pipes[int(l[0])] = connections

#print pipes

# check if the passed data is in a collection
def testConnection(d):
    # find the connections
    data = pipes[d]
    # go through each
    for d in data:
        # if it's not already there,
        if d not in touch:
            # add it
            touch.append(d)
            # test it's connections
            testConnection(d)

# add everything we touch here
touch = []

# the number of programs is the same as the number of lines
max_programs = len(lines)

# count of the number of groups
numgroups = 0

# start at ID 0
program = 0

# go through each
while(program < max_programs):
    # if you haven't found that program in a group yet
    if program not in touch:
        # there's another group
        numgroups += 1
        # start testing it
        testConnection(program)
    # loop through each program
    program += 1

print "number of unique programs:", numgroups
# correct answer: 186