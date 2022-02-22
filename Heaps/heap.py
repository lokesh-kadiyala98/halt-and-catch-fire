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
        self.heap[self.size - 1] = 0
        self.size -= 1
        self.heapify_down()

        return value

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

    def heapify_up(self):
        index_pointer = self.size - 1

        while index_pointer > 0 and self.heap[index_pointer] < self.get_value_at_parent(index_pointer):
            self.heap[index_pointer], self.heap[self.get_parent_node(index_pointer)] = self.heap[self.get_parent_node(index_pointer)], self.heap[index_pointer]
            index_pointer = self.get_parent_node(index_pointer)
    
    def heapify_down(self):
        index_pointer = 0

        while self.has_left_child(index_pointer):
            min_child = index_pointer
            min_child = self.get_left_node_pos(index_pointer) if self.heap[min_child] > self.get_value_at_left_child(index_pointer) else min_child
            if self.has_right_child(index_pointer) and self.heap[min_child] > self.get_value_at_right_child(index_pointer):
                min_child = self.get_right_node_pos(index_pointer)
            self.heap[index_pointer], self.heap[min_child] = self.heap[min_child], self.heap[index_pointer]
            index_pointer = min_child

heap = Heap(10)
heap.insert(20)
heap.insert(10)
heap.insert(5)
heap.insert(21)
heap.insert(1)
heap.insert(85)
print('polled', heap.poll())

heap.insert(1)
print('polled', heap.poll())
print('polled', heap.poll())
print(heap.heap)