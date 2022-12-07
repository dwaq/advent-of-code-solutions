txt = open("input.txt", "r").readlines()
#print(txt)

# store each elf's calories
elf = []
score = 0

def getScore(opponent, me):
    global score
    match opponent:
        case 'A':   # rock
            match me:
                case 'X':   # lose
                    score += 3 # scissor
                    score += 0 # lose
                case 'Y':   # draw
                    score += 1 # rock
                    score += 3 # draw
                case 'Z':   # win
                    score += 2 # paper
                    score += 6 # win
        case 'B':   # paper
            match me:
                case 'X':   # lose
                    score += 1 # rock
                    score += 0 # lose
                case 'Y':   # draw
                    score += 2 # paper
                    score += 3 # draw
                case 'Z':   # win
                    score += 3 # scissor
                    score += 6 # win
        case 'C':   # scissor
            match me:
                case 'X':   # lose
                    score += 2 # paper
                    score += 0 # lose
                case 'Y':   # draw
                    score += 3 # scissor
                    score += 3 # draw
                case 'Z':   # win
                    score += 1 # rock
                    score += 6 # win



# go through each line
for line in txt:
    # format the line into your move and opponent's move
    guide = line.strip('\n').split(' ')
    getScore(guide[0], guide[1])
    print(guide, score)