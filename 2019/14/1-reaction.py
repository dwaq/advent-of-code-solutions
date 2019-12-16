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

# store simplified inputs here
ingredients = {'FUEL': 1}
#ingredients = {'A': 10}
#ingredients = {'A': 10, 'B': 24, 'C': 40}
#ingredients = {'AB': 2}
#ingredients = {'BC': 3}
#ingredients = {'CA': 4}

# there may be leftover ingredients; store them here
leftover = {}

ore = 0

def substitute():
    global ore, ingredients, reactions

    # what is still left to reduce
    print("ingredients:", ingredients)
    
    # loop through those ingredients
    # starting with the largest value
    for i in sorted(ingredients, key=ingredients.get, reverse=True):
        #for i in ingredients:

        # this is the one we're working with
        print("current ingredient", i)

        # go through the reactions to find out how to make that ingredient
        for r in reactions:
            
            # found the reaction needed to make that ingredient
            if i in r['out']:
                # recipe for that ingredient
                print("recipe:", r)
                
                # inputs to make that ingredient
                for key, value in r['in'].items(): 
                    #print ("(key, value):", (key, value))
                    #print("data", ingredients[i],  r['out'][i], value)

                    # calculate how many inputs we need to make the current ingredient

                    # need ingredients[i] number of current ingredient
                    # divide by the amount that is made in one reaction (r['out][i])
                    # can't make a partial batch, so round up using ceil()
                    # then multiply by the amount of the new ingredients (value)
                    additional = math.ceil(ingredients[i] / r['out'][i]) * value
                    
                    print("Additional", additional, "of", key)

                    # ore is stored outside of ingredients{}
                    # so I know when ingredients are empty
                    if key == 'ORE':
                        ore += additional
                    # otherwise update the new ingredient
                    else:
                        
                        # check if the new ingredient is already present
                        existing = 0
                        if key in leftover:
                            existing = leftover[key]
                            print("Existing", existing, "of", key)
                            # remove so I don't double count it
                            del leftover[key]

                        # update the quantity of the ingredient
                        # if new, existing will be 0, so it will only equal to additional
                        ingredients[key] = existing + additional
                
                    # remove the used quantity of the old ingredient
                    # additional//value = multiplier
                    # r['out'][i] = recipe quantity
                    # multiply to get how many are made
                    # then remove old amount (ingredients[i]) to get current amount remaining
                    #print(additional, value, additional//value, r['out'][i], ingredients[i])
                    leftover[i] = ((additional//value) * r['out'][i]) - ingredients[i]

                # remove from ingredients list now
                del ingredients[i]

                
                print("new ingredients", ingredients)
                
                print("Leftover ingredients:", i, leftover)
                #print("number of ore", ore)
                
                #if (i == 'C'):
                #    exit()
                
                return


while (len(ingredients) > 0):
    substitute()
    #time.sleep(1)

    print ("number of ore:", ore)
    print()