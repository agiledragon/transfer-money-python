from domain.model.comm_role.money_src import MoneySrc
from domain.model.comm_role.account_info import AccountInfo
from domain.model.remote_account.remote_account_provider import *


class RemoteMoneySrc(MoneySrc):

    def __init__(self):
        self.account_info = AccountInfo()

    def transfer_money_to(self, dest, amount):
        dest.transfer_money_from(self.account_info.id, amount)
        ok = Response()
        ok.is_failed = False
        send_protocol_resp(ok)



