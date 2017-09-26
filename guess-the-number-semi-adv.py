from random import randint
import time

# Asks the user for his or her name and difficulty level
def gather_info():
    n = input('Hello! What is your name? ')
    d = input('What level of difficulty (easy, medium, hard)? ')
    return n, d

# Greets the user with a banner
def greet(n):
    banner = ("*" * len(name))
    print("{}Let's get started with the guessing game, {}!{}".format(banner, name.capitalize(), banner))

# Computer chooses a random number based on difficulty level
def choose_compuer_number(difficulty):
    if difficulty.lower() == 'easy':
        comp_random_number = randint(1, 100)
        print("I'm thinking of a number between 1 and 100.")
    elif difficulty.lower() == 'medium':
        comp_random_number = randint(1, 125)
        print("I'm thinking of a number between 1 and 125.")
    else:
        comp_random_number = randint(1, 150)
        print("I'm thinking of a number between 1 and 150.")
    return comp_random_number

# Function to check guessed number against computer number
def number_check(user_number, comp_random_number, count):
    if user_number > comp_random_number:
        print('Too high!')
    elif user_number < comp_random_number:
        print('Too low!')
    else:
        print('Awesome job! You guessed my number correctly in {} guesses.'.format(count))


# Check win
def check_win(user_number, comp_random_number):
    if user_number == comp_random_number:
        q = input('Would you like to play again?: ').lower()
        count = 1
        if q in ['yes', 'y']:
            for x in list(range(3))[::-1]:
                print('New game in {}'.format(x))
                time.sleep(1)
            return True, True
        elif q in ['no', 'n']:
            print("Goodbye!")
            return False, False
# Asks user to guess the number and computer checks until correct and keeps score

name, difficulty = gather_info()
game = True
while game:
    count = 1
    greet(name)
    comp_random_number = choose_compuer_number(difficulty)
    running = True
    while running:
        print('Guess number: {}'.format(count))
        user_number = int(input('Please guess the number: '))
        time.sleep(2)
        number_check(user_number, comp_random_number, count)
        count += 1
        check_win(user_number, comp_random_number)
        game, running
