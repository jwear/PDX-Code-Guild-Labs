import random

# Ask the user for three adjectives
adjectives = input('Give me three adjectives to describe a cat, separated by a comma: ')

# Split the adjectives into a list separated by a comma and print the list
x = adjectives.split(", ")
print(adjectives_list)

# Shuffle using random
random.shuffle(adjectives_list)

# Assign three variables to adjectives_list
ad1,ad2,ad3 = adjectives_list

print("The cat is {}, {}, {}.".format(ad1, ad2, ad3))
