class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
    def print_list_values(self):
        current = self.head
        values = []
        while current:
            values.append(current.value)
            current = current.next
        print(values)
    # middle node - without using length
    def find_middle_node(self):
        pointer_first = self.head
        pointer_second = self.head
        while pointer_second and pointer_second.next is not None:
            pointer_first = pointer_first.next
            pointer_second = pointer_second.next.next
        return pointer_first
    # list has loop - without using length
    def has_loop(self):
        slow_pointer = self.head
        fast_pointer = self.head
        while fast_pointer and fast_pointer.next is not None:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if slow_pointer == fast_pointer:
                return True
        return False
    # without using tail
    def partition_list(self, x):
        if self.head is None:
            return
        less_head = Node(0)  
        less_tail = less_head
        greater_head = Node(0) 
        greater_tail = greater_head
        temp = self.head
        while temp:
            if temp.value < x:
                less_tail.next = temp
                less_tail = temp
            else:
                greater_tail.next = temp
                greater_tail = temp
            temp = temp.next
        greater_tail.next = None
        less_tail.next = greater_head.next  # nối phần cuối ở less vào phần sau phần head của greater (để loại bỏ 0 của greater)
        self.head = less_head.next  # loại bỏ node value = 0 ban đầu của less
    # use Set() to remove
    def remove_duplicates(self):
        if self.head is None:
            return
        temp = self.head
        list_remove_duplicates = set()
        previous = self.head
        while temp:
            if temp.value in list_remove_duplicates:
                previous.next = temp.next
            else:
                list_remove_duplicates.add(temp.value)
                previous = temp
            temp = temp.next
    # binary to decimal
    def binary_to_decimal(self):
        len = self.length
        if len == 0:
            return 0
        else:
            temp = self.head
            decimal = 0
            while temp:
                if temp.value == 1:
                    decimal += (2 ** (len - 1))
                len -= 1
                temp = temp.next
            return decimal
    # without using tail
    def reverse_between(self, start_index, end_index):
        if self.head is None or start_index < 0 or end_index >= self.length or start_index > end_index:
            return None
        if start_index == end_index:
            return None
        dummy = Node(0)
        dummy.next = self.head
        prev_start = dummy
        for _ in range(start_index):
            prev_start = prev_start.next

        start = prev_start.next
        current = start
        prev = None
        for _ in range(end_index - start_index + 1):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        prev_start.next = prev
        start.next = current
        self.head = dummy.next

# find kth node from the end of list - without using length
# p2 chạy k bước, sau đó chạy p1 p2 từng bước 1 tới khi p2 cuối danh sách
def find_kth_from_end(ll, k):
    if k <= 0 or not ll.head:
        return None
    else:
        first_pointer = ll.head
        second_pointer = ll.head
        for _ in range(k):
            if second_pointer:
                second_pointer = second_pointer.next
            else:
                return None  # k > length of ll
        while second_pointer is not None:
            first_pointer = first_pointer.next
            second_pointer = second_pointer.next
        return first_pointer


my_linked_list = LinkedList(1)
my_linked_list.append(4)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(2)
my_linked_list.append(5)
#
my_linked_list.partition_list(3)
my_linked_list.print_list_values()
#
k = 2
result = find_kth_from_end(my_linked_list, k)
print(result.value)
#
print(my_linked_list.find_middle_node().value)
#
my_linked_list.tail.next = my_linked_list.head
print(my_linked_list.has_loop())
