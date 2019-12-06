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

print(orbits)

counts = {}
'''
# find root
for oo in orbits:
    for o in oo:
        # if already there, increase count
        if o in counts:
            counts[o] += 1
        # otherwise set to 1
        else:
            counts[o] = 1

print(counts)
'''
'''
def stringToInt(orbit):
    #print(orbit)
    num = 0
    for l in orbit:
        num += ord(l)
    return num
'''

tree = {}

# set root
tree[orbits[0][0]] = Node(orbits[0][0])
#root = Node(orbits[0][0])
tree[orbits[0][1]] = Node(orbits[0][1], parent=tree[orbits[0][0]])

# loop through remaining orbits
#for o in orbits[1:]:
#    newone = Node(o[1], o[0])    

#print(root)

# display full tree
print(RenderTree(tree[orbits[0][0]]))