from domain.model.base.role import Role
from domain.model.account import account_repo
from domain.model.account.money_src import MoneySrc
from domain.model.account.money_dest import MoneyDest


class TransferMoneyToLocalService(object):

    def __init__(self):
        self.repo = account_repo.get()

    def execute(self, from_id, to_id, amount):
        from_account = self.repo.get(from_id)
        Role.inject(from_account, MoneySrc)
        to_account = self.repo.get(to_id)
        Role.inject(to_account, MoneyDest)
        Role.cast(from_account, MoneySrc).transfer_money_to(Role.cast(to_account, MoneyDest), amount)
