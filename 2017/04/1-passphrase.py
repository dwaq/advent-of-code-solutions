#pp = "aa bb cc dd ee"

# open file and split into lines
with open('1-list.txt') as f:
    pp = f.readlines()

# count of good passphrases
good_count = 0

# go through each in list
for p in pp:
    # split by whitespace
    c = p.split()
    #print c
    
    # find duplicates
    # https://stackoverflow.com/a/1541827
    # false if good, true if bad
    if ((len(c) != len(set(c))) == False):
        good_count = good_count +1

print good_count