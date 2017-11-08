name = input('What is your name: ')
age = input('How old are you: ')

age_in_a_year = int(age) + 1

banner = ("*" * len(name))

print("{}{}{}\nYou will be {} years old in a year.".format(banner, name, banner, age_in_a_year))
