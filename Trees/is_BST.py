from cmath import inf


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def is_BST(root):
    stack = []
    range = [-inf, inf]
    stack.append([root, range])
    while stack:
        [node, range] = stack.pop(0)

        if not(range[0] <= node.data <= range[1]):
            return False

        if node.left:
            stack.append([node.left, [range[0], node.data]])
        if node.right:
            stack.append([node.right, [node.data, range[1]]])

    return True

root = Node(31)
root.left = Node(26)
root.right = Node(37)
root.left.left = Node(21)
root.left.right = Node(27)
root.left.right.left = Node(26)
root.left.right.left.left = Node(26)
print(is_BST(root))