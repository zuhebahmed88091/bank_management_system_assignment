# Abstract Method
from abc import ABC, abstractmethod


class Customer(ABC):

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def set_name(self, name):
        pass

    @abstractmethod
    def get_nid(self):
        pass

    @abstractmethod
    def set_nid(self, nid):
        pass

    @abstractmethod
    def get_address(self):
        pass

    @abstractmethod
    def set_address(self, address):
        pass

    @abstractmethod
    def get_age(self):
        pass

    @abstractmethod
    def set_age(self, age):
        pass
