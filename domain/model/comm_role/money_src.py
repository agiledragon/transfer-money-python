from abc import abstractmethod
from domain.model.base.role import Role


class MoneySrc(Role):

    @abstractmethod
    def transfer_money_to(self, dest, amount):
        raise NotImplementedError
