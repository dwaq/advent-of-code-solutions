txt = open("input.txt", "r").readlines()
#print(txt)

num_red = 0
num_green = 0
num_blue = 0

max_red = 12
max_green = 13
max_blue = 14

# add all the possible IDs together
possible_total = 0

# assume valid
game_valid = 1

# go through each line
for line in txt:
    # decode...

    # split game from instructions
    game = line.split(": ")
    # remove text "Game "(5)
    game_id = int(game[0][5:])
    #print(game_id)

    # instructions, strip newline
    instructions = game[1].strip("\n")
    # split at semicolon
    ins = instructions.split("; ")
    #print(ins)

    # go through each instruction
    for i in ins:
        # split at comma
        cubes = i.split(", ")
        #print(cubes)

        # split cubes into nums of colors
        # each time is one hand
        for cube in cubes:

            split = cube.split(" ")
            color = split[1]
            num = int(split[0])
            
            # decode colors
            if color == "red":
                num_red = num
            if color == "blue":
                num_blue = num
            if color == "green":
                num_green = num

        # check against maximums
        if (num_red <= max_red and num_green <= max_green and num_blue <= max_blue):
            game_valid = 1
        else:
            # once one hand is invalid, break
            game_valid = 0
            break
    
    # if valid, add to total
    if (game_valid == 1):
        print(game_id, "is valid")
        possible_total += game_id

    # reset counters
    num_red = 0
    num_green = 0
    num_blue = 0
    game_valid = 1

print("total:", possible_total)
