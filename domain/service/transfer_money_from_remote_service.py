from domain.model.base.role import Role
from domain.model.local_account import local_account_repo
from domain.model.local_account.local_money_dest import LocalMoneyDest
from domain.model.remote_account.remote_money_src import RemoteMoneySrc
from domain.model.remote_account.remote_account import RemoteAccount


class TransferMoneyFromRemoteService(object):

    def __init__(self):
        self.repo = local_account_repo.get()

    def execute(self, from_id, to_id, amount):
        from_account = RemoteAccount(from_id)
        Role.inject(from_account, RemoteMoneySrc)
        to_account = self.repo.get(to_id)
        Role.inject(to_account, LocalMoneyDest)
        Role.cast(from_account, RemoteMoneySrc).transfer_money_to(Role.cast(to_account, LocalMoneyDest), amount)
