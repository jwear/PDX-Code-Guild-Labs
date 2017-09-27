# Function to sum original input numbers from user
def sum1(num_int):
    sum1_result = sum(num_int)
    return sum1_result

def check_digit(sum1_result):
    sum1_result_str = str(sum1_result)
    return len(sum1_result_str) > 1

# Function to sum the result from sum1
def sum2(sum1_result):
    num_int2 = list(map(int, str(sum1_result)))
    sum2_result = sum(num_int2)
    return sum2_result

# Ask user for numbers to shrink and convert to integers
numbers = input('Please provide the numbers to shrink: ')
num_int = list(map(int, numbers))

# Runs the program to shrink
while True:
    sum1_result = sum1(num_int)
    if check_digit(sum1_result):
        sum2_result = sum2(sum1_result)
        print(sum2_result)
    else:
        print(sum1_result)
    quit()
