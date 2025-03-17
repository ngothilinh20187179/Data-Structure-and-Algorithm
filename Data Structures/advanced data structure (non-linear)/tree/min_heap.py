class MinHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        current_node_index = len(self.heap) - 1
        while current_node_index > 0 and self.heap[current_node_index] < self.heap[self._parent(current_node_index)]:
            self._swap(current_node_index, self._parent(current_node_index))
            current_node_index = self._parent(current_node_index)
 
    def _sink_down(self, index):
        min_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if (left_index < len(self.heap) and 
                    self.heap[left_index] < self.heap[min_index]):
                min_index = left_index

            if (right_index < len(self.heap) and 
                    self.heap[right_index] < self.heap[min_index]):
                min_index = right_index

            if min_index != index:
                self._swap(index, min_index)
                index = min_index
            else:
                return

    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        minHeap = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        return minHeap
 
myheap = MinHeap()
myheap.insert(12)
myheap.insert(10)
myheap.insert(8)
myheap.insert(6)
print(myheap.heap)  # [6, 8, 10, 12]

myheap.insert(4)
print(myheap.heap)  # [4, 6, 10, 12, 8]

myheap.insert(2)
print(myheap.heap)  # [2, 6, 4, 12, 8, 10]

myheap.insert(4)
print(myheap.heap)  # [2, 6, 4, 12, 8, 10, 4]


myheap.insert(9)
print(myheap.heap)  # [2, 6, 4, 9, 8, 10, 4, 12]

removed = myheap.remove()
print(f'Removed: {removed}, Heap: {myheap.heap}') # [4, 6, 4, 9, 8, 10, 12]



