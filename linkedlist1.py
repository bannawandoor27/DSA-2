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
        lltr = ''
        while current:
            lltr+=str(current.data)+' --> '
            current = current.next
        print(lltr)
    
    def insert_at_end(self,data):
        if self.head is None:
            self,head = Node(data,None)
            return
        
        itr  = self.head



if __name__ == '__main__':
    ll = LinkedList()
    for i in  reversed(range(1,11)):ll.insert_at_beginning(i)
    ll.print()