"""Write a program that uses a loop to
ask the user to enter today’s sales for
five stores. The entered results should
be stored in a list. You may assume the
user will enter integers.

After the data has been entered,
the program should display a bar graph
comparing each store’s sales. Each bar
 should be a row of asterisks, and
 each asterisk representing $100 of
 sales (hint: there are several ways
 to do this. One way is to use nested
 loops. The outer loop iterates over
 the list you created, and the inner
 loop prints one asterisk per 100
 dollars of sales for that store.)

 A sample output:

Enter today’s sales for store 1: 1000
Enter today’s sales for store 2: 1200
Enter today’s sales for store 3: 1800
Enter today’s sales for store 4: 800
Enter today’s sales for store 5: 1900

SALES BAR CHART  (Each * = $100)

Store 1: **********
Store 2: ************
Store 3: ******************
Store 4: ********
Store 5: *******************"""


def main():
    s_list = []  # sale list
    # enter how many times
    for i in range(5):
        s_list.append(int(input(f"Enter today's sales for store {i + 1}: ")))
    print()
    # print graph and calc
    # end makes print side by side
    print(f'SALES BAR CHART  (Each * = $100)')
    for i in range(5):
        print(f"Store {i + 1}: ", end='')
        for j in range(s_list[i] // 100):
            print('*', end='')
        print()


main()
