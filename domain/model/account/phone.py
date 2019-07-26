from domain.model.base.value_object import ValueObject
from domain.model.account.account_info import AccountInfo


class Phone(ValueObject):

    def __init__(self, phone_number="", account_info=AccountInfo(0)):
        self.phone_number = phone_number
        self.account_info = account_info

    def send_withdraw_msg(self, amount):
        print "phone %s: %d yuan has been withdrawed from accountId(%s)!\n" \
              %(self.phone_number, amount, self.account_info.id)
