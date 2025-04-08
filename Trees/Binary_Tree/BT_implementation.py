class Node():

    def __init__(self,value=None):

        self.value = value
        self.left = None
        self.right = None

    
class Binary_Tree():

    def populate(self):

        self.value = int(input("Enter the root Node:"))

        self.root = Node(self.value)

        self._populate(self.root)

    def _populate(self,node):

        left = input(f"Do you want to enter to the left of {node.value} ?(Y/N:)")

        if left.lower() == 'y':
            left_value = int(input(f'Enter to the left of {node.value}:'))
            node.left = Node(left_value)
            self._populate(node.left)

        right = input(f'do you want to enter to the right of {node.value}?(Y/N:)')

        if right.lower() == 'y':
            right_value = int(input(f'enter to the right of {node.value}:'))
            node.right = Node(right_value)
            self._populate(node.right)

    def display(self):
        self._display(self.root)

    def _display(self, node, indent=""):
        if node is None:
            return
        print(indent + str(node.value))
        self._display(node.left, indent + "  L")
        self._display(node.right, indent + "  R-")

tree = Binary_Tree()
tree.populate()
print("\n print tree structure")
tree.display()