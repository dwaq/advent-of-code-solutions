#example = "(3x3)XYZ"
#example = "X(8x2)(3x3)ABCY"
example = "(27x12)(20x12)(13x14)(7x10)(1x12)A"
#example = "A(2x2)BCD(2x2)EFG"


def uncompress(example):
    # find location of '('
    marker_1 = example.index('(')
    # find location of ')'
    marker_2 = example.index(')')
    # split into two numbers, seperated by 'x'
    marker = example[marker_1+1:marker_2]
    marker = marker.split('x')
    num_chars = int(marker[0])
    num_times = int(marker[1])
    #print num_chars, num_times
    # perform calculation on following data
    # get characters to repeat (num_chars after parenthesis)
    char_to_repeat = example[marker_2+1:marker_2+1+num_chars]
    # repeat them num_times
    char_to_insert = char_to_repeat*num_times
    #insert them after the parenthesis and overwrite what's been repeated
    #print example[:marker_1], char_to_insert, example[marker_2+1+num_chars:]
    new_string = example[:marker_1] + char_to_insert + example[marker_2+1+num_chars:]
    return new_string


# true as long as there's still markers in the text
while ('(' in example):
    example = uncompress(example)
    print example


print "final:", example, len(example)

