#why linked list over array 
#insertion in an array 
#deletion in a aray --- is difficult
#non continuous memory location 

class Node:

    def __init__(self,value):
        self.data = value
        self.next = None


class LL:
    def __init__(self):

        #empty linked list 
        self.head = None
        self.n = 0 # no of nodes 


    def __len__(self):
        return self.n
    
    def insert_head(self,value):
        new_node =Node(value)
        new_node.next = self.head
        self.head =new_node
        self.n += 1

    def traverse(self):
        curr = self.head
        while curr != None :
            print(curr.data)
            curr = curr.next
    
    def insert_from_tail(self,value):
        new_node = Node(value)
        if self.n == 0:
            self.head = new_node
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = new_node
        self.n += 1


    def insert_in_middle(self,value,k):
        new_node = Node(value)

        new_node = Node(value)

        curr = self.head
        while curr != None:
            if curr.data == k:
                break
            curr = curr.next 
        if curr != None:

            new_node.next = curr.next
            curr.next = new_node
        else: return 'Item not found'

    def reverse_ll(self):
        prev , curr = None , self.head
        while curr != None :
            temp = curr.next

            curr.next= prev
            prev =curr
            curr=temp  

        
s = Node(1)

print(s.next)

l = LL()
l.insert_head(4)
l.insert_head(5)
l.insert_head(30)
l.insert_from_tail(40)
l.insert_in_middle(32,5)
l.reverse_ll()
#print(len(l))
print(l.traverse())
















