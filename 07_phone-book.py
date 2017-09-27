contact = {
    'julie': {'f_name': 'Julie', 'l_name': 'Wear', 'phone': 773444888},
    'mary': {'f_name': 'Mary', 'l_name': 'Siy', 'phone': 312555999},
    }

# Ask user for full contact information to create or update
def gather_info():
    f_name = input('First name: ')
    l_name = input('Last name: ')
    phone = input('Phone: ')
    return f_name, l_name, phone

# Ask user which contact to find, update, or delete
def gather_info_rud():
    f_name = input('First name: ')
    return f_name

# Create a contact
def create(f_name, l_name, phone):
    contact[f_name.lower()] = {'f_name': f_name.capitalize(), 'l_name': l_name.capitalize(), 'phone': phone}
    print(contact)

# Find a contact
def find(f_name):
    print(contact[f_name.lower()]['f_name'])
    print(contact[f_name.lower()]['l_name'])
    print(contact[f_name.lower()]['phone'])

# Delete a contact
def delete(f_name):
    del contact[f_name]
    print(contact)

# Ask the user to create, find, update, delete, print, or exit
running = True
while running:
    cmd = input('Would you like to create, find, update, delete, print, or exit: ')
    if cmd == 'create':
        f_name, l_name, phone = gather_info()
        create(f_name, l_name, phone)
    elif cmd == 'find':
        f_name = gather_info_rud()
        find(f_name)
    elif cmd == 'update':
        f_name = gather_info_rud()
        print('Previous contact information was deleted.')
        delete(f_name)
        print('Now it is time to get new information about your contact.')
        f_name, l_name, phone = gather_info()
        create(f_name, l_name, phone)
    elif cmd == 'delete':
        f_name = gather_info_rud()
        delete(f_name)
    elif cmd == 'print':
        print(contact)
    elif cmd == 'exit':
        break
    else:
        print('Invalid entry. Please try again.')
