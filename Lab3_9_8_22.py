"""
Write a Python program that continually
asks the user to enter two integers.

-If either value entered is not an integer,
inform them of this and ask again.
--Otherwise, add the integers and print the
result.
-Inside the loop, after the two numbers have
been added and displayed (or the user has
been informed that the input is bad),
ask the user if they would like to
perform another addition. If they enter
"no", the loop should exit.
-Hint: Use a while loop. The Boolean
expression it tests should evaluate to
True if the variable for the first number
contains the string “no” and False otherwise.
"""


def main():
    end_loop = ''
    while end_loop.lower() != "n":
        print()
        num = input("Enter number 1: ")
        num2 = input("Enter number 2: ")
        if num.isdigit() and num2.isdigit():
            sum_a = int(num) + int(num2)
            print("The sum is: ", sum_a)
            end_loop = input("Do you want to perform an another addition?'Y/N','N' exits: ")
        else:
            print("The both numbers must be an integer!")
            end_loop = input("Do you want to perform an another addition?'Y/N',Type 'N' to exits: ")


main()
