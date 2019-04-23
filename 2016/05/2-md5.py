import hashlib

door_id = "ojvtpuvg"

m = hashlib.md5()

integer = 0
digits = 0

# 8 character password
password = [0, 1, 2, 3, 4, 5, 6, 7]

# digits we haven't found yet
available = [0, 1, 2, 3, 4, 5, 6, 7]


# find all digits
while (len(available) > 0):
    # concatenate ID and integer
    seed = door_id + str(integer)

    # calculate MD5
    h = hashlib.md5(seed).hexdigest()

    # compare top 5 digits
    if (h[0:5] == "00000"):
        # found something that starts with 5 0's
        print h[5]
        # needs to fit in 8 character password length
        if (h[5] < str(8)):
            # h[5] is now the position in the password
            # don't overwrite it, so check if available
            if (int(h[5]) in available):
                # replace next character into password
                password[int(h[5])] = h[6]
                # remove from available
                available.remove(int(h[5]))
                # found something good
                print available

    # count up
    integer = integer + 1

# final password
print password