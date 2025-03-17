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
            self.tail = new_node
        self.length += 1

    def bubble_sort(self):
        if self.head is None or self.length == 1:
            return
        step = 0
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current and current.next:
                if current.value > current.next.value:
                    current.value, current.next.value = current.next.value, current.value
                    swapped = True
                current = current.next
                step += 1
                print("step", step)
                
    # bình thường duyệt 1 lượt và cập nhật phần tử max rồi đặt cuối ds
    # ở LL, tìm min và đặt đầu ll
    def selection_sort(self):
        if self.head is None or self.length == 1:
            return
        current = self.head
        while current:
            min_node = current
            inner_current = current.next
            while inner_current:
                if inner_current.value < min_node.value:
                    min_node = inner_current
                inner_current = inner_current.next

            if min_node != current:
                current.value, min_node.value = min_node.value, current.value

            current = current.next
    
    # tách 2 phần đã sx và phần chưa sx
    # bình thường lấy phần tử đầu tiên của phần chưa sx và so sánh từ cuối ds đã sx rồi chèn
    # ở LL thì lấy phần tử đầu tiên của phần chưa sx và so sánh từ đầu ds đã sx
    def insertion_sort(self):
        if self.head is None or self.head.next is None:
            return
        # tách riêng phần tử đầu (đã sx) và phần còn lại (chưa sx))
        ordered = self.head
        unorderd = self.head.next
        ordered.next = None
        
        # duyệt từ ll chưa sx tới None thì dừng
        temp = unorderd
        while temp:
            temp_next = temp.next
            # phần tử đầu (ds chưa sx) nhỏ hơn/= phần tử đầu (ds đã sx)
            if temp.value <= ordered.value:
                temp.next = ordered
                ordered = temp
            # phần tử đầu (ds chưa sx) lớn hơn các phần tử (ds đã sx) -> tìm vị trí để chèn
            else:
                search = ordered
                while search.next and search.next.value < temp.value:
                    search = search.next
                temp.next = search.next
                search.next = temp
                if temp.next is None:
                    self.tail = temp
            temp = temp_next
        self.head = ordered
        

my_linked_list = LinkedList(5)
my_linked_list.append(3)
my_linked_list.append(8)
my_linked_list.append(4)
my_linked_list.append(6)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.bubble_sort()

print("\nSorted Linked List:")
my_linked_list.print_list()
