from Account import Account


class Transaction:
    _amount = None

    # constructor
    def __init__(self, amount):
        self._amount = amount
        # bool changes what is in str
        self.is_withdrawal = None  # Account.deposit or Account.withdraw

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        if isinstance(amount, Account):
            self._amount = amount

    def __str__(self):
        if Account.deposit == True:
            self.is_withdrawal = False
        if Account.withdraw == True:
            self.is_withdrawal = True

        if self.is_withdrawal:
            return f'Withdrawal: -{self.amount}\n'
        else:  # if false print
            return f'Deposit: +{self.amount}\n'

