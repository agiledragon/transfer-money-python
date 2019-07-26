from abc import abstractmethod


class Repo(object):

    @abstractmethod
    def add(self, id, obj):
        raise NotImplementedError

    @abstractmethod
    def remove(self, id):
        raise NotImplementedError

    @abstractmethod
    def update(self, id, obj):
        raise NotImplementedError

    @abstractmethod
    def get(self, id):
        raise NotImplementedError

