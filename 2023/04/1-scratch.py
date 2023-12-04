txt = open("input.txt", "r").readlines()
#print(txt)

score = 0

# go through each line
for line in txt:
    match = 0

    details = line.split(": ")
    card = details[0][4:]
    numbers = details[1].strip("\n").split(" | ")
    winning = numbers[0].split(" ")
    mynums = numbers[1].split(" ")

    #print(card)

    for num in mynums:
        if (num) in winning:
            match += 1
            #print ("\t",num)

    #print("\t\tmatch", match)
    card_score = int(pow(2, match-1))
    #print("\t\tscore", card_score)
    score += card_score

print("total score", score)