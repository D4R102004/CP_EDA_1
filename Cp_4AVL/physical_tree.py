from Clases_Practicas_EDA_I.Cp_4AVL.aBB import BinarySearchTree as ABB
from Clases_Practicas_EDA_I.Cp_4AVL.aVl import AVL


class AVLTree:
    def __init__(self, node: 'ABB'):
        self._root = node

    @property
    def root(self):
        return self._root

    def restore_root(self):
        while self.root.parent:
            self._root = self.root.parent

    def find(self, key):
        return self.root.search(key)

    def insert(self, node: 'ABB'):
        self.root.insert(node)
        self.restore_root()

    def remove(self, node: 'ABB'):
        self.root.remove(node)
        self.restore_root()

    def in_order(self):
        return self.root.in_order()

    def pre_order(self):
        return self._root.pre_order()

    def rank(self, key):
        return self.root.rank(key)

