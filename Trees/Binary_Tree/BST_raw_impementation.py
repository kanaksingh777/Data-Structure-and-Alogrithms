class Node():

    def __init__(self,value=None):

        self.value = value 
        self.left = None
        self.right = None

class BST():

    def __init__(self):
        self.root = None

    def insert(self,value):

        if not self.root:

            self.root = Node(value)

        else: 
            self._insert(self.root,value)
    
    def _insert(self,node,value):

        if value < node.value :
            if not node.left :
                node.left = Node(value)
            else : self._insert(node.left, value)

        elif  value > node.value:

            if not node.right:
                node.right = Node(value)
            else:self._insert(node.right,value)

        else :print(f"The BST already have the  number {value}")
    def height(self):
        return self._height(self.root)
    
    def _height(self,node):
        if not node:
            return 0
        return 1 + max(self._height(node.left),self._height(node.right))
    
    def pre_order(self):

        print("pre_order_traversal",end= " ")
        self._pre_order(self.root)

    def _pre_order(self,node):
        if node: 
            print(node.value)

            self._pre_order(node.left)
            self._pre_order(node.right)
    

bst= BST()

for val in [60,50,30,75,45,80,77,100]:
    bst.insert(val)

ans = (bst.height())
bst.pre_order()
print(ans)


    


    