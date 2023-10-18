
class Account:
    # constructor

    def __init__(self, balance):
        self._balance = balance
        self.transaction = []

    def transaction(self):
        return self.transaction

    @property
    def balance(self):
        return self._balance

    @balance.setter  # double check if it is ok to use raise in obs video
    def balance(self, balance):
        if balance < 0:
            raise ValueError("Invalid balance: " + str(balance) + " must be greater than 0!")

    def withdraw(self, amount):
        if amount == self._balance < 0:
            # do not perform the withdrawal
            # print error and return false
            print(f'Invalid balance: {amount} You must have a balance greater than 0.')
            return False
        else:
            self._balance -= amount
            self.transaction.append(self._balance)  # add to Transaction
            return True

    def deposit(self, amount):
        self._balance += amount
        self.transaction.append(self._balance)  # add to Transaction
        return True

    def __str__(self):
        return_string = f''
        total_trans = 0
        for transaction in self.transaction:
            return_string += f'${transaction:.2f}\n'
            total_trans += transaction

        return_string += "Balance:\n"
        return_string += f'${total_trans:.2f}'

        return return_string
