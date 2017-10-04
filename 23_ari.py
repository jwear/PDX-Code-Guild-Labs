# Book directory
ari = {  '1' : 'geneology_of_morals.txt',
         '2' : 'gettysburg_address.txt',
         '3' : 'iliad.txt',
         '4' : 'jack_and_jill.txt',
         '5' : 'marketing_ipsum.txt',
         '6' : 'odyssey.txt',
         '7' : 'po.txt',
         '8' : 'the_room_with_the_little_door.txt'
}

# Prints book directory and prompts user for a selction
print('To compute its automated readability index, pick from one of the files below:\n')
for key, value in ari.items():
    print(key + " -", value)

print("""

or

q - Quit""")

selected = input('Your number selection: ')

# Function to find book in directory
def search_dict(selected):
    if selected in ari:
        selected_book = ari[selected]
        return selected_book
    else:
        quit()

selected_book = search_dict(selected)

# Opens and reads selected book
with open(selected_book, 'r', encoding='utf-8') as file:
    data_file = file.read()

# Function to count number of characters
def count_all(selected_book):
    sentences = data_file.count('.') + data_file.count('!') + data_file.count('?')
    characters = 0
    words = 0
    for line in data_file:
        words += len(line.split())
        characters += len(line)
    return characters, words, sentences

characters, words, sentences = count_all(selected_book)

# Function that calculates ARI score
def ari_conversion(characters, words, sentences):
    score = round((4.71 * (characters / words)) + (0.5 * (words / sentences)) - 21.43)
    return score

score = ari_conversion(characters, words, sentences)

# ARI scale dictionary
ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

# Function to look up age range and grade level
def lookup(score):
    if score in ari_scale:
        score = ari_scale[score]
        grade = ari_scale[score]['grade level']
        age = ari_scale[score]['ages']
        return grade, age
    elif score > 14:
        grade = ari_scale[14]['grade_level']
        age = ari_scale[14]['ages']
        return grade, age

grade, age = lookup(score)

# Final output
print("""
The ARI for the file, {}, is {}. This corresponds to a {} level of difficulty
that is suitable for an average person {} years old.""".format(selected_book, score, grade.lower(), age))
