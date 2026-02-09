# Create and print a singly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
# Create nodes
head = Node(10)
second = Node(20)
third = Node(30)
# Link nodes
head.next = second
second.next = third
# Traverse and print linked list
current = head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")
