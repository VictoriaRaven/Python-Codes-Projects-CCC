def create_scores_file():
    try:
        with open("scores.txt") as file:
            for line in file.readlines():
                month, day, *score = line.split()
        print("Previous added scores is imported!")
    except:
        # creating a file to store values of employees
        f_list = ["January 15 200 300 126 200 250", "April 20 125 100", "May 17 300 100 215"]
        with open("scores.txt", "w") as file:
            for item in f_list:
                # write item on new line
                file.write(f'{item}\n')
        print("File does not exist so, File created!")


def view_scores():
    with open("scores.txt") as file:
        for line in file.readlines():
            month, day, *score = line.split()
            print(f'On {month} {day}, you scored: ', end="")
            for i in score:
                print(f'{i}', end=",")
            print()
        return month, day, score
    # needs to include 20,30, and 126, etc.. it has [] so far../


def score_exists_for_date(m2, d2):
    with open("scores.txt", "r") as file:
        for line in file:
            month, day, *scores = line.split()
            if m2 in month and d2 in day:
                return True


def add_score():
    with open("scores.txt", "a") as file:
        mon = input(f'Enter month: ')
        date = input(f'Enter date: ')
        # add if
        if score_exists_for_date(mon, date):
            print(f'That date already exists! It has an entry on it.')
            return
        if date.isdigit():  # check
            if 32 > int(date) > 0:
                file.writelines(mon + " ")
                file.writelines(str(date) + " ")
                # add scores
                while True:
                    scores = input("Enter Score, 'q' to quit: ")
                    if scores == 'q':
                        file.writelines("\n")
                        break
                    elif int(scores) > 300 or int(scores) < 0:
                        print("Invalid score!")
                    else:
                        file.writelines(str(scores) + " ")
            else:
                print("Please enter an integer that corresponds to an existing day within the specified month.")
            return


def average_scores():
    total_scores_in_list = 0
    divisor_number = 0
    with open("scores.txt") as file:
        for line in file.readlines():
            month, day, *scores = line.split()
            for score_num in scores:
                total_scores_in_list = total_scores_in_list + int(score_num)
                divisor_number += 1
    average = total_scores_in_list / divisor_number
    print(f'The average is: {average:.2f}')


def num_300s():
    with open("scores.txt") as file:
        data = file.read()
        occurrences = data.count("300")
    print(f'Number of Occurrences with "300" : {occurrences}')


def main():
    create_scores_file()
    while True:
        print()
        print(f'1: Quits Program')
        print(f'2: View All Scores')
        print(f'3: Add a Score')
        print(f'4: Average Scores')
        print(f'5: Number of 300s')
        u_options = input("Enter option #: ")
        if u_options == "1":
            break
        elif u_options == "2":
            view_scores()
        elif u_options == "3":
            add_score()
        elif u_options == "4":
            average_scores()
        elif u_options == "5":
            num_300s()
        else:
            print(f"Please enter #'s 1-5!")


main()
