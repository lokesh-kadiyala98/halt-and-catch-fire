# MAX HEAP
class Heap:
    def __init__(self, arr):
        self.heap = arr
        self.size = len(arr)

    def get_value_at_parent(self, node_pos):
        return self.heap[self.get_parent_node(node_pos)]

    def get_value_at_left_child(self, node_pos):
        return self.heap[self.get_left_node_pos(node_pos)]

    def get_value_at_right_child(self, node_pos):
        return self.heap[self.get_right_node_pos(node_pos)]

    @staticmethod
    def get_parent_node(node_pos):
        return (node_pos - 1) // 2

    @staticmethod
    def get_left_node_pos(node_pos):
        return (node_pos * 2) + 1

    @staticmethod
    def get_right_node_pos(node_pos):
        return (node_pos * 2) + 2

    def has_left_child(self, node_pos):
        return (node_pos * 2) + 1 < self.size

    def has_right_child(self, node_pos):
        return (node_pos * 2) + 2 < self.size

    def is_leaf_node(self, node_pos):
        if not self.has_left_child(node_pos) and not self.has_right_child(node_pos):
            return True
        return False

    def heapify(self, index_pointer, size):
        min_child = index_pointer
        left_child = (index_pointer * 2) + 1
        right_child = (index_pointer * 2) + 2

        if left_child < size and self.heap[min_child] < self.get_value_at_left_child(index_pointer):
            min_child = self.get_left_node_pos(index_pointer)
        if right_child < size and self.heap[min_child] < self.get_value_at_right_child(index_pointer):
            min_child = self.get_right_node_pos(index_pointer)

        if min_child != index_pointer:
            # swap
            self.swap(index_pointer, min_child)
            self.heapify(min_child, size)

    def swap(self, fro, to):
        self.heap[fro], self.heap[to] = self.heap[to], self.heap[fro]
    
    def heap_sort(self):
        # heapify first
        for i in range(self.size//2 - 1, -1, -1):
            self.heapify(i, self.size)
        
        # call heapify on last but one element
        # till there are none left
        for i in range(self.size - 1, 0, -1):
            self.swap(0, i)
            self.heapify(0, i)

arr = [12, 11, 13, 5, 18, 6, 7, 1]
heap = Heap(arr)
heap.heap_sort()
print(heap.heap)