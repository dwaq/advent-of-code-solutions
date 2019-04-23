from anytree import Node, RenderTree

# open file and split into lines
with open('input.txt') as f:
    lines = f.readlines()

#level
names = {}

# make first level
for l in lines:
    # split by spaces
    s = l.split()

    # key is top level 
    x = s[0]
    
    # key: value
    names[x] = x
    
    # key points to node
    names[x] = Node(x)
    
    #print(names[x])
    
#print names['havc']
#print names

# second level
for l in lines:
    # split by spaces again
    s = l.split()
    
    # if there's children
    if (len(s) > 2):
        # the children that are pointed to
        # starting after the '->' and going to the end
        n = 3
        while(n<(len(s)-1)):
            # remove comma from string
            x = s[n].replace(",", "")
            
            # set that child's parents
            names[x].parent = names[s[0]]
            
            # move to the next one
            n=n+1

#print names

#print

# this is used to print a tower and it's parents
# then you can manually search up the tree
# just enter any ol name and it'll show the head
# 'hlhomy' is the head
print RenderTree(names['hlhomy'])

# print tree
#for pre, fill, node in RenderTree(names['hlhomy']):
#    print("%s%s" % (pre, node.name))