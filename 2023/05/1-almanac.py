file = open("input.txt", "r")
# strip newlines
txt = [x.strip("\n") for x in file.readlines()]
#txt = open("input.txt", "r").readlines()
#print(txt)


# starting here
seeds = []

# each map decoded into these
soil = []
fertilizer = []
water = []
light = []
temperature = []
humidity = []
location =  []


# decode each section of maps
def decodeText(dict):
    global l
    # skip 2 (map text & blank line)
    l += 2
    line = txt[l]
    
    # go until next blank line
    while (line != ""):
        decodeMap(line, dict)

        l += 1
        line = txt[l]

# decode each individual instruction
def decodeMap(line, dic):
    #print(line)

    # split into 3 numbers
    m = line.split(" ")
    # convert them to int
    m = [int(x) for x in m]
    # put them in the map array
    dic.append(m)

def followMap(dic):
    #print("\nmap")
    global seeds
    # go through each seed
    for i, s in enumerate(seeds):
        
        # get current seed
        seed = seeds[i]

        # go through each list
        for d in dic:
            # check if the seed is in the source range
            source_start = d[1]
            source_end = source_start + d[2]
            if (seed >= source_start and seed < source_end):
                # if it is, change the seed to the destination + offset
                destination = d[0]
                offset = seed - source_start
                # just reuse the seed and change destination when needed
                seeds[i] = destination + offset
            # if it's not in list, keep it the same (OK)

        #print(s, seeds[i])


# go through each line
l = 0

# get current line
line = txt[l]

#print(line[0:5])

# seeds
if (line[0:5] == "seeds"):
    seeds =  line[7:].split(" ")
    # convert to int
    seeds = list(map(int, seeds))
    # go to next map's data
    l +=1
    #print("seeds:", seeds)

# seed-to-soil map:
decodeText(soil)

# soil-to-fertilizer map:
decodeText(fertilizer)

#fertilizer-to-water map:
decodeText(water)

#water-to-light map:
decodeText(light)

#light-to-temperature map:
decodeText(temperature)

#temperature-to-humidity map:
decodeText(humidity)

#humidity-to-location map:
decodeText(location)


# map seeds to next one
followMap(soil)
followMap(fertilizer)
followMap(water)
followMap(light)
followMap(temperature)
followMap(humidity)
followMap(location)

print("Closest location:", min(seeds))