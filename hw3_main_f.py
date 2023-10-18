# Function writes the score list to file
def writeToFile(scoreList):
    with open("scores.txt", 'w') as f:
        for row in scoreList:
            f.write(str(row[0]))
            f.write(" ")
            f.write(str(row[1]))
            f.write(" ")
            scores = row[2]
            for s in scores:
                f.write(str(s) + " ")
            f.write('\n')


def score_exists_for_date(month, date, scoreList):
    for row in scoreList:
        if month == row[0] and date == row[1]:
            return True
    return False


def add_score(scoreList):
    month = input('Enter month: ')
    date = int(input('Enter date: '))
    scores = []
    while date < 1 or date > 31:
        if date < 1 or date > 31:
            print('Invalid date, try again!')
            date = int(input('Enter date: '))
        else:
            break
    while True:
        score = int(input('Enter score: '))
        while score < 0 or score > 300:
            if score < 0 or score > 300:
                print('Invalid score, try again!')
                score = int(input('Enter score: '))

            else:
                break
        scores.append(score)
        choice = input('Add another score? Y/N: ')
        if choice != 'Y' and choice != 'y':
            break
    scoreExists = score_exists_for_date(month, str(date), scoreList)
    if not scoreExists:
        scoreList.append([month, date, scores])

    else:
        print('scores already exist with a month and date!')
    return scoreList


def view_scores(scoreList):
    for row in scoreList:
        month = row[0]
        date = row[1]
        scores = row[2]
        print(f'On {month} {date}, you scored: ', end="")
        for s in scores:
            print(f'{s}', end=",")
        print()


def average_scores(scoreList):
    scoreSum = 0
    count = 0
    for row in scoreList:
        scores = row[2]
        for s in scores:
            scoreSum += int(s)
            count += 1
    return scoreSum / count


def num_300s(scoreList):
    count = 0
    for row in scoreList:
        scores = row[2]
        for s in scores:
            if int(s) == 300:
                count += 1
    return count


# main code
def main():
    choice = 0
    scoreList = []
    while choice != 1:
        choice = int(input(
            '\n1. Quit the program\n2. View all scores\n3. Add a score\n'
            '4. Average scores\n5. Number of 300s\nEnter your choice: '))
        if choice == 1:
            print('Scores Saved and Program Exited!')
        elif choice == 2:
            scoreList = []
            try:
                with open("scores.txt") as file:
                    for row in file:
                        data = row.split(' ')
                        month = data[0]
                        date = data[1]
                        scores = []
                        for i in range(2, len(data) - 1):
                            scores.append(int(data[i]))
                        scoreList.append([month, date, scores])
                    view_scores(scoreList)
            except IOError:
                print('File doesnt exist, so enter scores with option 3')
        elif choice == 3:
            scoreList = add_score(scoreList)
            writeToFile(scoreList)
        elif choice == 4:
            avg = average_scores(scoreList)
            print('The average of scores is:', avg)
        elif choice == 5:
            N = num_300s(scoreList)
            print('The number of occurrences of "300s" is: ', N)


main()
