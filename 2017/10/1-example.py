
# circular list
lst = [0,1,2,3,4]

# length of list
l = len(lst)

# input lengths
inp = [3,4,1,5]

# current position
cp = 0

# skip size
ss = 0

for i in inp:
    
    # need to wraparound if end position is longer than list
    if ((cp+i) > l):
        # how many we need to grab at the start of the list
        additional_length = (cp+i)%l
        
        sublst = lst[cp:] + lst[:additional_length]

    else:
        # just the portion we're working with
        sublst = lst[cp:cp+i]
        
    # reverse list
    # https://stackoverflow.com/a/3940137/7564623
    sublst = sublst[::-1]
    
    #print sublst, cp, lst
       
    # temporary current position
    # used to loop though all positions in lst
    tcp = cp
    
    # need to loop through each in sublst
    # and store new values in place in lst
    for s in sublst:
        #print lst, tcp, s
        lst[tcp] = s
        tcp=tcp+1
        if(tcp>=len(lst)):
            tcp=0
    
    # current position moves forward by the
    # (length plus the step size)
    # and wraps around
    cp = (cp + (i + ss))%l
    
    # Increase the skip size by one
    ss = ss + 1
    
    print lst, lst[cp]
    print

print "answer:", lst[0]*lst[1]