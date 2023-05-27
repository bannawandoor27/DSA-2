class Node:
    def __init__(self,data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node
    
    def print(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
    