import math

# As input, FFT takes a list of numbers
#signal = "12345678"
#signal = "80871224585914546619083218645595"
#signal = "19617804207202209144916044189917"
#signal = "69317163492948606335995924319873"
signal = "59728776137831964407973962002190906766322659303479564518502254685706025795824872901465838782474078135479504351754597318603898249365886373257507600323820091333924823533976723324070520961217627430323336204524247721593859226704485849491418129908885940064664115882392043975997862502832791753443475733972832341211432322108298512512553114533929906718683734211778737511609226184538973092804715035096933160826733751936056316586618837326144846607181591957802127283758478256860673616576061374687104534470102346796536051507583471850382678959394486801952841777641763547422116981527264877636892414006855332078225310912793451227305425976335026620670455240087933409"

# convert signal into a list of ints
sequence = [int(digit) for digit in signal]

#print(sequence)

# this is the pattern that everything is multiplied against
basePattern = [0, 1, 0, -1]

# number of rounds to test
rounds = 100

# FFT operates in repeated phases (number of rounds)
for phase in range(1, rounds+1):
    #print(phase)

    # a new list is constructed with the same length as the input list
    newList = [None] * len(sequence)

    # do some data manipulation on each element in the sequence
    for whichElement, element in enumerate(range(len(sequence))):
        # start at 1 instead of 0
        whichElement+=1

        # Then, repeat each value in the pattern a number of times equal to the position in the output list being considered.
        pattern = []
        # take each value in the pattern
        for p in basePattern:
            # repeat it the number of times
            for _ in range(whichElement):
                pattern.append(p)
        
        #print(whichElement, pattern)
        
        # if we need more digits
        if (len(pattern) < (len(newList) + whichElement) ):
            # make pattern as long as the signal, so each digit can be multiplied
            pattern *= math.ceil((len(newList) + whichElement) / len(pattern))
    
        #print(whichElement, pattern[whichElement-1:len(newList)+whichElement])

        # Each element in the new list is built by multiplying every value in the input list by a value in a repeating pattern and then adding up the results.
        elementSum = 0
        for digit in range(len(sequence)):
            # When applying the pattern, skip the very first value exactly once. (In other words, offset the whole pattern left by one.)
            #print(str(sequence[digit])+'*'+ str(pattern[digit + 1]), '\t+ ', end='')
            elementSum += sequence[digit] * pattern[digit + 1]

        # absolute removes the negative sign
        # %10 gets the last digit
        newDigit = abs(elementSum) % 10

        #print('\x08\x08=',newDigit)

        # add that digit to the new list
        newList[element] = newDigit

    # convert array to number (for printing)
    sig = 0
    # only want first 8 digits
    for n in newList[:8]:
        sig = (sig*10) + n

    print("After", phase, "phase:", sig)

    # make this list the sequence for the next phase
    sequence = newList