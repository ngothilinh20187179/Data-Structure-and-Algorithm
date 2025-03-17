class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    #
    def swap_first_last(self):
        if self.head is None or not self.head.next:
            return
        else:
            self.head.value, self.tail.value = self.tail.value, self.head.value
    #
    def reverse(self):
        if self.head is None or not self.head.next:
            return
        temp = self.head
        while temp:
            temp.next, temp.prev = temp.prev, temp.next
            temp = temp.prev
        self.head, self.tail = self.tail, self.head
    #
    def is_palindrome(self):
        left_node = self.head
        right_node = self.tail
        
        while left_node and right_node and left_node != right_node and left_node.prev != right_node:
            if left_node.value != right_node.value:
                return False
            left_node = left_node.next
            right_node = right_node.prev
        
        return True
    ##
    def swap_pairs(self):
        if not self.head or not self.head.next:
            return
        current = self.head
        while current and current.next:
            first = current
            second = current.next

            first.next = second.next
            if second.next:
                second.next.prev = first
            
            second.prev = first.prev
            if first.prev:
                first.prev.next = second
            else:
                self.head = second
            
            second.next = first
            first.prev = second
            
            current = first.next
    

my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)

# swap_first_last
print('DLL before swap_first_last():')
my_doubly_linked_list.print_list()

my_doubly_linked_list.swap_first_last()
print('\nDLL after swap_first_last():')
my_doubly_linked_list.print_list()

# reverse
my_doubly_linked_list.reverse()
print('\nDLL after reverse():')
my_doubly_linked_list.print_list()

# palindrome
my_dll_1 = DoublyLinkedList(1)
my_dll_1.append(2)
my_dll_1.append(3)
my_dll_1.append(2)
my_dll_1.append(1)

print('my_dll_1 is_palindrome:')
print( my_dll_1.is_palindrome() )

my_dll_2 = DoublyLinkedList(1)
my_dll_2.append(2)

print('\nmy_dll_2 is_palindrome:')
print( my_dll_2.is_palindrome() )

# swap_pairs
my_dll = DoublyLinkedList(1)
my_dll.append(2)
my_dll.append(3)
my_dll.append(4)

print('my_dll before swap_pairs:')
my_dll.print_list()

my_dll.swap_pairs() 


print('my_dll after swap_pairs:')
my_dll.print_list()