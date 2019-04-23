
# open file and split into lines
with open('in1.txt') as f:
    content = f.readlines()

checksum = 0
for c in content:
    # split line by whitespace and convert to ints
    # https://stackoverflow.com/a/6429930
    line = map(int, c.split())
    #print line
    
    # find max and min and subtract them
    # https://stackoverflow.com/a/27009257
    max_value = max(line)
    min_value = min(line)
    difference = max_value - min_value
    #print difference
    
    # checksum is adding all of the differences
    checksum = checksum + difference

print checksum
#answer is 32020