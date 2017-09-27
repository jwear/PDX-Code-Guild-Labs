# Ask the user for a word or phrase
word = input("What is your word or phrase?: ").lower()
new_word = word.replace(' ', '')
reversed_word = ''.join(reversed(new_word))

# Check if the word or phrase is a palindrome
def palindrome(new_word):
    if new_word == reversed_word:
        return True
    else:
        False

# Print output
if palindrome(new_word) == True:
    print("Yes, your {} is a palindrome.".format(word))
else:
    print("Your {} is not a palindrome.".format(word))
