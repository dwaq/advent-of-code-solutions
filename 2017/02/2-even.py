
# open file and split into lines
with open('in1.txt') as f:
    content = f.readlines()

checksum = 0
for c in content:
    # split line by whitespace and convert to ints
    # https://stackoverflow.com/a/6429930
    line = map(int, c.split())
    #print line
    
    # store length
    l = len(line)
    # compare the 0th against the 1st
    s = 1
    # go through part of the matrix
    while(s < l):
        # for each number in the remainder
        for n in line[s:l]:
            #print line[s-1], n, line[s-1]%n, n%line[s-1]
            # compare original number with new one
            # (evenly divisible)
            if (line[s-1]%n == 0):
                # if so, add it to the checksum
                checksum = checksum + (line[s-1]/n)
                # and end
                break
            # same but in reverse
            if (n%line[s-1] == 0):
                checksum = checksum + (n/line[s-1])
                break
        # wasn't that number, compare the next, etc
        s = s + 1

print checksum
#answer is 236