class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def in_order(root):
    stack = []
    current = root
    while True:
        if current:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            print(current.data)
            current = current.right
        else:
            break

def pre_order(root):
    stack = []
    stack.append(root)
    while stack:
        node = stack.pop()
        print(node.data)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

def peek(stack):
    if len(stack):
        return stack[-1]
    return None

def post_order(root):
    stack = []
    current = root
    while True:
        while current:
            if current.right:
                stack.append(current.right)
            stack.append(current)
            current = current.left

        current = stack.pop()

        if current.right and peek(stack) == current.right:
            right_child = stack.pop()
            stack.append(current)
            current = right_child
        else:
            print(current.data)
            current = None
        if not stack:
            break

root = Node(31)
root.left = Node(26)
root.right = Node(37)
root.left.left = Node(21)
root.left.right = Node(27)
post_order(root)