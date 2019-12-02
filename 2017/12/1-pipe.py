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

# start at ID 0
testConnection(0)

#print sorted(touch)

print "number of programs:", len(touch)
# correct answer: 152