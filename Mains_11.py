from Contacts_11 import Contact
import pickle


def load_contacts():
    """ Load the pickled contact dictionary from 'mydata.dat' and return it
    If the file does not exist, return an emtpy dictionary """
    try:
        with open('mydata.dat', 'rb') as file:
            contact_dictionary = pickle.load(file)
    except FileNotFoundError:
        contact_dictionary = {}
    return contact_dictionary


def save_contacts(contacts):
    """ Pickle 'contacts' and save it to 'mydata.dat' """
    with open('mydata.dat', 'wb') as file:
        pickle.dump(contacts, file)


def add(contacts):
    """ Ask the user for information about a Contact and add it to the 'contacts' dictionary """
    print("Adding a new contact\n\n")
    name = input("Name: ")

    if name in contacts:
        # Do not allow contacts with duplicate names
        print("A Contact with that name already exists in your phone book!")
        return

    email = input("Email: ")
    entry = Contact(name, email)

    # Add phone numbers to the Contact object until the user decides to stop
    while True:
        next_num = input("Enter a Phone Number (or q to stop): ")
        if next_num.lower() == 'q':
            break
        entry.add_number(next_num)

    # Add the new contact to the 'contacts' dictionary
    contacts[entry.name] = entry


def look_up(contacts):
    """ Display the information about the desired contact """
    name = input("Enter a name: ")
    if name in contacts:
        print(contacts[name])
    else:
        print("Name not found in phone book!")


def delete(contacts):
    """ Remove a given Contact from the 'contacts' dictionary """
    name = input("Enter a name: ")
    if name in contacts:
        contacts.pop(name)
    else:
        print("Name not found in phone book!")


def edit(contacts):
    name = input("Enter a name: ")
    if name in contacts:
        while True:
            # Ask the user what to do next
            choice = int(input("1) Remove Number 2) Add Number 3) Change Email 4) Change Name 5) Quit: "))
            if choice == 1:
                # remove number
                numb1 = input("Number to remove: ")
                contacts[name].remove_number(numb1)
                print("Number Removed!")
            elif choice == 2:
                # add number
                numb2 = input("Number to add: ")
                contacts[name].add_number(numb2)
                print("Number Added!")
            elif choice == 3:
                # change email
                e_c = input("Email to change: ")
                contacts[name].email = e_c
                print("Email Changed!")
            elif choice == 4:  # Need improvements here
                # change contact name
                """Since keys are what dictionaries use to lookup values,
                you can't really change them. The closest thing you can 
                do is to save the value associated with the old key, 
                delete it, then add a new entry with the replacement key 
                and the saved value"""
                name2 = input("Name to change: ")
                contacts[name2] = contacts.pop(name)
                print("Name Changed!")
            elif choice == 5:
                break
    else:
        print("Name not found in phone book!")


def main():
    contacts = load_contacts()

    while True:
        # Ask the user what to do next
        choice = int(input("1) Add a new Contact 2) Lookup a Contact 3) Remove a Contact. 4) Edit a Contact 5) Quit: "))
        if choice == 1:
            add(contacts)
        elif choice == 2:
            look_up(contacts)
        elif choice == 3:
            delete(contacts)
        elif choice == 4:
            edit(contacts)
        elif choice == 5:
            break
    save_contacts(contacts)


main()
