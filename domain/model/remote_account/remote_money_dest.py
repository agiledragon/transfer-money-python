from domain.model.comm_role.money_dest import MoneyDest
from domain.model.comm_role.account_info import AccountInfo
from domain.model.remote_account.remote_account_provider import *


class RemoteMoneyDest(MoneyDest):

    def __init__(self):
        self.account_info = AccountInfo()

    def transfer_money_from(self, from_id, amount):
        send_transfer_to_protocol_msg(from_id, self.account_info.id, amount)
        ok = wait_protocol_resp()
        if ok.is_failed:
            raise Exception("transfer money to remote fail!")

    def get_account_id(self):
        return self.account_info.id

