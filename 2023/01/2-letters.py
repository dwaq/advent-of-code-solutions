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

real_digits = ["1","2","3","4","5","6","7","8","9"]
spelled_digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def getFirst(line):
    # go through each position
    for pos in range(len(line)):
        # remaining text
        text = line[pos:]

        # go through real numbers
        for d in real_digits:
            # return matching number
            if text.startswith(d):
                return d
        
        # go through text numbers
        for i, d in enumerate(spelled_digits):
            # use index to convert spelled number to real number when found
            if text.startswith(d):
                return real_digits[i]

def getLast(line):
    length = len(line)
    # go through each position
    for pos in range(length):
        # remove text from end
        text = line[:(length-pos)]
        #print(text)

        # go through real numbers
        for d in real_digits:
            # return matching number
            if text.endswith(d):
                return d
        
        # go through text numbers
        for i, d in enumerate(spelled_digits):
            # use index to convert spelled number to real number when found
            if text.endswith(d):
                return real_digits[i]


# go through each line
for line in txt:
    # find first number
    first_num = getFirst(line)
    #print(first_num)

    # find second number
    second_num = getLast(line)
    #print(second_num)

    # combine numbers, convert to int, add to array
    value.append(int(first_num+second_num))

# add all of the contents
print(array_sum(value))

