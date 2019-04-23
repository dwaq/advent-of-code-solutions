from anytree import Node, RenderTree

# open file and split into lines
with open('example.txt') as f:
    lines = f.readlines()

#level
names = {}

# make first level
for l in lines:
    # split by spaces
    s = l.split()

    # key is top level 
    x = s[0]
    
    # weight is at index 1
    # remove the parenthesis around it
    # convert to int
    weight = int(s[1].replace("(", "").replace(")", ""))
    
    # key points to node and weight in array
    
    names[x] = [Node(x), weight]

#print names

#for n in names:
#    print names[n][1]


# second level
for l in lines:
    # split by spaces again
    s = l.split()
    
    # if there's children
    if (len(s) > 2):
        # the children that are pointed to
        # starting after the '->' and going to the end
        n = 3
        while(n<len(s)):
            # remove comma from string
            x = s[n].replace(",", "")
            
            # set that child's parents
            names[x][0].parent = names[s[0]][0]
            
            # move to the next one
            n=n+1
            


# this is used to print a tower and it's parents
# then you can manually search up the tree
# just enter any ol name and it'll show the head
# 'hlhomy' is the head
#print RenderTree(names['tknk'][0])

for pre, fill, node in RenderTree(names['tknk'][0]):
    # add weight afterwards
    print("%s%s" % (pre, node.name)),
    weight_above = 0
    for c in node.children:
        weight_above = weight_above + names[c.name][1]
    #print weight_above
    # add current weight too             # \/ current weight
    weight_at_and_above = weight_above + names[node.name][1]
    print weight_at_and_above

#print
print names

'''
my current method isn't helpful because it only works on one parent (not all the way down)

one way to do this:

search through all and find all that have no children (they're at the bottom)

http://anytree.readthedocs.io/en/2.4.2/api/anytree.walker.html
use tree walking to start at the head (which I know from section 1)
and add all weights from top to bottom
this will give me the branch that has wrong weight

will need to find a way to change the weight without breaking the whole chain
because others may depend on it
maybe visulizing where it is can help


I don't know if I need this but another resource:
http://anytree.readthedocs.io/en/2.4.2/api/anytree.resolver.html

'''
