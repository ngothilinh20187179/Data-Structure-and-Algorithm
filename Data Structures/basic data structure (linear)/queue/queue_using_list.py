class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item) 

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None
        
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None # or raise IndexError("peek from empty queue")

    def size(self):
        return len(self.items)

    def print_queue(self):
        print(self.items)

# Example Usage:
queue = Queue()

print("Is queue empty?", queue.is_empty())

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue:", end=" ")
queue.print_queue()

print("Peek:", queue.peek())

dequeued_item = queue.dequeue()
print("Dequeued item:", dequeued_item)

print("Queue after dequeue:", end=" ")
queue.print_queue()

print("Size of queue:", queue.size())

print("Is queue empty?", queue.is_empty())

print("dequeue all item")
queue.dequeue()
queue.dequeue()
queue.dequeue()
print("peek after dequeue all item", queue.peek())
print("dequeue after dequeue all item", queue.dequeue())