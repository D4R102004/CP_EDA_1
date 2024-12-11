from Clases_Practicas_EDA_I.Cp_4AVL.aVl import AVL
from Clases_Practicas_EDA_I.Cp_4AVL.physical_tree import AVLTree
from Clases_Practicas_EDA_I.Cp_4AVL.aBB import BinarySearchTree as ABB


class Set:
    def __init__(self, node: AVL):
        self._myavl = AVLTree(node)

    @property
    def myavl(self):
        return self._myavl

    def find(self, key):
        return self.myavl.find(key)

    def insert(self, node: 'AVL'):
        self.myavl.insert(node)

    def remove(self, node: 'AVL'):
        self.myavl.remove(node)

    def rank(self, key):
        return self.myavl.rank(key)

    def select(self, k):
        root = self.myavl.root

        def _select(node: 'ABB', k):
            if node is None or k > node.size or k < 0:
                return None
            if k == 0:
                return node.lowest()
            left_size = node.left.size if node.left else 0
            if k == left_size:
                return node.value
            if k < left_size:
                return _select(node.left, k)
            else:
                return _select(node.right, k - left_size - 1)
        return _select(root, k)









