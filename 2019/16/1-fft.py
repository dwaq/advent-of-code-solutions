import math

#As input, FFT takes a list of numbers. In the signal you received (your puzzle input), each number is a single digit: data like 15243 represents the sequence 1, 5, 2, 4, 3.
#signal = "12345678"
#signal = "80871224585914546619083218645595"
#signal = "19617804207202209144916044189917"
#signal = "69317163492948606335995924319873"
signal = "59728776137831964407973962002190906766322659303479564518502254685706025795824872901465838782474078135479504351754597318603898249365886373257507600323820091333924823533976723324070520961217627430323336204524247721593859226704485849491418129908885940064664115882392043975997862502832791753443475733972832341211432322108298512512553114533929906718683734211778737511609226184538973092804715035096933160826733751936056316586618837326144846607181591957802127283758478256860673616576061374687104534470102346796536051507583471850382678959394486801952841777641763547422116981527264877636892414006855332078225310912793451227305425976335026620670455240087933409"

sequence = [int(digit) for digit in signal]

#print(sequence)

basePattern = [0, 1, 0, -1]

# number of rounds to test
rounds = 100

for phase in range(1, rounds+1):
    #print(phase)

    #FFT operates in repeated phases. In each phase, a new list is constructed with the same length as the input list. This new list is also used as the input for the next phase.
    newList = [None] * len(sequence)



    # Each element in the new list is built by multiplying every value in the input list by a value in a repeating pattern and then adding up the results.
    # So, if the input list were 9, 8, 7, 6, 5 and the pattern for a given element were 1, 2, 3,
    # the result would be 9*1 + 8*2 + 7*3 + 6*1 + 5*2 (with each input element on the left and each value in the repeating pattern on the right of each multiplication).
    # Then, only the ones digit is kept: 38 becomes 8, -17 becomes 7, and so on.
    for whichElement, element in enumerate(range(len(sequence))):
        # start at 1 instead of 0
        whichElement+=1

        # each digit of the pattern in repeated by the digit's index
        pattern = []
        for p in basePattern:
            #print(whichElement)
            for count in range(whichElement):
                pattern.append(p)
        
        #print(whichElement, pattern)
        
        # if we need more digits
        if (len(pattern) < (len(newList) + whichElement) ):
            # make pattern as long as the signal, so each digit can be multiplied
            pattern *= math.ceil((len(newList) + whichElement) / len(pattern))
    
        #print(whichElement, pattern[whichElement-1:len(newList)+whichElement])

        elementSum = 0

        #for digit in range(len(sequence)):
        #    print(pattern[digit], end='')
        #print()

        for digit in range(len(sequence)):
            #print(str(sequence[digit])+'*'+ str(pattern[digit + 1]), '\t+ ', end='')
            elementSum += sequence[digit] * pattern[digit + 1]

        newDigit = abs(elementSum) % 10

        #print('\x08\x08=',newDigit)

        newList[element] = newDigit

    # convert array to number
    sig = 0
    # only want first 8 digits
    for n in newList[:8]:
        sig = (sig*10) + n

    print("After", phase, "phase:", sig)

    sequence = newList

    # While each element in the output array uses all of the same input array elements, the actual repeating pattern to use depends on which output element is being calculated. The base pattern is 0, 1, 0, -1.
    # Then, repeat each value in the pattern a number of times equal to the position in the output list being considered.
    # Repeat once for the first element, twice for the second element, three times for the third element, and so on.
    # So, if the third element of the output list is being calculated, repeating the values would produce: 0, 0, 0, 1, 1, 1, 0, 0, 0, -1, -1, -1.

    # When applying the pattern, skip the very first value exactly once. (In other words, offset the whole pattern left by one.)
    # So, for the second element of the output list, the actual pattern used would be: 0, 1, 1, 0, 0, -1, -1, 0, 0, 1, 1, 0, 0, -1, -1, ....

    # After using this process to calculate each element of the output list, the phase is complete, and the output list of this phase is used as the new input list for the next phase, if any.
