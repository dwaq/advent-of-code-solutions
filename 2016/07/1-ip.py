import re

#example = "abba[mnop]qrst"
#example = "abcd[bddb]xyyx"
#example = "aaaa[qwer]tyui"
#example = "ioxxoj[asdfgh]zxcvbn"
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
    
    # reset counters
    valid = 0
    invalid = 0
    
    # go through each portion of the data (previously seperated by brackets)
    d = 0
    while (d < len(data)):
        
        # go throught this chunk, stopping before going past the end
        # only going in chunks of 4 characters
        i = 0
        while (i < (len(data[d])-3)):
            # "good" data: 12 == 21
            if ((data[d][i] == data[d][i+3]) and (data[d][i+1] == data[d][i+2])):
                # can't be 1111
                if (data[d][i] != data[d][i+1]):

                    # odd (portion previously inside brackets) is not OK
                    if (d%2):
                        invalid = 1
                    # even are OK
                    else:
                        valid = 1

            i = i + 1
        d = d + 1
        
    # check if good
    # not considered good if algorithm matched inside brackets
    if (invalid == 0):
        if (valid == 1):
            good = good + 1
            
print "total number of good IPs:", good
