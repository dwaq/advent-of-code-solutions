#pp = "aa bb cc dd ee"

# open file and split into lines
with open('1-list.txt') as f:
    pp = f.readlines()

# count of good passphrases
bad_count = 0

# count total to subtract bad
tot = 0

# go through each in list
for p in pp:
    # split by whitespace
    c = p.split()
    print c
    
    tot = tot+1
    
    # store length
    l = len(c)
    # compare the 0th against the 1st
    orig = 0
    # used to break out of both loops
    b = 0
    # go through part of the matrix
    while(orig < l):
        #print "orig:",orig
        comp = orig+1
        while(comp < l):
            
            # sort and compare (great way to detect anagrams)
            # https://stackoverflow.com/a/14990938
            if (sorted(c[orig]) == sorted(c[comp])):
                
                # only count once
                if (b==0):
                    print c[orig], c[comp] 
                    bad_count = bad_count +1
                # found it's wrong, break
                b = 1
                    
            comp=comp+1
        orig=orig+1

print "# Valid:",tot-bad_count