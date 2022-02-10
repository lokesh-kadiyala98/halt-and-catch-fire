class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def binary_insert_rec(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.left is None:
                root.left = node
            else:
                binary_insert_rec(root.left, node)
        else:
            if root.right is None:
                root.right = node
            else:
                binary_insert_rec(root.right, node)

def in_order_print_rec(root):
    if not root:
        return
    in_order_print_rec(root.left)
    print(root.data)
    in_order_print_rec(root.right)

def pre_order_print_rec(root):
    if not root:
        return
    print(root.data)
    pre_order_print_rec(root.left)
    pre_order_print_rec(root.right) 

def post_order_print_rec(root):
    if not root:
        return
    post_order_print_rec(root.left)
    post_order_print_rec(root.right)
    print(root.data)

root = Node(3)
binary_insert_rec(root, Node(7))
binary_insert_rec(root, Node(2))
binary_insert_rec(root, Node(1))
binary_insert_rec(root, Node(5))

in_order_print_rec(root)
print()
pre_order_print_rec(root)
print()
post_order_print_rec(root)