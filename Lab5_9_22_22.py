"""You will write four functions (other than main)
-get_account: a function which calls the following three functions,
return in three variables.
-get_name: asks for and returns the user’s name
-get_email: asks for and returns the user’s email
-calculate_id: calculates and returns a new company ID for the user
After get_account has called these three functions and saved their
 return values, it should return all three."""

import random


def get_account():
    return f'Name: {get_name()} \nEmail: {get_email()} \nCompany ID: {calculate_id()}'


def get_name():
    name = input(f'Enter your name: ')
    return name


def get_email():
    email = input(f'Enter your email: ')
    print()
    return email


def calculate_id():
    id_val = random.randint(1111, 9999)
    return id_val


def main():
    print(get_account())


main()
