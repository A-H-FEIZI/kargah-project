class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node10 = Node(10)
node12 = Node(12)

node1.next = node2
node2.next = node3
node3.next = node10
node10.next = node12

current = node1

while current != None:
    print(current.data)
    current = current.next