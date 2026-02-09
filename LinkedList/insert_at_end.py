# Insert a node at the end of a linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to insert at end
def insert_at_end(head, data):
    new_node = Node(data)

    if head is None:
        return new_node

    current = head
    while current.next:
        current = current.next

    current.next = new_node
    return head

# Create initial linked list: 10 -> 20 -> 30
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

# Insert 40 at end
head = insert_at_end(head, 40)

# Print linked list
current = head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")
