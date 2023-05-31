class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
    
    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node (self,prev_node:Node,data):
        if prev_node is None:
            print('rfedsv')
        else:
            new_node = Node(data)
            new_node.next = prev_node.next
            prev_node.next = new_node
    
    def display(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next
            



    


        
    