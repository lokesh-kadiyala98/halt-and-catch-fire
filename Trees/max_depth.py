class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def get_max_depth(node):
    if not node:
        return -1
    
    return max(get_max_depth(node.left), get_max_depth(node.right)) + 1

root = Node(31)
root.left = Node(26)
root.left.left = Node(21)
root.left.right = Node(27)
root.left.right.left = Node(26)
root.left.right.left.left = Node(26)

print(get_max_depth(root))