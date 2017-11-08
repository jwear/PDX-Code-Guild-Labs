# Ask the user for original word or phrase and remove spaces
first = input('Please provide a word or phrase: ')
new_first = first.replace(' ', '')

# Ask the user for word or phrase to test and remove spaces
second = input('Please provide the word or phrase to test: ')
new_second = second.replace(' ', '')

# Function to convert original and test word or phrase into a list, sort, and test
def anagram_test(new_first, new_second):
    if sorted(list(new_first.lower())) == sorted(list(new_second.lower())):
        print('It is an anagram')
    else:
        print('Not an anagram')

anagram_test(new_first, new_second)
