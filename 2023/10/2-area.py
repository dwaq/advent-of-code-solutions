file = open("input.txt", "r")
# strip newlines
txt = [x.strip("\n") for x in file.readlines()]
#txt = open("input.txt", "r").readlines()
#print(txt)

puzzle = []
# split lines into characters
for line in txt:
    puzzle.append([x for x in line])

#print(puzzle)

# hardcode starting point
# (0,0) is top left
# x is left to right (line)
# y is up to down (column)

# keep track of where we went (can also be used for step counter)
# this is the actual position of "S"
history = [(55,38)]

# start above S ("|")
# so we don't have to manually check all 4 directions
x, y = 55, 37

#print(puzzle[y][x])

def move(p):
    global x, y

    # last position
    last = history[-1]
    lx, ly = last

    #print(puzzle[ly][lx],"was at (", lx, ",", ly, ")")
    #print(puzzle[y][x]  ,"    at (", x,  ",", y,  ")\n")

    # append current to history for next time
    history.append((x,y))

    match p:
        # a vertical pipe connecting north and south
        case "|":
            # can only go up or down or right
            y = y+1 if ly < y else y-1
        # a horizontal pipe connecting east and west.
        case "-":
            # can only go left or right
            x = x+1 if lx < x else x-1
        # a 90-degree bend connecting north and east.
        case "L":
            # from right, go up
            if (lx > x):
                y -= 1
            # from top, go right
            else:
                x += 1
        # a 90-degree bend connecting north and west.
        case "J":
            # from left, go up
            if (lx < x):
                y -= 1
            # from top, go left
            else:
                x -= 1
        # a 90-degree bend connecting south and west.
        case "7":
            # from left, go down
            if (lx < x):
                y += 1
            # from bottom, go left
            else:
                x -= 1
        # a 90-degree bend connecting south and east.
        case "F":
            # from right, go down
            if (lx > x):
                y += 1
            # from bottom, go right
            else:
                x += 1
        # ground; there is no pipe in this tile.
        case ".":
            print("Shouldn't be here")
            exit()
        # the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
        case "S":
            print("Found exit")
            exit()

        

# step along the path until we make it back to "S"
while (puzzle[y][x] != "S"):
    # use the character of the current position to move to the next
    move(puzzle[y][x])
    #exit()


#print("max distance:", int(len(history)/2))

for px, row in enumerate(puzzle):
    for py, col in enumerate(row):
        # print @ on path
        if (py, px) in history:
            print("@", end ="")
        # print . outside of path
        else:
            print(".", end ="")
    print()
