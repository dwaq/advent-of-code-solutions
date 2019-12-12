inputText = open("positions.txt", "r")

position = []
velocity = []

for line in inputText:
    # remove extra characters
    line = line.strip("<>\n")

    # split into x, y, z
    line = line.split(", ")

    data = []

    # remove x=, y=, and z= text
    # and convert to int
    for c in line:
        data.append(int(c[2:]))

    position.append(data)
    # each position also has a velocity starting at 0
    velocity.append([0,0,0])

print(position)
print(velocity)