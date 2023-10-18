def get_score():
    while True:
        u_score = input("Enter the Score: ")
        # int only between 0-9, not 10, no neg, no letters.
        # then convert to int for calc
        if u_score not in '0123456789' or int(u_score) > 9:
            print("Enter Again! Invalid Input: ")
        else:
            return int(u_score)
            break


def perform_calculations(int_list):
    # sum/n_sum, int only
    average_score = sum(int_list) // len(int_list)
    # takes only highest
    high_score = max(int_list)
    # takes only lowest
    low_score = min(int_list)
    return average_score, high_score, low_score


def main():
    # main fun
    print(f'Basketball Scoring Calculator!')
    player_game = int(input(f'How Many Games the Player Played: '))
    int_list = []
    for index in range(player_game):
        # import score num, put in list
        score_num = get_score()
        int_list.append(score_num)
    # unpack/tuple/return, print
    print(f'Results Below!')
    avg, hgh, low = perform_calculations(int_list)
    print(f'The Average is: {avg}')
    print(f'The High Value is: {hgh}')
    print(f'The Low Value is: {low}')


main()
