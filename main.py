def add_numbers_write():
    while True:
        num1 = input("Enter number 1: ")
        if num1 == 'q':
            view_numbers_read()
            break
        num2 = input("Enter number 2: ")
        if num2 == 'q':
            view_numbers_read()
            break
        sum_i = int(num1) + int(num2)
        sum_s = str(sum_i)
        file_string_equation = num1 + " + " + num2 + " = " + sum_s
        with open("data//results.txt", "a") as file:
            file.write(file_string_equation + "\n")


def view_numbers_read():
    print()
    print("Your Sum Equations: ")
    with open("data//results.txt", "r") as file:
        for file_string_equation in file.readlines():
            print(file_string_equation, end="")


# continued on next slide
def main():
    add_numbers_write()


main()
