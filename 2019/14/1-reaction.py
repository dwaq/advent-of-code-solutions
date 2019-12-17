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

# store each loop's output here
new_ingredients = {}

# store leftovers here
leftover = {}

def substitute():
    global reactions, ingredients, leftover, new_ingredients

    # what is still left to reduce
    print("ingredients:", ingredients)
    
    # loop through those ingredients
    # starting with the largest value
    #for ingredient in sorted(ingredients, key=ingredients.get, reverse=True):
    for ingredient in ingredients:

        # this is the one we're working with
        print("current ingredient", ingredient)

        # go through the reactions to find out how to make that ingredient
        for reaction in reactions:
            
            # found the reaction needed to make that ingredient
            if ingredient in reaction['out']:
                # recipe for that ingredient
                print("recipe:", reaction)
                
                # inputs to make that ingredient
                for key, value in reaction['in'].items(): 
                    #print ("(key, value):", (key, value))
                    #print("data", ingredients[ingredient],  reaction['out'][ingredient], value)

                    # calculate how many inputs we need to make the current ingredient

                    # need this many of current ingredient
                    current_qty = ingredients[ingredient]
                    # amount that is made in one reaction
                    new_qty = reaction['out'][ingredient]

                    # use any leftover ingredients (if there are any)
                    needed_qty = current_qty
                    if key in leftover:
                        needed_qty -= leftover[key]

                    # can't make a partial batch, so round up using ceil()
                    # then multiply by the amount of the new ingredients (value)
                    additional = math.ceil(needed_qty / new_qty) * value
                    
                    print("\tAdditional", additional, "of", key)
                    print("\tQTY:", current_qty, new_qty, value, additional)

                    # check if the new ingredient is already present
                    if key in new_ingredients:
                        new_ingredients[key] += additional
                    # update the quantity of the ingredient
                    else:
                        new_ingredients[key] = additional
                
                    # remove the used quantity of the old ingredient
                    leftover[ingredient] = current_qty - new_qty

                print("Leftover ingredients:", leftover)
                print()

    print("New ingredients", new_ingredients)
    
    print()



substitute()
while (len(new_ingredients) > 0):
    time.sleep(1)
    print()
    ingredients = new_ingredients.copy()
    new_ingredients.clear()
    substitute()

print ("number of ore:", ingredients['ORE'])
print()