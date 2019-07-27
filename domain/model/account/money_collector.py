from domain.model.base.role import Role
from domain.model.account.balance import Balance
from domain.model.account.phone import Phone


class MoneyCollector(Role):

    def __init__(self):
        self.balance = Balance()
        self.phone = Phone()

    def withdraw(self, amount):
        if self.balance.amount < amount:
            raise Exception("insufficient money!")
        self.balance.decrease(amount)
        self.phone.send_withdraw_msg(amount)
