from anytree import Node, RenderTree

# open file
map = open('map.txt', 'r')

unorderedOrbits = []

# go through each
for o in map:
    # remove newline
    o = o.strip('\n')

    # split based on orbit
    unorderedOrbits.append(o.split(')'))

#print(unorderedOrbits)

# reorder list to start at root
orbits = []

def orderList(parent):
    # loop through each
    for o in unorderedOrbits:
        # add to list if parent
        if (o[0] == parent):
            orbits.append(o)
            # do the same to that child
            orderList(o[1])

# start at COM
orderList('COM')

#print(len(unorderedOrbits), len(orbits))

#print(orbits)

# use dictionary to store the tree in a way I can refer to it later
# https://stackoverflow.com/a/1373185/7564623
tree = {}

# set root
tree[orbits[0][0]] = Node(orbits[0][0])
# set variable for future use
root = tree[orbits[0][0]]

# set first child
tree[orbits[0][1]] = Node(orbits[0][1], parent=tree[orbits[0][0]])

# loop through remaining orbits
for orbit in orbits[1:]:
    # set as child
    tree[orbit[1]] = Node(orbit[1], parent=tree[orbit[0]])

#print(orbits)

you_i = 0
san_i = 0
# find where YOU and SAN are inside the orbits list
for x, o in enumerate(orbits):
    if (o[1] == 'YOU'):
        you_i = x
    if (o[1] == 'SAN'):
        san_i = x

# converts each orbit path to a string
# then splits based on the slash
# this gives all of the transfers needed to get to that point
you = str(tree[orbits[you_i][0]]).split('/')
san = str(tree[orbits[san_i][0]]).split('/')


matchPoint = 0
# find the point at which the paths are different
while(you[matchPoint] == san[matchPoint]):
    matchPoint+=1

# take the length from where the paths are different to the end
# and add them to get the total number of transfers
transfers = len(you[matchPoint:]) + len(san[matchPoint:])

print("Transfers required:", transfers)