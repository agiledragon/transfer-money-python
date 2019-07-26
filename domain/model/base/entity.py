
class Entity(object):

    def __init__(self, id):
        self._id = id

    def __eq__(self, other):
        return self.id == other.id

    def __ne__(self, other):
        return not self == other

    @property
    def id(self):
        return self.id

