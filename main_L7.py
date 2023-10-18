# Optional Coding, to create a txt file with the strings.
def create_employee_file():
    # creating a file to store values of employees
    f_list = ["123 Bob Smith", "345 Anne Jones", "256 Carol Lee", "845 Steve Robert Anderson", "132 Jill Thompson"]
    textfile = open("Employees.txt", "w")
    with open("employees.txt", "w") as file:
        for item in f_list:
            # write item on new line
            file.write(f'{item}\n')


# Coding for the Problem Starts Here (BELOW):

# dictionary for lookup_employee
employee_list = {}  # key = id #, values = names in tuple
# parallel list for finding ID to the name
# creates 4 separate lists to compare, each goes per index
ID_list = []
First_n = []
Middle_n = []
Last_n = []


def lookup_employee(u_id):  # option 1, dictionary method
    with open("employees.txt") as file:
        for line in file:
            id_n, first, *middle, last = line.split()
            employee_list[id_n] = first, middle, last
    try:
        first, middle, last = employee_list.get(str(u_id))
        return f'ID: {str(u_id)}, Name: {first} {middle} {last}'
    except:
        return f'Employee not found'


def lookup_id(u_first, u_last):  # option2, parallel list method (idk dictionary)
    with open("employees.txt") as file:
        for line in file:
            id_n, first, *middle, last = line.split()
            ID_list.append(id_n)
            First_n.append(first)
            Middle_n.append(middle)
            Last_n.append(last)
    try:
        for i in range(len(First_n)) and range(len(Last_n)):
            if First_n[i].lower() == u_first.lower() and Last_n[i].lower() == u_last.lower():
                return f'ID: {ID_list[i]} , Name: {First_n[i]} {Middle_n[i]} {Last_n[i]}'
    except None:
        return f'ID not found'


def main():
    create_employee_file()
    while True:
        print("1 = Enter ID to Find Employee's Name")
        print("2 = Enter Name to Find Employee's ID")
        print("3 = Exits/Quits")
        try:  # must enter between 1-3
            user = input("Enter Option #: ")
            if user not in ['1', '2', '3']:
                print("Invalid! Input a number 1-3!")
                print()
            else:
                # option1, dictionary
                if int(user) == 1:
                    try:
                        u_id = int(input("Enter ID: "))
                        print(lookup_employee(u_id))
                        print()
                    except:
                        print("Error! Enter ID #'s.")
                # option2, parallel lists
                if int(user) == 2:
                    u_first = input("Enter First Name: ")
                    u_last = input("Enter Last Name: ")
                    print(lookup_id(u_first, u_last))
                    print()
                # option3, exits
                if int(user) == 3:
                    break
        except ValueError or KeyError:  # if entered value is a char/string
            print("Invalid! Input a number 1-3!")
            print()


main()
