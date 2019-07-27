from domain.model.base.aggregate_root import AggregateRoot
from domain.model.comm_role.account_info import AccountInfo
from domain.model.local_account.phone import Phone
from domain.model.local_account.balance import Balance


class LocalAccount(AggregateRoot):
    def __init__(self, account_id, phone_number, amount):
        AggregateRoot.__init__(self, account_id)
        self.account_info = AccountInfo(account_id)
        self.phone = Phone(phone_number, self.account_info)
        self.balance = Balance(amount)