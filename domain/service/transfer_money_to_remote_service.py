from domain.model.base.role import Role
from domain.model.local_account import local_account_repo
from domain.model.local_account.local_money_src import LocalMoneySrc
from domain.model.remote_account.remote_money_dest import RemoteMoneyDest
from domain.model.remote_account.remote_account import RemoteAccount


class TransferMoneyToRemoteService(object):

    def __init__(self):
        self.repo = local_account_repo.get()

    def execute(self, from_id, to_id, amount):
        from_account = self.repo.get(from_id)
        Role.inject(from_account, LocalMoneySrc)
        to_account = RemoteAccount(to_id)
        Role.inject(to_account, RemoteMoneyDest)
        Role.cast(from_account, LocalMoneySrc).transfer_money_to(Role.cast(to_account, RemoteMoneyDest), amount)
