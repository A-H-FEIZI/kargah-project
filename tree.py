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

def print_tree(node):
    if node is None:
        return
    print(node.data)
    print_tree(node.left)
    print_tree(node.right)

print_tree(root)