# MIN HEAP 
class Heap:
    def __init__(self, max_size):
        self.max_size = max_size
        self.size = 0
        self.heap = [0] * max_size
    
    def insert(self, value):
        if self.size + 1 >= self.max_size:
            print('size exceeded')
            return

        self.heap[self.size] = value
        self.size += 1
        self.heapify_up()

    def poll(self):
        if self.size == 0:
            print('nothing to remove')
            return
        
        value = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.heapify_down()

        return value

    def get_value_at_parent(self, node_pos):
        return self.heap[(node_pos - 1) // 2]
    
    def get_left_child(self, node_pos):
        return self.heap[(node_pos * 2) + 1]

    def get_right_child(self, node_pos):
        return self.heap[(node_pos * 2) + 2]

    def heapify_up(self):
        index_pointer = self.size - 1

        while index_pointer >= 0 and self.heap[index_pointer] < self.get_value_at_parent(index_pointer):
            self.heap[index_pointer], self.heap[(index_pointer - 1) // 2] = self.heap[(index_pointer - 1) // 2], self.heap[index_pointer]
            index_pointer = (index_pointer - 1) // 2
    
    def heapify_down(self):
        index_pointer = 0

        while index_pointer <= ((index_pointer * 2) + 1):
            min_child = index_pointer
            min_child = ((index_pointer * 2) + 1) if self.heap[min_child] < self.get_left_child(index_pointer) else min_child
            if index_pointer <= ((index_pointer * 2) + 2) and self.heap[min_child] < self.get_right_child(index_pointer):
                min_child = index_pointer
            self.heap[index_pointer], self.heap[min_child] = self.heap[min_child], self.heap[index_pointer]
            index_pointer = min_child

heap = Heap(10)
heap.insert(20)
heap.insert(10)