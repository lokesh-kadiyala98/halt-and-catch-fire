class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self, value = None) -> None:
        self.head = Node(value)

    def append(self, node):
        if not self.head.value:
            self.head = node
            return

        ptr = self.head

        while ptr.next:
            ptr = ptr.next
        ptr.next = node

    def get(self, index):
        ptr = self.head
        
        while index and ptr:
            ptr = ptr.next
            index -= 1
        
        if ptr:
            return ptr.value
        else:
            return "ERROR: Element not found"

    def set(self, index, value):
        ptr = self.head

        while index and ptr:
            ptr = ptr.next
            index -= 1

        if ptr:
            ptr.value = value
        else:
            return "ERROR: Index OutOfBounds"

    def remove(self, value):
        if not self.head.value:
            return

        ptr = self.head

        # check if want to remove node is head
        if ptr.value == value:
            self.head = ptr.next
            return

        while ptr.next:
            if ptr.next.value == value:
                break
            ptr = ptr.next

        if ptr.next:
            # check if want to remove node is tail
            if ptr.next.next == None:
                ptr.next = None
                return

            ptr.next = ptr.next.next

    def reverse(self):
        ptr = self.head.next
        prev = self.head
        prev.next = None
        while ptr:
            next = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = next

        self.head = prev

    def traverse(self):
        ptr = self.head
        while ptr:
            print(ptr.value, end=" ")
            ptr = ptr.next
        print()

sll = SinglyLinkedList()
sll.append(Node(10))
sll.append(Node(20))
sll.append(Node(30))
sll.append(Node(200))
sll.append(Node(333))

sll.traverse()
sll.reverse()
sll.traverse()

sll.remove(10)
sll.append(Node(100))
sll.traverse()

sll.reverse()
sll.traverse()
sll.remove(100)

sll.remove(1100)
sll.traverse()

print(sll.get(0))
print(sll.get(3))
print(sll.get(6))

sll.set(2, 40)
sll.set(4, 10)
sll.traverse()