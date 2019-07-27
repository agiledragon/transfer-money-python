from domain.model.base.entity import Entity


class AccountInfo(Entity):
    def __init__(self, account_id=0):
        Entity.__init__(self, account_id)
