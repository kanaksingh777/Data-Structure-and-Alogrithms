class Node():
    def __init__(self, value=None):
        self.value = value 
        self.left = None
        self.right = None
        self.height = 1  # New attribute for AVL

class AVL():
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if not node:
            return Node(value)

        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        else:
            print(f"The AVL already has the number {value}")
            return node

        # Update the height
        print(node.value)
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        print(node.height)
        print(node.left.value)
        # Get the balance factor
        balance = self._get_balance(node)

        # Perform rotations
        # Case 1 - Left Left
        if balance > 1 and value < node.left.value:
            return self._right_rotate(node)

        # Case 2 - Right Right
        if balance < -1 and value > node.right.value:
            return self._left_rotate(node)

        # Case 3 - Left Right
        if balance > 1 and value > node.left.value:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)

        # Case 4 - Right Left
        if balance < -1 and value < node.right.value:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def _left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def pre_order(self):
        print("pre_order_traversal", end=" ")
        self._pre_order(self.root)

    def _pre_order(self, node):
        if node:
            print(node.value, end=" ")
            self._pre_order(node.left)
            self._pre_order(node.right)
avl = AVL()
for val in [60, 50, 30, 75, 45, 80, 77, 100]:
    avl.insert(val)

avl.pre_order()
