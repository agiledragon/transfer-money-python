from domain.service.account_service import AccountService
from domain.service.withdraw_money_service import WithdrawMoneyService
from domain.service.transfer_money_to_local_service import TransferMoneyToLocalService
from domain.service.transfer_money_service import TransferMoneyService
from domain.service.transfer_money_to_remote_service import TransferMoneyToRemoteService
from domain.service.transfer_money_from_remote_service import TransferMoneyFromRemoteService


class AccountApi(object):

    def __init__(self):
        self.account_service = AccountService()
        self.withdraw_money_service = WithdrawMoneyService()
        self.transfer_money_to_local_service = TransferMoneyToLocalService()
        self.transfer_money_service = TransferMoneyService()
        self.transfer_money_to_remote_service = TransferMoneyToRemoteService()
        self.transfer_money_from_remote_service = TransferMoneyFromRemoteService()

    def create_account(self, phone_number, init_amount):
        id = self._generate_account_id(phone_number)
        self.account_service.create_account(id, phone_number, init_amount)
        return id

    def destroy_account(self, account_id):
        self.account_service.destroy_account(account_id)

    def withdraw_money(self, account_id, amount):
        self.withdraw_money_service.execute(account_id, amount)

    def get_amount(self, account_id):
        return self.transfer_money_service.get_amount(account_id)

    def transfer_money_to_local(self, from_id, to_id, amount):
        return self.transfer_money_to_local_service.execute(from_id, to_id, amount)

    def transfer_money_to_remote(self, from_id, to_id, amount):
        return self.transfer_money_to_remote_service.execute(from_id, to_id, amount)

    def transfer_money_from_remote(self, from_id, to_id, amount):
        return self.transfer_money_from_remote_service.execute(from_id, to_id, amount)

    @staticmethod
    def _generate_account_id(phone_number):
        return phone_number[2:] + "888"

