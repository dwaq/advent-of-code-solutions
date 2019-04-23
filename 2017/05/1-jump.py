# open file and split into lines
with open('inst.txt') as f:
    lines = f.readlines()

# remove newlines and convert to int
l = []
for x in lines:
   l.append((int(x))) 
    
# starting at index 0
index = 0
# count of steps taken to exit
steps = 0

# complete when you move past the end
while (index < len(l)):
    # store index because we need to modify it after
    old = index
    # increase the index by the current value
    index = index + l[index]
    # increase the current value by 1
    l[old] = l[old] + 1
    # add a step
    steps = steps + 1
    
    #print l, '\n'
    
print "total steps taken:", steps
# correct answer: 360603