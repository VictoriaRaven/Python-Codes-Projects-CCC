from Transaction import Transaction
from Account import Account


def main():
    starting_balance = 0
    # create obj with hard coded input ex: Date(1,34,555)

    ObjA1 = Account(0)
    ObjA2 = Account(0)
    ObjA3 = Account(0)
    ObjA4 = Account(0)

    ObjA1.deposit(200)
    ObjA1.withdraw(10)
    ObjA1.deposit(1)
    print(Transaction(ObjA1))

    ObjA2.withdraw(10)
    ObjA2.deposit(1)
    print(Transaction(ObjA2))

    ObjA3.deposit(100)
    print(Transaction(ObjA3))

    ObjA4.withdraw(20)
    print(Transaction(ObjA4))


main()
