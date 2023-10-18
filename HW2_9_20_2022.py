"""Enter a new customer sale into the system.
Ask how many books, subtotal cost of the books, before tax.
Ask whether the customer is a free member, paid member, or non-member.
Calculate 9.25% of the subtotal cost to be the amount for taxes and add that amount to the subtotal to calculate the final cost.
If the customer is a paid member, remove 10% of the subtotal cost from the final cost. (Note: The tax amount is not discounted)
Add the final cost to the grand_total variable.
Determine how many points the customer will receive for this purchase. If the customer is not a member, they receive 0 points. Otherwise, the number of points earned by the customer is based on the following list:
If 1 book is purchased, all members earn 5 points.
If 2 books are purchased, all members earn 15 points.
If 3 books are purchased:
Paid members earn 50 points
Free members earn 30 points
If 4 or more books are purchased
Paid members earn 100 points
Free members earn 60 points
"""

# grand variables
point = 0
grand_total = 0


def point_g(num_of_books, member_type):
    # calculate the points
    if num_of_books == 1:
        points = point + 5
    elif num_of_books == 2:
        points = point + 15
    elif num_of_books == 3:
        if member_type == 1:
            points = point + 30
        elif member_type == 2:
            points = point + 50
        elif member_type == 3:
            points = point + 0
    elif num_of_books >= 4:
        if member_type == 1:
            points = point + 60
        elif member_type == 2:
            points = point + 100
        elif member_type == 3:
            points = point + 0

    return points


def subtotal_cost_tax_final(subtotal_cost):
    tax = 0.0925 * subtotal_cost
    total_cost = subtotal_cost + tax
    print(f'The Tax: {tax:.2f}')
    print(f'The Final Cost: ${total_cost:,.2f}')


def t_member(member_type, subtotal_cost, points):
    if member_type == 2:
        tax = 0.0925 * subtotal_cost
        total_cost = (subtotal_cost * 1.0925) - (subtotal_cost * 0.1)
        g_total = grand_total + total_cost
        print(f'Amount saved: ${(subtotal_cost * 0.1):,.2f}')
        print(f'Total Points received: {points}')
        print(f'Grand Total: ${g_total:,.2f} ;This store has made ${g_total:,.2f} today!')
    else:
        tax = 0.0925 * subtotal_cost
        total_cost = (subtotal_cost * 1.0925)
        g_total = grand_total + total_cost
        print(f'Total Points received: {points}')
        print(f'Grand Total: ${g_total:,.2f} ;This store has made ${g_total:,.2f} today!')


def book_sub(num_books, sub_cost):
    print(f'Number of books: {num_books}')
    print(f'The Sub Total: ${sub_cost:,.2f}')


def main():
    end_loop = ''
    while end_loop.lower() != "n":
        print()
        num_books = int(input("Enter Amount of Books You Buy:  "))
        sub_cost = float(input("Enter Subtotal Cost:  "))
        mem_type = int(input("Enter Member Type:(1=Free, 2=Paid, 3=None/Non):  "))
        print(f'Your Receipt is Below:')
        book_sub(num_books, sub_cost)
        subtotal_cost_tax_final(sub_cost)
        point_g(int(num_books), mem_type)
        t_member(mem_type, sub_cost, point_g(num_books, mem_type))
        end_loop = input("Do you want to continue?(Y/N):  ")


main()
