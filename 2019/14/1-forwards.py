import time
import math

reactions =[]
with open("reactions.txt", "r") as fp:
    for line in (fp):
        # split into inputs and outputs
        in_out = line.strip('\n').split(" => ")

        # store in nested dict
        reaction = {}

        # only one output, store as:
        # {'chemical': amount}
        out_data = in_out[1].split(" ")
        out_dict = {out_data[1]: int(out_data[0])}
        reaction["out"] = out_dict

        # split the multiple inputs
        in_data = in_out[0].split(", ")
        in_dict = {}
        for i in in_data:
            i = i.split(' ')
            in_dict[i[1]] = int(i[0])
        reaction["in"] = in_dict

        reactions.append(reaction)

#print(reactions)

# loop through all of the reactions
for r in reactions:
    # if there's only one input, we can substitute the output
    if (len(r['in']) == 1):
        # get input data
        key_in = list(r['in'].keys())[0]
        value_in = r['in'][key_in]

        # get output data
        key_out = list(r['out'].keys())[0]
        value_out = r['out'][key_out]

        # multiply values to get new number of output
        new_amount = value_in * value_out

        # print for easier understanding
        print(value_in, "of", key_in, "=>", new_amount, "of", key_out)
        print()
    #else:
    #    print("longer")