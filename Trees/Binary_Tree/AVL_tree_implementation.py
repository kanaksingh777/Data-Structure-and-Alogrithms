class Node():

    def __init__(self,value =None):
        self.value =value
        self.height = 1
        self.left = None 
        self.right = None

class AVL():

    def __init__(self):
        self.root = None

    def insert(self,value):
        self.root = self._insert(self.root,value)


    def _insert(self,node,value):
        if not node:
            return Node(value)
        
        elif value < node.value:
            node.left = self._insert(self,node.left,value)  #this here is till 60.left

        elif value > node.value:
            node.right = self._insert(self,node.right,value)
        
        else :
            print(f"Duplicate num in keys {value} ")
            return node
        
        node.height = 1 + max(self.get_height(node.left),self.get_height(node.right))

        balance =   self.get_balance(node)
        #case left -left
        if balance > 1 and value < node.left.value:
            return self.right_rotate(node)
        
        #case Right-Right

        if balance <-1 1 and value > node.right.value:
            return self.left_rotate(node)
        
        #case left-right

        if balance > 1 and value > node.left.value:
            node.left = self.left_rotate(node)
            return self.right_rotate(node)
        #case right-left 
        if balance <-1 and value < node.right.value:
            node.right  = self.right_rotate(node)
            return self.left_rotate(node)
        
        return node
    
    def left_rotate(self,node):
        new_root = node.right
        t2 = new_root.left

        new_root.left = node
        node.right = t2
        node.height= 1 + max(self.get_height(node.left),self.get_height(node.right))

        new_root.height = 1 + max(self.get_hieght(new_root.left),self.get_height(new_root.right))

        return new_root


            
    def right_roate(self,node):
        new_root = node.left
        t3 = new_root.right

        new_root.right =node
        node.left = t3

        #update 
        node.height = 1 +max(self.get_height(node.left),self.get_height(node.right))
        new_root.height = 1 +max(self.get_height(new_root.left),self.get_height(new_root.right))

        return new_root



        


    def get_height(self,node):

            if not node :
                return 0
            return node.height
        
    def get_balance(self,node):
            if not node :
                return 0
            return self.get_height(node.left)-self.get_height(node.right)
        

            
        


avl = AVL()
keys = [60,50,30,45,77,80,63,90]
for k in keys:
    avl.insert(k)

    