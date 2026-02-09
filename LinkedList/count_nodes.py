# Count number of nodes in a linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to count nodes
def count_nodes(head):
    count = 0
    current = head

    while current:
        count += 1
        current = current.next

    return count

# Create linked list: 10 -> 20 -> 30 -> 40
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

# Count nodes
print("Number of nodes:", count_nodes(head))
