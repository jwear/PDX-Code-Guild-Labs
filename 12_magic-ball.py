import random

print("Welcome to the Magic 8 Ball game!")

# List of Magic 8 Ball answers
answer = ['Nap time. Come back later.', 'No soup for you!', 'Serenity now!',
          'It\'s your lucky day!', 'You\'re the master of my domain']

# Predicts output of Magic 8 Ball
def prediction(question):
        print(random.choice(answer))

# Check if user wants to play again
def check_play(play_again):
    if play_again == 'yes':
        return True
    elif play_again == 'no':
        print('Goodbye!')
        return False

# Runs the game
while True:
    question = input('What is your question? ').lower()
    prediction(question)
    play_again = input('Would you like to play again - yes or no? ').lower()
    if not check_play(play_again):
        quit()
