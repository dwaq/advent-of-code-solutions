instructions = []

x = 0
y = 0

with open('input.txt', 'rb') as f:
    # break into pieces
    for piece in f:
        for i in piece:
            instructions.append(i)
            y = y + 1
        x = x + 1

print instructions