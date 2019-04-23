import sys

# how everything is looking now
diagram = [['.', '.', '.', '.'], ['.', '.', 'LG', '.'], ['HG', '.', '.', '.'], ['.', 'HM', '.', 'LM']]

# where elevator currently is
elevator = 1

# how to print without newline:
# http://stackoverflow.com/a/493399
def printDiagram(d):
    # start on 4th floor
    floor = 4
    for row in d:
        # print floor
        sys.stdout.write('F'+str(floor)+' ')
        
        # print where elevator is
        if (floor == elevator):
            sys.stdout.write("E ")
        else:
            sys.stdout.write(". ")
        
        # print each item in the row
        for i in row:
            # add a space to the period to match usual 2 character length
            if i == '.':
                i = ". "
            
            # print item and space seperator
            sys.stdout.write(i+' ')
        # need to flush when finished
        sys.stdout.flush()
        # move to new floor/row
        floor = floor - 1
        print

# converts elevator floor to diagram index
def l2i(elevator):
    return 4 - elevator
        
printDiagram(diagram)

print diagram[l2i(elevator)]

