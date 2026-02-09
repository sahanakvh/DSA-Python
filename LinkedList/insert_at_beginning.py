# Insert a node at the beginning of a linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to insert at beginning
def insert_at_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

# Create initial linked list: 10 -> 20 -> 30
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

# Insert 5 at beginning
head = insert_at_beginning(head, 5)

# Print linked list
current = head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")
