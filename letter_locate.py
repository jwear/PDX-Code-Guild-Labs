# Ask user for a word and which letter to find
word = input('Please provide a word: ')
letter = input('Which letter do you want to locate: ')

# Function to locate indices of letter in a word
def find_indices(word, letter, start=0, end=None):
    indices_list = []
    new_start = start
    while True:
        try:
            index = word.index(letter, new_start, end)
        except ValueError:
            return indices_list
        else:
            indices_list.append(index)
            new_start = index + len(letter)

print(find_indices(word, letter))
