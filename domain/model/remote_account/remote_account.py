from domain.model.base.aggregate_root import AggregateRoot
from domain.model.comm_role.account_info import AccountInfo


class RemoteAccount(AggregateRoot):
    def __init__(self, account_id):
        AggregateRoot.__init__(self, account_id)
        self.account_info = AccountInfo(account_id)