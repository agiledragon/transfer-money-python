from domain.model.base.role import Role
from domain.model.account.account_info import AccountInfo
from domain.model.account.balance import Balance
from domain.model.account.phone import Phone
from domain.model.account.money_dest import MoneyDest


class MoneySrc(Role):

    def __init__(self):
        self.account_info = AccountInfo()
        self.balance = Balance()
        self.phone = Phone()

    def transfer_money_to(self, dest, amount):
        if self.balance.amount < amount:
            raise Exception("insufficient money!")
        dest.transfer_money_from(self.account_info.id, amount)
        self.balance.decrease(amount)
        self.phone.send_transfer_to_msg(dest.get_account_id(), amount)

    def get_amount(self):
        return self.balance.amount
