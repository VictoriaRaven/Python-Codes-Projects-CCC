book_dictionary = {}


def add_book():
    book_title = input("Enter book title: ")
    b_copies = input("Enter book copies: ")
    if book_title in book_dictionary:
        print("That Book Title exists and will update copies!")
        book_data = book_dictionary[book_title]
        book_data["copies"] = b_copies
        print("Book copy number updated!")
    else:
        book_dictionary[book_title] = {"name": book_title, "copies": b_copies}


def view_book():
    for book_title, book_info in book_dictionary.items():
        print(f'Book Title: {book_info["name"]} Copies: {book_info["copies"]}')


def find_book():  # need to find only one title!
    book_t = input("Enter book title: ")
    try:
        if book_t in book_dictionary:
            print("Your book is below in {}, with name = book title and copies = book amount")
            print(book_dictionary[book_t])
    except:
        print("Book Title Does Not Exist!")


def remove_book():
    book_title = input("Enter book title: ")
    if book_title not in book_dictionary or book_dictionary[book_title] == {"name": 0, "copies": 0}:
        print("Can not return as there are no copies of the book in stock")
        return
    else:
        del book_dictionary[book_title]


def load_data():
    try:
        with open("books.txt") as file:
            for line in file:
                b_t, b_c = line.split()
                book_dictionary[b_t] = {"name": b_t, "copies": b_c}

    except FileExistsError:
        print("File does not exist!")
        print(book_dictionary)


def main2():
    load_data()
    while True:
        option = input("Would you like to (a)dd a book, (f)ind a book, (r)emove book, (v)iew all books, or (q)uit? ")
        if option.lower() == 'a':
            add_book()
        elif option.lower() == 'v':
            view_book()
        elif option.lower() == 'f':
            find_book()
        elif option.lower() == 'r':
            remove_book()
        elif option.lower() == 'q':
            with open("books.txt", "w") as file:
                for book_title, book_info in book_dictionary.items():
                    file.writelines(f'{book_info["name"]} {book_info["copies"]}\n')
            break


main2()
