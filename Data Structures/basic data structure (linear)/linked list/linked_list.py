class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    # def __init__(self, value):
    #     new_node = Node(value)
    #     self.head = new_node
    #     self.tail = new_node
    #     self.length = 1
    def __init__(self, values=None):
        self.head = self.tail = None
        self.length = 0
        if values is not None:
            if isinstance(values, list):
                for value in values:
                    self.append(value)
            else:
                self.append(values)

    def get(self, position):
        if position < 0 or position >= self.length:
            return None
        else:
            temp = self.head
            for _ in range(position):
                temp = temp.next
            return temp
    def set(self, position, value):
        temp = self.get(position)
        if temp:
            temp.value = value
            return True
        else:
            return False
    def print_list(self):
        temp = self.head
        print("List:")
        while temp is not None:
            print(temp.value)
            temp = temp.next

    ###########
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    def insert(self, position, value):
        length = self.length
        if position < 0 or position > length:
            return False
        elif position == 0:
            self.prepend(value)
        elif position == length:
            self.append(value)
        else:
            new_node = Node(value)
            temp = self.get(position - 1)
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
        return True

    ###########
    # Phải chạy từ đầu head cho tới tail để lấy được item previous của tail
    def pop(self):
        if self.length == 0:
            return None
        else:
            previous = self.head
            temp = self.head
            while temp.next is not None:
                previous = temp
                temp = temp.next
            self.tail = previous
            self.tail.next = None
            self.length -= 1
            if self.length == 0:
                self.head = None
                self.tail = None
            return temp.value
    def pop_first(self):
        if self.length == 0:
            return None
        else:
            first_node = self.head
            self.head = self.head.next
            first_node.next = None
            self.length -= 1
            if self.length == 0:
                self.head = None
                self.tail = None
            return first_node.value
    def remove_item(self, position):
        length = self.length
        if position < 0 or position >= length:
            return None
        elif length == 0:
            return self.pop_first()
        elif position == length - 1: 
            return self.pop()
        else: 
            prev = self.get(position - 1)
            temp = prev.next
            prev.next = temp.next
            temp.next = None
            self.length -= 1
            return temp
    #
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        previous = None
        after = temp.next
        for _ in range(self.length):
            after = temp.next
            temp.next = previous
            previous = temp
            temp = after
            


my_linked_list = LinkedList(4)

my_linked_list.prepend(3)
my_linked_list.append(5)
my_linked_list.print_list()

print("pop: ", my_linked_list.pop())
my_linked_list.print_list()
print("pop first item: ", my_linked_list.pop_first())
my_linked_list.print_list()

my_linked_list.insert(0, 3)
my_linked_list.print_list()
my_linked_list.insert(2, 6)
my_linked_list.print_list()
my_linked_list.insert(2, 5)
my_linked_list.print_list()

my_linked_list.set(2, 6)
my_linked_list.print_list()


my_linked_list.remove_item(2)
my_linked_list.print_list()


my_linked_list.reverse()
my_linked_list.print_list()


# print("Head:", my_linked_list.head.value)
# print("Tail:", my_linked_list.tail.value)
# print("Length:", my_linked_list.length)

# {
#     "head": {
#         "value": 4,
#         "next": {
#             "value": 5,
#             "next": {
#                 "value": 6,   (tail)
#                 "next": None  (tail)
#             }
#         }
#     },
#     "tail": {
#         "value": 6,
#         "next": None
#     },
#     "length": 3
# }
