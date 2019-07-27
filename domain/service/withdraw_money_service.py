from domain.model.base.role import Role
from domain.model.local_account.money_collector import MoneyCollector
from domain.model.local_account import local_account_repo


class WithdrawMoneyService(object):

    def __init__(self):
        self.repo = local_account_repo.get()

    def execute(self, account_id, amount):
        account = self.repo.get(account_id)
        Role.inject(account, MoneyCollector)
        Role.cast(account, MoneyCollector).withdraw(amount)


