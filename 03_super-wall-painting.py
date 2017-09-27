from math import ceil

width = int(input('What is the width of the wall? '))
height = int(input('What is the height of the wall? '))
per_gallon_cost = float(input('How much a gallon of paint costs? '))
num_coat = int(input('How many coats of paint will you use? '))

area_needed = (width * height) * num_coat
gallons_needed = ceil(area_needed / 400)
full_cost = gallons_needed * per_gallon_cost

print("You will need to buy {} gallons of paint. It will cost you ${} to paint the wall."
.format(gallons_needed, full_cost))
