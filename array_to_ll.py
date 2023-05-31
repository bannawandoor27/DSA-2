class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def array_to_linked_list(arr):
    if not arr:
        return None

    head = Node(arr[0])
    current = head

    for i in range(1, len(arr)):
        new_node = Node(arr[i])
        current.next = new_node
        current = new_node

    return head

# linkedinlist = ['linkedin','linkedin','linkedin','linkedin','linkedin','linkedin','linkedin',]

# Example usage
array = [1, 2, 3, 4, 5]
linked_list = array_to_linked_list(array)

# Display the linked list
current = linked_list
while current is not None:
    print(current.data, end=" ")
    current = current.next
