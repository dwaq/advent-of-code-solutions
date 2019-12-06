from anytree import Node, RenderTree

# open file
map = open('map.txt', 'r')

orbits = []

# go through each
for o in map:
    # remove newline
    o = o.strip('\n')

    # split based on orbit
    orbits.append(o.split(')'))

#print(orbits)

# use dictonary to store the tree in a way I can refer to it later
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

#print(root)

# display full tree
for pre, fill, node in RenderTree(root):
    print("%s%s" % (pre, node.name))

# get the paths of every orbit
paths = root.descendants
#print(paths)

numberOfOrbits = 0

# for each path, add it's depth to the number of orbits
for path in paths:
    numberOfOrbits += path.depth

print("Total number of Orbits:", numberOfOrbits)