#file = open("input.txt", "r")
#txt = [x.strip("\n") for x in file.readlines()]
txt = open("input.txt", "r").readlines()
#print(txt)

num_lines = len(txt)-1 # index to 0
num_columns = len(txt[0])-1 # index to 0, skip newline
#print(num_lines, num_columns)

start_digit_i = None
end_digit_i = None

ratios = dict()

# if more than one, it's valid
valid = []

def isGear(character):
    # now, we only care if it's a gear
    return character=="*"

#print(isGear("."))
#exit()

def findAround(line_i, start_col_i, end_col_i):
    number = txt[line_i][start_col_i:end_col_i]

    #print("\tfinding here:", line_i, start_col_i, end_col_i, number)

    # one to the left
    start_col_i = start_col_i - 1
    if (start_col_i < 0):   # bounds checking
        start_col_i = 0
    # one to the right
    end_col_i = end_col_i +1
    if (end_col_i > num_columns):   # bounds checking
        end_col_i = num_columns
    
    # line above
    line = line_i - 1
    if (line >= 0): # bounds checking
        line_above = txt[line][start_col_i:end_col_i]
        #print("\tline_above:", line_above)
        for y, c in enumerate(line_above):
            # if this character is a gear, return the number and position
            if (isGear(c)):
                return number, (line, start_col_i+y)

    # line of, left of
    if (isGear(txt[line_i][start_col_i])):
        return number, (line_i, start_col_i)

    # line of, right of
    # go back one in this format (typically last one not included)
    #print("\t\tright", txt[line_i], end_col_i-1, txt[line_i][end_col_i-1])
    if (isGear(txt[line_i][end_col_i-1])):    
        return number, (line_i, end_col_i-1)

    # line below
    line = line_i +1
    if (line <= num_lines): # bounds checking
        for y, c in enumerate(txt[line][start_col_i:end_col_i]):
            # if this character is a symbol, return the number and position
            if (isGear(c)):
                return number, (line, start_col_i+y)
            
    # nothing found, return 0
    return 0


# go through each line
for l, line in enumerate(txt):
    #print("line", line)
    #print()

    # column index
    c = 0

    # loop through each column
    while (c < num_columns):
        #print("c", c)

        # find start of digit
        if line[c].isdigit():
            # to ignore middle digits
            if (start_digit_i == None):
                start_digit_i = c
                #print("start", start_digit_i)

        else:
            # find last digit
            if (start_digit_i != None):
                end_digit_i = c
                
                # if (c == 0): # bounds checking
                #     print(c, "LAST DIGIT")
                #     end_digit_i = 9
                #     #c = 9
                
                #print("end", end_digit_i)
                #print("\nNumber:", line[start_digit_i:end_digit_i])
                #print(c, start_digit_i, end_digit_i)
                
                found = findAround(l, start_digit_i, end_digit_i)
                
                # if it's found
                if found != 0:
                    gear = int(found[0])
                    loc = found[1]
                    #print("\tGear?:", gear, "\t", loc)
                    
                    # if the location has already been added to the ratios dictionary,
                    # then it is valid
                    if (loc in ratios):
                        valid.append(loc)
                        # the gear ratio is the old ratio times the new ratio
                        gear = ratios[loc] * gear
                    
                    # update that location with the gear ratio
                    ratios.update({loc: gear})

                #total += int(found)

                # reset
                start_digit_i = None

        c = c+1

#print("final ratios:", ratios)

# remove duplicates from valid array
valid = set(valid)
#print("Valid:", valid)

# sum all of the valid gear ratios
total = 0
for gr in valid:
    total += ratios[gr]

print("Total gear ratio:", total)