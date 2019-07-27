from domain.model.base.value_object import ValueObject
from domain.model.account.account_info import AccountInfo


class Phone(ValueObject):

    def __init__(self, phone_number="", account_info=AccountInfo()):
        self.phone_number = phone_number
        self.account_info = account_info

    def send_withdraw_msg(self, amount):
        print "phone %s: %d yuan has been withdrawed from accountId(%s)!\n" \
              %(self.phone_number, amount, self.account_info.id)

    def send_transfer_to_msg(self, to_id, amount):
        print "phone %s: account_id(%s) send %d yuan to account_id(%s)!\n" \
              %(self.phone_number, self.account_info.id, amount, to_id)

    def send_transfer_from_msg(self, from_id, amount):
        print "phone %s: account_id(%s) receive %d yuan from account_id(%s)!\n" \
              %(self.phone_number, self.account_info.id, amount, from_id)
