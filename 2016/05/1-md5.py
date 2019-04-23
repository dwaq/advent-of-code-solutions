import hashlib

#door_id = "ojvtpuvg"
door_id = "abc"

m = hashlib.md5()

integer = 0
digits = 0

# find 8 digits
while (digits < 8):
    # concatenate ID and integer
    seed = door_id + str(integer)

    # calculate MD5
    h = hashlib.md5(seed).hexdigest()

    # compare top 5 digits
    if (h[0:5] == "00000"):
        print h[5]
        print h
        digits = digits + 1
    
    # count up
    integer = integer + 1
