import re

#example = "aba[bab]xyz"
#example = "xyx[xyx]xyx"
#example = "aaa[kek]eke"
#example = "zazbz[bzb]cdb"
#example = "rnqfzoisbqxbdlkgfh[lwlybvcsiupwnsyiljz]kmbgyaptjcsvwcltrdx[ntrpwgkrfeljpye]jxjdlgtntpljxaojufe"

ips = []

# open file
with open('input.txt', 'rb') as f:
    # break into pieces
    for line in f:
        # strip the newline and append
        ips.append(line.strip(']\n'))

# store number of good entries      
good = 0

# go line by line
for example in ips:
    
    # split at the brackets
    data = re.split('\[|\]',example)
    
    aba = []
    bab = []
    
    # go through each portion of the data (previously seperated by brackets)
    d = 0
    while (d < len(data)):
        
        # go throught this chunk, stopping before going past the end
        # only going in chunks of 3 characters
        i = 0
        while (i < (len(data[d])-2)):
    
            # "good" data: 121, but 2 needs to be different than 1
            if ((data[d][i] == data[d][i+2]) and (data[d][i] != data[d][i+1])):
                
                #print i, data[d][i], data[d][i+1], data[d][i+2], data[d][i:i+3], i
                # odd (portion previously inside brackets) is BAB
                if (d%2):
                    bab.append(data[d][i:i+3])
                # even are ABA
                else:
                    aba.append(data[d][i:i+3])
    
            i = i + 1
        d = d + 1
    
    # invert bab
    bab_invert = []
    for b in bab:
        one = b[0]
        two = b[1]
        bab_invert.append(two+one+two)
    
    found = 0
    # find a aba in bab_invert
    for a in aba:
        if a in bab_invert:
            found = 1
            #print aba
            #print bab
            #print bab_invert
            #print a
            #print example
            #print
    
    # found is 1 if found, otherwise 0
    good = good + found

print "total number of IPs that support SSL:", good
