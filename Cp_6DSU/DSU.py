from abc import ABC, abstractmethod


class DSU(ABC):
    @abstractmethod
    def set_of(self, index: int):
        pass

    @abstractmethod
    def merge(self, a: int, b: int):
        pass

