class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left:
                self._insert(node.left, value)
            else:
                node.left = Node(value)
        elif value > node.value:
            if node.right:
                self._insert(node.right, value)
            else:
                node.right = Node(value)
        else:
            print(f"Duplicate value '{value}' not inserted.")

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return -1  # or 0 if you prefer that convention
        return 1 + max(self._height(node.left), self._height(node.right))

    def inorder(self):
        print("Inorder Traversal:", end=" ")
        self._inorder(self.root)
        print()

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.value, end=" ")
            self._inorder(node.right)


# Example usage
if __name__ == "__main__":
    bst = BinarySearchTree()
    for val in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(val)

    bst.inorder()
    print("Tree Height:", bst.height())  # Expected: 2
