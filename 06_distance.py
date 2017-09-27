# Conversion function
def conversion(distance, initial_unit, target_unit):
    if initial_unit.lower() == 'mi':
        if target_unit.lower() == 'km':
            return distance * 1.60934
        elif target_unit.lower() == 'ft':
            return distance * 5280
        else:
            return distance * 1609.34
    if initial_unit.lower() == 'km':
        if target_unit.lower() == 'mi':
            return distance * 0.621371
        elif target_unit.lower() == 'ft':
            return distance * 3280.84
        else:
            return distance * 1000
    if initial_unit.lower() == 'ft':
        if target_unit.lower() == 'mi':
            return distance * 0.000189394
        elif target_unit.lower() == 'km':
            return distance * 0.0003048
        else:
            return distance * 0.3048
    if initial_unit.lower() == 'm':
        if target_unit.lower() == 'mi':
            return distance * 0.000621371
        elif target_unit.lower() == 'km':
            return distance * 0.001
        else:
            return distance * 3.28084

# Print instructions
print("Please enter a distance and the units in either mi, m, km, or ft to convert.")

# User inputs
distance = int(input('Enter a distance: '))
initial_unit = input('Enter units: ')
target_unit = input('Enter target units: ')

# Print results
print("{} {} is {} {}".format(distance, initial_unit, conversion(distance, initial_unit, target_unit), target_unit))
