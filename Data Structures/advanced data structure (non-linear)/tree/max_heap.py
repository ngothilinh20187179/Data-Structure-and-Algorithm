class MaxHeap:
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
        # add node to last array, find father, compare, swap
        self.heap.append(value)
        current_node_index = len(self.heap) - 1
        while current_node_index > 0 and self.heap[current_node_index] > self.heap[self._parent(current_node_index)]:
            self._swap(current_node_index, self._parent(current_node_index))
            current_node_index = self._parent(current_node_index)
    
    # restores the heap property when it's been violated
    def _sink_down(self, index):
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if (left_index < len(self.heap) and 
                    self.heap[left_index] > self.heap[max_index]):
                max_index = left_index

            if (right_index < len(self.heap) and 
                    self.heap[right_index] > self.heap[max_index]):
                max_index = right_index

            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return
    
    def remove(self):
        if len(self.heap) == 0: 
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        # replace root node - last node, sink down
        maxNode = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        return maxNode
    
# find_kth_smallest
def find_kth_smallest(nums, k):
    max_heap = MaxHeap()
    for num in nums:
        max_heap.insert(num)
    remove_times = len(nums) - k
    for _ in range(remove_times):
        max_heap.remove()
    return max_heap.heap[0]
    
#
def stream_max(nums):
    max_values = []
    max_heap = MaxHeap()

    for num in nums:
        max_heap.insert(num)
        root_heap = max_heap.heap[0]
        max_values.append(root_heap)

    return max_values

    
myheap = MaxHeap()
myheap.insert(99)
myheap.insert(72)
myheap.insert(61)
myheap.insert(58)
print(myheap.heap)  

myheap.insert(100)
print(myheap.heap)  

myheap.insert(75)
print(myheap.heap)

myheap.remove()
print(myheap.heap)

"""
    EXPECTED OUTPUT:
    ----------------
    [99, 72, 61, 58]
    [100, 99, 61, 58, 72]
    [100, 99, 75, 58, 72, 61]

"""

# test cases find_kth_smallest
nums = [[3,2,1,5,6,4], [1,2,3,4,5,6], [3,2,3,1,2,4,5,5,6]]
ks = [2, 4, 7]

for i in range(len(nums)):
    print(f'Input: {nums[i]} with k = {ks[i]}')
    result = find_kth_smallest(nums[i], ks[i])
    print(f'Output: {result}')
    
# [1, 2, 2, 3, 3, 3, 5, 7, 7]
result = stream_max([1, 2, 2, 3, 1, 2, 5, 7, 6]) 
print(f'stream_max output: {result}')

