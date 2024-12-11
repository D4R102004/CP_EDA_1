from Clases_Practicas_EDA_I.Cp_4AVL.aVl import AVL
from Clases_Practicas_EDA_I.Cp_4AVL.physical_tree import AVLTree

class CP4:
    @staticmethod
    def get_minimum_nodes_needed_avl(h: int):
        if h <= 0:
            return 0
        return CP4.get_minimum_nodes_needed_avl(h - 1) + CP4.get_minimum_nodes_needed_avl(h - 2) + 1

    @staticmethod
    def get_height(n: int):
        h = 0
        needed = CP4.get_minimum_nodes_needed_avl(h)
        while needed < n:
            h += 1
            needed = CP4.get_minimum_nodes_needed_avl(h)
        return h - 1

    @staticmethod
    def is_avl(tree: 'AVLTree'):
        for i in tree.root.pre_order():
            left_height = i.left.height if i.left else -1
            right_height = i.right.height if i.right else -1
            factor = right_height - left_height
            if not -1 <= factor <= 1:
                return False
        return True




