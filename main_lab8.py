# Optional Coding, to create a txt file with the strings.
def create_quote_file():
    # creating a file to store values of employees
    file_list = ["we observe today not a victory", "of party but a celebration",
                 "of freedom symbolizing an end", "as well as a beginning",
                 "signifying renewal as well", "as change"]
    with open("quote.txt", "w") as file:
        for item in file_list:
            # write item on new line
            file.write(f'{item}\n')

    # When Iterating over x or something:
    """ Notes for myself to remember:
    for i in list: (simple vers),is the same as
    for i in range(len(list)): (anti-pattern vers), is the same as
    for i, e in enumerate(list): (most used vers)
    A 'pattern' is an idea of how to solve a problem of some class.
    An 'anti-pattern' is an idea not solving a problem because
    it would fail and is an attempt to solve it """


# 10-20-22 Notice: THIS CONCEPT IS ON EXAM2 ON THURS!!!
# Hints: You’ll need nested loops. The outer for loop should read
# one line from the file at a time and use the enumerate function
# (so you can keep track of which line you’re currently reading)

# Code Begins Here

words_per_l_dict = {}


def count_word_per_line(file):
    # all lines in file into a list
    lines_in_file_list = file.readlines()
    # assigning elements of the iterable & iterating over x
    # hint says to use enumerate
    for index, element in enumerate(lines_in_file_list):
        # remove newline character at the end and split it into words
        # lower() incase to include uppercase letters/words
        for word in lines_in_file_list[index].replace("\n", "").lower().split(" "):
            # check if word is already present in the dictionary
            if word in words_per_l_dict:
                # adds index to list
                words_per_l_dict[word].append(index + 1)
            else:
                # adds word in dict
                words_per_l_dict[word] = [index + 1]
    return words_per_l_dict  # return values,outside loop


def print_result(w_c_p_l):
    # print the dictionary
    for key, value in words_per_l_dict.items():
        # end = " " is to Print " "
        # instead newline at the end
        print(key, end=" ")
        for i in value:
            print(i, end=" ")
        print()


def main():
    create_quote_file()
    with open("quote.txt") as file:
        # import func to var, put var in parameter to print
        words_per_line = count_word_per_line(file)
        print_result(words_per_line)


main()
