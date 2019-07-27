from domain.model.base.value_object import ValueObject


class Balance(ValueObject):

    def __init__(self, initial_amount=0):
        self.amount = initial_amount

    def increase(self, amount):
        self.amount += amount

    def decrease(self, amount):
        self.amount -= amount

    def get_amount(self):
        return self.amount

