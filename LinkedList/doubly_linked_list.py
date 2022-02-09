from platform import node


class Node:
    def __init__(self, value, prev = None, next = None):
        self.value = value
        self.prev = next
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, node):
        # insert first node
        if self.head == None:
            self.head = node
            return

        ptr = self.head
        while ptr.next != None:
            ptr = ptr.next

        node.prev = ptr
        ptr.next = node

    def remove(self, value):
        ptr = self.head

        while ptr.value != value:
            ptr = ptr.next

        if ptr.prev:
            ptr.prev.next = None
            ptr.prev = ptr.prev.prev

        if ptr.next:
            ptr.next.prev = None
            ptr = ptr.next.next

dll = DoublyLinkedList()
dll.append(Node(10))
dll.append(Node(20))
dll.append(Node(30))
dll.append(Node(21))

dll.remove(10)
dll.remove(20)
dll.remove(30)