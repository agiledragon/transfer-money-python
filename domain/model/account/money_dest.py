from domain.model.base.role import Role
from domain.model.account.account_info import AccountInfo
from domain.model.account.balance import Balance
from domain.model.account.phone import Phone


class MoneyDest(Role):

    def __init__(self):
        self.account_info = AccountInfo()
        self.balance = Balance()
        self.phone = Phone()

    def transfer_money_from(self, from_id, amount):
        self.balance.increase(amount)
        self.phone.send_transfer_from_msg(from_id, amount)

    def get_account_id(self):
        return self.account_info.id

