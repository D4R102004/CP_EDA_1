

class BinarySearchTree:
    def __init__(self, value):
        self._value = value
        self._parent = None
        self._left = None
        self._right = None
        self._height = 0
        self._size = 0

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, key):
        self._value = key

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, node):
        self._parent = node

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node):
        self._left = node

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        self._right = node

    def is_leaf(self):
        return self._right is None and self._left is None

    @property
    def height(self):
        return self._height

    @property
    def size(self):
        return self._size

    def update_height_and_size(self):
        if self.is_leaf():
            self._height = 0
            self._size = 0
        left_height = self.left.height if self.left else -1
        right_height = self.right.height if self.right else -1
        left_size = self.left.size if self.left else 0
        right_size = self.right.size if self.right else 0
        self._height = 1 + max(left_height, right_height)
        self._size = 1 + left_size + right_size
        if self.parent:
            self.parent.update_height_and_size()

    def set_parent(self, node):
        self._parent = node

    def search(self, key):
        if self.value == key:
            return True
        elif key < self.value:
            return (self.left is not None) and self.left.search(key)
        return (self.right is not None) and self.right.search(key)

    # rank
    def rank(self, key):
        def _rank(node, key):
            if node is None:
                return []
            if node.value > key:
                return _rank(node.left, key)
            elif node.value == key:
                return _rank(node.left, key)
            else:
                res = []
                res.extend(node.left.in_order())
                res.append(node)
                res.extend(_rank(node.right, key))
                return res
        return _rank(self, key)

    def insert_key(self, key):
        if self.search(key):
            raise ValueError("Value already in the tree")
        self.insert(BinarySearchTree(key))

    def insert(self, node):
        if self.search(node.value):
            print(f"El valor {node} ya existe")
            return
        if node.value < self._value:
            if self.left is None:
                self.left = node
                self.left.set_parent(self)
            else:
                self.left.insert(node)
        else:
            if self.right is None:
                self.right = node
                self.right.set_parent(self)
            else:
                self.right.insert(node)
        self.update_height_and_size()

    def remove(self, node):
        if not self.search(node.value):
            raise ValueError("Node is not in the tree")
        # Case 1:
        if node.is_leaf():
            if node.parent.left is node:
                node.parent.left = None
            else:
                node.parent.right = None
            self.update_height_and_size()
            return
        # Case 2 A:
        if node.left is None:
            if node.parent.left is node:
                node.parent.left = node.right
                node.right.set_parent(node.parent.left)
            else:
                node.parent.right = node.right
                node.right.set_parent(node.parent.right)
            self.update_height_and_size()
            return
        # Caso 2 B:
        if node.right is None:
            if node.parent.left is node:
                node.parent.left = node.left
                node.left.set_parent(node.parent.left)
            else:
                node.parent.right = node.left
                node.left.set_parent(node.parent.right)
            self.update_height_and_size()
            return
        # Caso 3:
        min_of_max = node.right.lowest()
        node.value = min_of_max.value
        self.update_height_and_size()
        min_of_max.remove(min_of_max)

    def in_order(self):
        return self.internal_in_order(self)

    def internal_in_order(self, node):
        res = []
        if node:
            res.extend(self.internal_in_order(node.left))
            res.append(node)
            res.extend(self.internal_in_order(node.right))
        return res

    def pre_order(self):
        return self.internal_preorder(self)

    def internal_preorder(self, node):
        res = []
        if node:
            res.append(node)
            res.extend(self.internal_preorder(node.left))
            res.extend(self.internal_preorder(node.right))
        return res

    def lowest(self):
        if self.left:
            return self._left.lowest()
        return self

    def highest(self):
        if self.right:
            return self.right.highest()
        return self

    def __repr__(self):
        return str(self.value)






