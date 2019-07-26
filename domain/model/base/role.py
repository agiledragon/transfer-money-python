class Role(object):

    @staticmethod
    def cast(obj, Role):
        return getattr(obj, Role().__class__.__name__)

    @staticmethod
    def inject(obj, Role):
        role = Role()
        for key in role.__dict__.keys():
            role.__dict__[key] = obj.__dict__[key]
        obj.__dict__[role.__class__.__name__] = role


class Teacher(object):

    def __init__(self):
        self._name = ""

    def reading_book(self):
        print "%s reading book" % self._name


class Man(object):

    def __init__(self, name):
        self._x = 1
        self._name = name


if __name__ == '__main__':
    man = Man("zxl")
    Role.inject(man, Teacher)
    t = Role.cast(man, Teacher)
    t.reading_book()




