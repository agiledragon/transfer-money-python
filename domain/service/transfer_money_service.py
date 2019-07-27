from domain.model.base.role import Role
from domain.model.account import account_repo
from domain.model.account.money_src import MoneySrc


class TransferMoneyService(object):

    def __init__(self):
        self.repo = account_repo.get()

    def get_amount(self, account_id):
        account = self.repo.get(account_id)
        Role.inject(account, MoneySrc)
        return Role.cast(account, MoneySrc).get_amount()
