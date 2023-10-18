"""
Write a Python script that has four functions defined on it.
    main
    print_employee_info
    print_employee_name
    print_employee_id
Your program should start by calling main.
    From main, call the print_employee_info function.
        From print_employee_info, call the following two functions:
        print_employee_name.
            In this function, print the name “Bob Smith”.
        print_employee_id.
            In this function, print the value “123abcd”
"""


def print_employee_name():
    print("Bob Smith")


def print_employee_id():
    print("123abcd")


def print_employee_info():
    print_employee_name()
    print_employee_id()


def main():
    print_employee_info()


main()
