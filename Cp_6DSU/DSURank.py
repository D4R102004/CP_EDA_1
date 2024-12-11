from typing import List
from Clases_Practicas_EDA_I.Utils.CPlus2 import CPlus2 as CPlus
from Clases_Practicas_EDA_I.Cp_6DSU.DSU import DSU


class DSURank(DSU):
    def __init__(self, n: int):
        self._ranks = [0] * (n + 1)
        self._parents = [i for i in range(n + 1)]

    @property
    def ranks(self):
        return self._ranks

    @property
    def parents(self):
        return self._parents

    def set_of(self, index: int):
        if index == self.parents[index]:
            return index
        self.parents[index] = self.set_of(self.parents[index])
        return self.parents[index]

    def merge(self, a: int, b: int):
        x = self.set_of(a)
        y = self.set_of(b)
        if x == y:
            return
        if self.ranks[x] < self.ranks[y]:
            x, y = y, x
        self.parents[y] = self.parents[x]
        if self.ranks[x] == self.ranks[y]:
            self.ranks[x] += 1


