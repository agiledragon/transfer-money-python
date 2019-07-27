from abc import abstractmethod
from domain.model.base.role import Role


class MoneyDest(Role):

    @abstractmethod
    def transfer_money_from(self, from_id, amount):
        raise NotImplementedError

    @abstractmethod
    def get_account_id(self):
        raise NotImplementedError
