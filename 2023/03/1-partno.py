#file = open("input.txt", "r")
#txt = [x.strip("\n") for x in file.readlines()]
txt = open("input.txt", "r").readlines()
#print(txt)

num_lines = len(txt)-1 # index to 0
num_columns = len(txt[0])-1 # index to 0, skip newline
#print(num_lines, num_columns)

start_digit_i = None
end_digit_i = None

total = 0

def isSymbol(character):
    #print("isSymbol", character, not(character.isdigit() or character=="."))
    # if not digit, or period
    return not(character.isdigit() or character==".")

#print(isSymbol("."))
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
        for c in line_above:
            # if this character is a symbol, return the number to add to the sum
            if (isSymbol(c)):
                return number

    # line of, left of
    if (isSymbol(txt[line_i][start_col_i])):
        return number

    # line of, right of
    # go back one in this format (typically last one not included)
    #print("\t\tright", txt[line_i], end_col_i-1, txt[line_i][end_col_i-1])
    if (isSymbol(txt[line_i][end_col_i-1])):    
        return number

    # line below
    line = line_i +1
    if (line <= num_lines): # bounds checking
        for c in txt[line][start_col_i:end_col_i]:
            # if this character is a symbol, return the number to add to the sum
            if (isSymbol(c)):
                return number
            
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
                #print("\tFound?:", found)

                total += int(found)

                # reset
                start_digit_i = None

        c = c+1

    #exit()
print("total:", total)