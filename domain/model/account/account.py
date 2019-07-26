from domain.model.base.aggregate_root import AggregateRoot
from domain.model.account.account_info import AccountInfo
from domain.model.account.phone import Phone
from domain.model.account.balance import Balance


class Account(AggregateRoot):
    def __init__(self, account_id, phone_number, amount):
        AggregateRoot.__init__(self, account_id)
        self.account_info = AccountInfo(account_id)
        self.phone = Phone(phone_number, self.account_info)
        self.balance = Balance(amount)