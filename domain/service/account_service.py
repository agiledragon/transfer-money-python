from domain.model.local_account.local_account import LocalAccount
from domain.model.local_account import local_account_repo


class AccountService(object):

    def __init__(self):
        self.repo = local_account_repo.get()

    def create_account(self, account_id, phone_number, amount):
        account = LocalAccount(account_id, phone_number, amount)
        self.repo.add(account_id, account)

    def destroy_account(self, account_id):
        self.repo.remove(account_id)
