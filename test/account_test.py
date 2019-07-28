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

JIM_PHONE_NUMBER = "19999999999"
JIM_INIT_AMOUNT = 10000
LUCY_PHONE_NUMBER = "18888888888"
LUCY_INIT_AMOUNT = 5000
AMOUNT = 1500


class AccountTest(unittest.TestCase):

    def setUp(self):
        self.api = AccountApi()
        self.jim_account_id = self.api.create_account(JIM_PHONE_NUMBER, JIM_INIT_AMOUNT)
        self.lucy_account_id = self.api.create_account(LUCY_PHONE_NUMBER, LUCY_INIT_AMOUNT)

    def tearDown(self):
        self.api.destroy_account(self.jim_account_id)

    def test_withdraw_money(self):
        self.api.withdraw_money(self.jim_account_id, AMOUNT)
        self.assertEqual(JIM_INIT_AMOUNT - AMOUNT, self.api.get_amount(self.jim_account_id))

    def test_transfer_money_to_local_service(self):
        self.api.transfer_money_to_local(self.jim_account_id, self.lucy_account_id, AMOUNT)
        self.assertEqual(JIM_INIT_AMOUNT - AMOUNT, self.api.get_amount(self.jim_account_id))
        self.assertEqual(LUCY_INIT_AMOUNT + AMOUNT, self.api.get_amount(self.lucy_account_id))

    def test_transfer_money_to_remote_service(self):
        self.api.transfer_money_to_remote(self.jim_account_id, self.lucy_account_id, AMOUNT)
        self.assertEqual(JIM_INIT_AMOUNT - AMOUNT, self.api.get_amount(self.jim_account_id))

    def test_transfer_money_from_remote_service(self):
        self.api.transfer_money_from_remote(self.lucy_account_id, self.jim_account_id, AMOUNT)
        self.assertEqual(JIM_INIT_AMOUNT + AMOUNT, self.api.get_amount(self.jim_account_id))


if __name__ == '__main__':
    unittest.main()

