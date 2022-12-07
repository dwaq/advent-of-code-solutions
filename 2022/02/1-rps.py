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
                case 'X':   # rock
                    score += 1
                    score += 3 # draw
                case 'Y':   # paper
                    score += 2
                    score += 6 # win
                case 'Z':   # scissor
                    score += 3
                    score += 0 # lose
        case 'B':   # paper
            match me:
                case 'X':   # rock
                    score += 1
                    score += 0 # lose
                case 'Y':   # paper
                    score += 2
                    score += 3 # draw
                case 'Z':   # scissor
                    score += 3
                    score += 6 # win
        case 'C':   # scissor
            match me:
                case 'X':   # rock
                    score += 1
                    score += 6 # win
                case 'Y':   # paper
                    score += 2
                    score += 0 # lose
                case 'Z':   # scissor
                    score += 3
                    score += 3 # draw



# go through each line
for line in txt:
    # format the line into your move and opponent's move
    guide = line.strip('\n').split(' ')
    getScore(guide[0], guide[1])
    print(guide, score)