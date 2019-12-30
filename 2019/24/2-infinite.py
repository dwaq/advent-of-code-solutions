# store state
state = []
with open("level.txt", "r") as fp:
    for f in (fp):
        line = f.strip('\n')
        # split line into tiles
        state.append([l for l in line])

# size of array (X & Y)
size = 5

# contents of cell
bug = '#'
empty = '.'
grid = '?'

# print the layout nicely
def prettyPrint(a):
    for x in a:
        for y in x:
            print(y,end='')
        print()

# count each cell's adjacent bugs
def countAdjacent(p):
    global state, newState

    # split p into x and y
    x = p//size
    y = p%size
    #print((x,y))

    adjacent = 0

    # first check that each direction is within bounds
    # then add to total if it's a bug
    # above
    if (y+1 < size):
        adjacent += (state[x][y+1] == bug)
    # below
    if (y-1 >= 0):
        adjacent += (state[x][y-1] == bug)  
    #  right
    if (x+1 < size):
        adjacent += (state[x+1][y] == bug)  
    # left
    if(x-1 >= 0):
        adjacent += (state[x-1][y] == bug)

    # "A bug dies (becoming an empty space) unless there is exactly one bug adjacent to it.""
    # check if it's a bug
    if (state[x][y] == bug):
        # it lives!
        if (adjacent == 1):
            newState[x][y] = bug
        # it dies!
        else:
            newState[x][y] = empty
    # "An empty space becomes infested with a bug if exactly one or two bugs are adjacent to it.""
    else:
        # infested!
        if(adjacent == 1 or adjacent == 2):
            newState[x][y] = bug
        # stays empty
        else:
            newState[x][y] = empty

# for easier storage and comparisons, convert array to a string
def arrayToString(a):
    s = ''
    for x in a:
        for y in x:
            s+=y
    return s

# https://thispointer.com/python-3-ways-to-check-if-there-are-duplicates-in-a-list/
def checkIfDuplicates(listOfElements):
    ''' Check if given list contains any duplicates '''    
    for elem in listOfElements:
        if listOfElements.count(elem) > 1:
            return True
    return False

# formula to calculate powers of cells
def calculateBiodiversity(a):
    rating = 0

    for p in range(25):
        points = 2**p

        # split p into x and y
        x = p//size
        y = p%size

        if(a[x][y] == bug):
            rating += points

    print("\nBiodiversity rating:", rating)
    exit()

# store old states for later comparision
stateStorage = []

print("Initial state:")
prettyPrint(state)
stateStorage.append(arrayToString(state))

# test until it matches
m = 1
while(True):
    print("\nAfter", m, "minutes:")

    # create new array to fill with data
    newState = [[None for i in range(size)] for j in range(size)]
    
    # test each cell
    for i in range(size*size):
        countAdjacent(i)

    # print it
    prettyPrint(newState)
    
    # store it
    stateStorage.append(arrayToString(newState))

    # check if there's been a repeat
    if (checkIfDuplicates(stateStorage) == True):
        calculateBiodiversity(newState)

    # update the state for the next round
    state = newState

    # count up the minutes
    m+=1