# Ask user for a word
word = input('Word? ')

# Convert to Pig Latin
if word[0] in ['a', 'e', 'i', 'o', 'u']:
    new_word = word[0] + "yay"
    print('{} in Piglatin is {}'.format(word, new_word))
else:
    new_word = word[1:] + word[0] + "ay"
    print('{} in Piglatin is {}'.format(word, new_word))
