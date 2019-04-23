#inp = open('day9.in').read().strip()

inp = "(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN"

part2 = False

def decompress(s):
    if '(' not in s:
        return len(s)
    ret = 0
    while '(' in s:
        ret += s.find('(')
        s = s[s.find('('):]
        #print s
        marker = s[1:s.find(')')].split('x')
        s = s[s.find(')') + 1:]
        #print s
        if part2:
            print s[:int(marker[0])], int(marker[1])
            ret += decompress(s[:int(marker[0])]) * int(marker[1])
        else:
            ret += len(s[:int(marker[0])]) * int(marker[1])
        s = s[int(marker[0]):]
    ret += len(s)
    return ret

#print decompress(inp)
part2 = True
print decompress(inp)  