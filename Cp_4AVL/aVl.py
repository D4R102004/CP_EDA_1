from Clases_Practicas_EDA_I.Cp_4AVL.aBB import BinarySearchTree as ABB


class AVL(ABB):
    @property
    def balance_factor(self):
        left_height = self.left.height if self.left else 0
        right_height = self.right.height if self.right else 0
        return right_height - left_height

    def check_balance(self):
        return -1 <= self.balance_factor <= 1

    def rotate_insert(self, parent: 'AVL'):
        if parent.balance_factor == 2:
            if self.balance_factor == 1:
                self.rotate_simple_left(parent)
            elif self.balance_factor == -1:
                self.rotate_double(self.left, parent)
        elif parent.balance_factor == -2:
            if self.balance_factor == -1:
                self.rotate_simple_right(parent)
            elif self.balance_factor == 1:
                self.rotate_double(self.right, parent)

    def rotate(self, parent: 'AVL'):
        if self.balance_factor == 0:
            if parent.balance_factor == 2:
                self.rotate_simple_left(parent)
            elif parent.balance_factor == -2:
                self.rotate_simple_right(parent)
            return True
        else:
            self.rotate_insert(parent)
            return False

    def rotate_simple_left(self, parent):
        print(f"Rotando simple izquierda: nodo {self.value}, padre {parent.value}")
        left_son = self.left
        self.parent = self.parent.parent
        if self.parent:
            if parent is self.parent.right:
                self.parent.right = self
            else:
                self.parent.left = self
        self.left = parent
        self.left.parent = self
        self.left.right = left_son
        if self.left.right:
            self.left.right.parent = self.left

    def rotate_simple_right(self, parent):
        print(f"Rotando simple derecha: nodo {self.value}, padre {parent.value}")
        right_son = self.right
        self.parent = self.parent.parent
        if self.parent:
            if parent is self.parent.right:
                self.parent.right = self
            else:
                self.parent.left = self
        self.right = parent
        self.right.parent = self
        self.right.left = right_son
        if self.right.left:
            self.right.left.parent = self.right

    def rotate_double(self, to_rot: 'AVL', parent: 'AVL'):
        if self.balance_factor == -1:
            to_rot.rotate_simple_right(self)
            to_rot.rotate_simple_left(parent)
        elif self.balance_factor == 1:
            to_rot.rotate_simple_left(self)
            to_rot.rotate_simple_right(parent)

    def insert(self, node: 'AVL'):
        super().insert(node)
        parent = node.parent
        first_node = node
        while parent:
            if not parent.check_balance():
                node.rotate_insert(parent)
                break
            node = parent
            parent = parent.parent
            if node.balance_factor == 0:
                break
        first_node.update_height_and_size()

    def remove(self, node: 'AVL'):
        super().remove(node)
        parent = node.parent
        first_node = node.parent
        while parent:
            if parent.balance_factor == 1 or parent.balance_factor == -1:
                break
            if not parent.check_balance:
                change = self.rotate(parent)
                if change:
                    break
            node = parent
            parent = parent.parent
        first_node.update_height_and_size()

















