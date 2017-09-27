# Ask user for credit card number
cc_num = list(input('Please enter your credit card number: '))

# Last digit to check
check_last_digit = cc_num[-1]

# Function to remove last item
def remove_last(cc_num):
    cc_num.pop()
    return cc_num

# Function to reverse digits
def reverse(cc_num):
    cc_num.reverse()
    return cc_num

# Function to double every other element
def double(cc_num):
    doubled_list = []
    for index, num in enumerate(cc_num):
        if index % 2 == 0:
            doubled_list.append(2 * int(num))
        else:
            doubled_list.append(int(num))
    return doubled_list

# Function to subract nine for numbers over nine
def subtract(doubled_list):
    subtracted_list = []
    for index, num in enumerate(doubled_list):
        if num > 9:
            subtracted_list.append(num - 9)
        else:
            subtracted_list.append(num)
    return subtracted_list

# Function to sum all values
def add_all(subtracted_list):
    added_num = sum(subtracted_list)
    return added_num

# Function that takes the second digit of the sum and compares if cc is valid or invalide
def validate(added_sum):
    new_num = str(added_num)
    print('Second digit is ' + new_num[-1])
    print('Check digit is: ' + check_last_digit)
    if new_num[-1] == check_last_digit:
        print('Valid!')
    else:
        print('Invalid!')

# Print steps to validate
print(cc_num)

print(remove_last(cc_num))

removed_list = remove_last(cc_num)
print(reverse(cc_num))

reversed_list = reverse(cc_num)
print(double(cc_num))

doubled_list = double(reversed_list)
print(subtract(doubled_list))

subtracted_list = subtract(doubled_list)
print(add_all(subtracted_list))

added_num = add_all(subtracted_list)
print(validate(added_num))
