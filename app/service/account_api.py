from domain.service.account_service import AccountService
from domain.service.withdraw_money_service import WithdrawMoneyService


class AccountApi(object):

    def __init__(self):
        self.account_service = AccountService()
        self.withdraw_money_service = WithdrawMoneyService()

    def create_account(self, phone_number, init_amount):
        id = self._generate_account_id(phone_number)
        self.account_service.create_account(id, phone_number, init_amount)
        return id

    def destroy_account(self, account_id):
        self.account_service.destroy_account(account_id)

    def withdraw_money(self, account_id, amount):
        self.withdraw_money_service.execute(account_id, amount)

    def get_amount(self, account_id):
        return self.withdraw_money_service.get_amount(account_id)

    @staticmethod
    def _generate_account_id(phone_number):
        return phone_number[2:] + "888"

