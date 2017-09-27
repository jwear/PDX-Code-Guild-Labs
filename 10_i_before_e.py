# Exception words in a list
exception_list = ['agreeing', 'science', 'disagreeing', 'caffeine', 'beige', 'vein', 'weird']

# Checks if it follows the rule or not and if it is an exception
def check_rule(word):
    if word in exception_list:
        print("{} is an exception to the rule".format(word))
    else:
        print("{} does follow the rule".format(word))

# Checks if user wants to
def check_new_word(check_again):
    if check_again == 'yes':
        return True
    elif check_again == 'no':
        print('Goodbye!')
        return False

# Runs the program
while True:
    word = input("Please provide a single English word: ").lower()
    check_rule(word)
    check_again = input('Would you like to check another word - yes or no? ').lower()
    if not check_new_word(check_again):
            quit()
