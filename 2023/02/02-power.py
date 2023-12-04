txt = open("input.txt", "r").readlines()
#print(txt)

sum_of_powers = 0

# go through each line
for line in txt:
    # reset values
    num_red = 0
    num_green = 0
    num_blue = 0

    max_red = 0
    max_green = 0
    max_blue = 0

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

        # set the max to the larger of current vs past values
        max_red = max([num_red, max_red])
        max_green = max([num_green, max_green])
        max_blue = max([num_blue, max_blue])
    power = max_red * max_green * max_blue

    sum_of_powers += power

    print("\t#", game_id, "\tred:", max_red, "green:", max_green, "blue:", max_blue, "power:", power)    


print("Sum of Powers:", sum_of_powers)