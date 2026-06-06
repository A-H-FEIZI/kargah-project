class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node(5)
root.left = Node(3)
root.right = Node(8)
root.left.left = Node(1)
root.left.right = Node(4)
root.right.left = Node(7)
root.right.right = Node(9)

def search(node, target):
    if node is None:
        return False
    if node.data == target:
        return True
    if target < node.data:
        return search(node.left, target)
    else:
        return search(node.right, target)

print(search(root, 7))
print(search(root, 6))