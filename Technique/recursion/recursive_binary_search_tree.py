class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        self.recursive_insert(self.root, value)
    
    def recursive_insert(self, node, value):
        if node is None:
            return Node(value)
        if node.value < value:
            node.right = self.recursive_insert(node.right, value)
        if node.value > value:
            node.left = self.recursive_insert(node.left, value)
        return node
        
    def contains(self, number):
        return self.recursive_contains(self.root, number)
    
    def recursive_contains(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        if node.value < value:
            return self.recursive_contains(node.right ,value)
        if node.value > value:
            return self.recursive_contains(node.left ,value)
    
    def min_value(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value
    

    # Nút cần xóa là nút lá:
    #     -> thay đổi con trỏ của nút cha của nút đó thành NULL
    # Nút cần xóa chỉ có một nút con:
    #     -> thay thế nút cần xoá bằng nút con của nó
    # Nút cần xóa có hai nút con:
    #     -C1 Tìm nút kế thừa: nút nhỏ nhất trong cây con bên phải của nút cần xóa (sao chép giá trị của nút kế thừa vào nút cần xóa, sau đó xóa nút kế thừa)
    #     -C2 Tìm nút tiền nhiệm: nút lớn nhất trong cây con bên trái của nút cần xóa (sao chép giá trị của nút tiền nhiệm vào nút cần xóa, sau đó xóa nút tiền nhiệm)

    def recursive_delete(self, current_node, value):
        # tìm kiếm node cần xoá
        if current_node == None:
            return None
        if value < current_node.value:
            current_node.left = self.recursive_delete(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.recursive_delete(current_node.right, value)
        else:
            # TH nút cần xoá là nút lá 
            if current_node.left == None and current_node.right == None:
                return None
            # TH nút cần xoá có 1 nút con bên trái / phải
            elif current_node.left == None:
                current_node = current_node.right
            elif current_node.right == None:
                current_node = current_node.left
            # TH có cả hai nút con
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.recursive_delete(
                    current_node.right, sub_tree_min
                )
        return current_node

    def delete(self, value):
        self.root = self.__delete_node(self.root, value)


my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print('BST Contains 27:')
print(my_tree.contains(27))

print('\nBST Contains 17:')
print(my_tree.contains(17))


print('\nBST Contains 21:')
print(my_tree.contains(21))
my_tree.delete(21)
print('\nBST Contains 21:')
print(my_tree.contains(21))

"""
    EXPECTED OUTPUT:
    ----------------
    BST Contains 27:
    True

    BST Contains 17:
    False

"""
