# circular list
#lst=[0,1,2,3,4]
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255]

# length of list
l = len(lst)

# input numbers
chars = "31,2,85,1,80,109,35,63,98,255,0,13,105,254,128,33"

# input lengths (now in ASCII)
inp = []

for c in chars:
    # add the ascii representation of the character to the list
    inp.append(ord(c))

# need to add these to the end
inp.append(17)
inp.append(31)
inp.append(73)
inp.append(47)
inp.append(23)


# current position
cp = 0

# skip size
ss = 0

# run 64 rounds
times = 0
while(times < 64):

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
        
    # increase number of times through loop
    times +=1

# store intermediary dense hash
dense_hash = []

# 16 pieces that are 16 digits long
st=0
while(st<255):
    # grab 16 digits
    numrs = lst[st:st+16]
    
    # does XOR of 16 numbers
    result = 0
    for x in numrs:
        result = result ^ x
    
    # adds to list
    dense_hash.append(result)
    
    # does the next 16 digits
    st=st+16

# the ending hash is a string of hex characters
dense_hash_hex = ""

# go through each character
for dh in dense_hash:
    # always needs to be 2 characters
    if (dh<=0xF):
        # so add a starting 0 if it was only one character
        dense_hash_hex+='0'
    # convert to hex and add to string
    dense_hash_hex += (hex(dh).split('x')[-1])

# print it
print dense_hash_hex
# correct answer is: 28e7c4360520718a5dc811d3942cf1fd