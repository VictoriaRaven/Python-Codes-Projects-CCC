def get_score():
    while True:
        u_score = input("Enter the Score: ")
        # int only between 0-9, not 10, no neg.
        if u_score not in '0123456789':
            print("Enter Again! Invalid Input: ")
        else:
            return int(u_score)
            break


def perform_calculations(int_list):
    # sum/n_sum, int only
    average_score = sum(int_list) // len(int_list)
    # takes high number
    high_score = max(int_list)
    # takes low number
    low_score = min(int_list)
    return average_score, high_score, low_score


def main():
    # main function
    print(f'Basketball player Scoring over a period of games!')
    player_game = int(input(f'How Many Games the Player Played: '))
    int_list = []
    for index in range(player_game):
        score_num = get_score()
        int_list.append(score_num)
    # print out the results
    print(f'Results Below!')
    avg, hgh, low = perform_calculations(int_list)
    print(f'The Average is: {avg}')
    print(f'The High Value is: {hgh}')
    print(f'The Low Value is: {low}')


main()
