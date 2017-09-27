"""

>>> locate('l', 'hello')
[2, 3]

>>> locate('b', 'bannanas')
[0]

>>> locate('i', 'mississippi')
[1, 4, 7, 10]
"""
# Ask user for a word and which letter to find
if __name__ == "__main__":
    w = input('Please provide a word: ').lower()
    l = input('Which letter do you want to locate: ').lower()
    print(locate(word, letter))

# Function to locate indices of letter in a word
def locate(letter, word, start=0, end=None):
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
