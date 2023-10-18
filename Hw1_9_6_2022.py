"""
About the first house:
-The address
-The square footage
-The price
-The tax rate. If 10, the tax rate = 10%, etc.

About the second house.
For now, you may assume the user
will enter proper data: A string for the
address, an integer for the square footage,
and floats for the price and tax rate.

Perform some calculations and display:
-The address
-The price after the tax rate is applied.
-The price (after the tax rate is applied)
per square foot.

ALWAYS: Make sure the data that
prints is formatted
nicely with f-strings."""


def main():

    print("Info. on the 1st House:")
    address1 = input("Enter Address: ")
    address = str(address1)
    sqr_ft1 = input("Enter Square Footage: ")
    sqr_ft1 = int(sqr_ft1)
    price1 = input("Enter Price: ")
    price1 = float(price1)
    tax_r1 = input("Enter Tax Rate %: ")
    tax_r1 = float(tax_r1)/100 + 1.00
    print()
    print("Info. on the 2nd House:")
    address2 = input("Enter Address: ")
    address2 = str(address2)
    sqr_ft2 = input("Enter Square Footage: ")
    sqr_ft2 = int(sqr_ft2)
    price2 = input("Enter Price: ")
    price2 = float(price2)
    tax_r2 = input("Enter Tax Rate %: ")
    tax_r2 = float(tax_r2)/100 + 1.00

    # calc
    pt1 = price1 * tax_r1
    pt2 = price2 * tax_r2
    pt_s1 = (pt1 / sqr_ft1)
    pt_s2 = (pt2 / sqr_ft2)
    # format
    pt1_left = f'{pt1:,.2f}'
    pt2_left = f'{pt2:,.2f}'
    pt1_s1_left = f'{pt_s1:,.2f}'
    pt2_s2_left = f'{pt_s2:,.2f}'

    print()
    print("Calculations: ")
    print(f'House Number:          {"1st": <30}    {"2nd": <30}')
    print(f'Address:               {address1: <30}    {address2: <30}')
    print(f'Price w/Tax:           ${pt1_left: <30}   ${pt2_left: <30}')
    print(f'Price per SqrFt:       ${pt1_s1_left: <30}   ${pt2_s2_left: <30}')


main()
