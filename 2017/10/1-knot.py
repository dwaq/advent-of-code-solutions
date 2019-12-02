
# circular list
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255]

# length of list
l = len(lst)

# input lengths
inp = [31,2,85,1,80,109,35,63,98,255,0,13,105,254,128,33]

# current position
cp = 0

# skip size
ss = 0

# go through each input
for i in inp:
    
    # need to wraparound if end position is longer than list
    if ((cp+i) > l):
        # how many we need to grab at the start of the list
        additional_length = (cp+i)%l
        
        # merge end and beginning to make sublst
        sublst = lst[cp:] + lst[:additional_length]

    else:
        # just the portion we're working with
        sublst = lst[cp:cp+i]
        
    # reverse the sublst
    # https://stackoverflow.com/a/3940137/7564623
    sublst = sublst[::-1]
       
    # temporary current position
    # used to loop though all positions in lst
    tcp = cp
    
    # need to loop through each in sublst
    # and store new values in place in lst
    for s in sublst:
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
    
    #print lst, lst[cp]
    #print

print "answer:", lst[0]*lst[1]
# correct answer is 6952