from domain.model.base.role import Role
from domain.model.local_account import local_account_repo
from domain.model.local_account.local_money_src import LocalMoneySrc


class TransferMoneyService(object):

    def __init__(self):
        self.repo = local_account_repo.get()

    def get_amount(self, account_id):
        account = self.repo.get(account_id)
        Role.inject(account, LocalMoneySrc)
        return Role.cast(account, LocalMoneySrc).get_amount()
