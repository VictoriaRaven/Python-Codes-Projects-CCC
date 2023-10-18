class Contact:

    """ Represents a Contact in the user's phone book. Each contact has a name, email, and list of phone numbers """
    def __init__(self, name, email=None):
        self._name = name
        self._email = email
        self._phone_numbers = []


    @property
    def name(self):
        return self._name

    @property
    def phone_numbers(self):
        return self._phone_numbers

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        self._email = new_email

    def add_number(self, phone_number):
        """ Add 'phone_number' to this Contact's list of phone numbers """
        if phone_number in self._phone_numbers:
            print("That number is already in the list!")
        else:
            self._phone_numbers.append(phone_number)

    def remove_number(self, phone_number):
        """ Removes 'phone_number' from this Contact's list of phone numbers, if it exists """
        if phone_number in self._phone_numbers:
            self._phone_numbers.remove(phone_number)

    def __str__(self):
        return_string = f'Name: {self._name}\n'
        return_string += "Numbers: "
        for num in self._phone_numbers:
            return_string += f'{num} '
        return_string += '\n'
        if self._email is not None:
            return_string += f'Email: {self._email}\n'

        return return_string
