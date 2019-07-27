from domain.model.comm_role.money_dest import MoneyDest
from domain.model.comm_role.account_info import AccountInfo
from domain.model.local_account.balance import Balance
from domain.model.local_account.phone import Phone


class LocalMoneyDest(MoneyDest):

    def __init__(self):
        self.account_info = AccountInfo()
        self.balance = Balance()
        self.phone = Phone()

    def transfer_money_from(self, from_id, amount):
        self.balance.increase(amount)
        self.phone.send_transfer_from_msg(from_id, amount)

    def get_account_id(self):
        return self.account_info.id

