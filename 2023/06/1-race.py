file = open("input.txt", "r")
# strip newlines
txt = [x.strip("\n") for x in file.readlines()]
#txt = open("input.txt", "r").readlines()
#print(txt)

race = []

times = txt[0].split(" ")
distances = txt[1].split(" ")

for i, t in enumerate(times):
    # ignore text
    if i == 0:
        continue
    # put times and distances into array
    race.append([int(times[i]),int(distances[i])])

print("Race:", race)

margins = []

# go through each race
for r in race:
    time = r[0]
    recordDistance = r[1]

    winCount = 0

    # calculate distance traveled
    for holdTime in range(time):
        # speed equates to time held
        speed = holdTime
        # travel time is the remaining time after holding
        travelTime = time - holdTime
        # distance is speed x time
        distance = travelTime * speed
        # if distance is greater than record distance, count it as a win
        if (distance > recordDistance):
            winCount += 1
        #print(holdTime, distance)
    
    # add this race's winCount to margins to calculate total margin
    margins.append(winCount)
    
    #print(winCount)

# calculate total margins
margin = 1
for m in margins:
    margin *= m

print("margin:", margin)