from typing import List
from Clases_Practicas_EDA_I.Utils.CPlus2 import CPlus2 as CPlus
from Clases_Practicas_EDA_I.Cp_6DSU.DSU import DSU


class DSUSize(DSU):
    def __init__(self, n: int):
        self._sizes = [0] * (n + 1)
        self._parents = [i for i in range(n + 1)]

    @property
    def sizes(self):
        return self._sizes

    @property
    def parents(self):
        return self._parents

    def set_of(self, index: int):
        if index == self.parents[index]:
            return index
        self.parents[index] = self.set_of(self.parents[index])
        return self.parents[index]

    def merge(self, a: int, b: int):
        root_a = self.set_of(a)
        root_b = self.set_of(b)
        if root_a == root_b:
            return
        if self.sizes[root_a] < self.sizes[root_b]:
            root_a, root_b = root_b, root_a
        self.parents[root_b] = self.parents[root_a]
        self.sizes[root_a] += self.sizes[root_b]
