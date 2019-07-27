import unittest

from domain.model.base.repo import Repo
from app.service.account_api import AccountApi
from domain.model.local_account import local_account_repo


class FakeAccountRepo(Repo):

    def __init__(self):
        self._repo = {}

    def add(self, id, obj):
        if self._repo.has_key(id):
            return False
        self._repo[id] = obj
        return True

    def remove(self, id):
        if self._repo.has_key(id):
            del self._repo[id]

    def update(self, id, obj):
        if self._repo.has_key(id):
            self._repo[id] = obj
            return True
        return False

    def get(self, id):
        return self._repo[id]


repo = FakeAccountRepo()
local_account_repo.set(repo)


class AccountTest(unittest.TestCase):

    def setUp(self):
        self.api = AccountApi()
        self.jim_phone_number = "19999999999"
        self.jim_init_amount = 10000
        self.jim_account_id = self.api.create_account(self.jim_phone_number, self.jim_init_amount)
        lucy_phone_number = "18888888888"
        self.lucy_init_amount = 5000
        self.lucy_account_id = self.api.create_account(lucy_phone_number, self.lucy_init_amount)

    def tearDown(self):
        self.api.destroy_account(self.jim_account_id)

    def test_withdraw_money(self):
        amount = 1500
        self.api.withdraw_money(self.jim_account_id, amount)
        self.assertEqual(self.jim_init_amount - amount, self.api.get_amount(self.jim_account_id))

    def test_transfer_money_to_local_service(self):
        amount = 1500
        self.api.transfer_money_to_local(self.jim_account_id, self.lucy_account_id, amount)
        self.assertEqual(self.jim_init_amount - amount, self.api.get_amount(self.jim_account_id))
        self.assertEqual(self.lucy_init_amount + amount, self.api.get_amount(self.lucy_account_id))

    def test_transfer_money_to_remote_service(self):
        amount = 1500
        self.api.transfer_money_to_remote(self.jim_account_id, self.lucy_account_id, amount)
        self.assertEqual(self.jim_init_amount - amount, self.api.get_amount(self.jim_account_id))

    def test_transfer_money_from_remote_service(self):
        amount = 1500
        self.api.transfer_money_from_remote(self.lucy_account_id, self.jim_account_id, amount)
        self.assertEqual(self.jim_init_amount + amount, self.api.get_amount(self.jim_account_id))


if __name__ == '__main__':
    unittest.main()

