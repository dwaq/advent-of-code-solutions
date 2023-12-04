txt = open("input.txt", "r").readlines()
#print(txt)

# store each line's values
value = []

def array_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total

first_num = None
second_num = None

# go through each line
for line in txt:
    # go through each character
    for char in line:
        # check if number
        if (char.isdigit()):
            # first occurance
            if (first_num == None):
                first_num = char
            # set the second one, at the end it'll be the last
            second_num = char
        #print(char)
    # combine numbers, convert to int, add to array
    value.append(int(first_num+second_num))
    #print(value)
    # reset first value for next loop
    first_num = None


# add all of the contents
print(array_sum(value))

