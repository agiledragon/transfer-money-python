from domain.model.account.account import Account
from domain.model.base.role import Role
from domain.model.account.money_collector import MoneyCollector
from domain.model.account import account_repo


class AccountService(object):

    def __init__(self):
        self.repo = account_repo.get()

    def create_account(self, account_id, phone_number, amount):
        account = Account(account_id, phone_number, amount)
        Role.inject(account, MoneyCollector)
        self.repo.add(account_id, account)

    def destroy_account(self, account_id):
        self.repo.remove(account_id)
