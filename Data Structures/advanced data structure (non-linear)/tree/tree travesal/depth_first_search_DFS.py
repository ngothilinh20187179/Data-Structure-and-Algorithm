class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while (temp):
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
        
    def BFS(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results
    
    def dfs_pre_order(self):
        results = []
        def travesal(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                travesal(current_node.left)
            if current_node.right is not None:
                travesal(current_node.right)
        travesal(self.root)
        return results

    def dfs_post_order(self):
        results = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)
        traverse(self.root)
        return results
            
    def dfs_in_order(self):
        results = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results
    
    # check if tree is binary search tree using DFS in order
    def is_valid_bst(self):
        dfs_in_order_values = self.dfs_in_order()
        if not dfs_in_order_values: # if empty
            return True
        for i in range(1, len(dfs_in_order_values)):
            if dfs_in_order_values[i] <= dfs_in_order_values[i - 1]:
                return False
        return True
    
    # def kth_smallest(self, position):
        # dfs_in_order_values = self.dfs_in_order()
        # if position < 1 or position > len(dfs_in_order_values):
        #     return None
        # return dfs_in_order_values[position - 1]
        
    def kth_smallest(self, k):
        result = None 
        count = 0
        def traverse(current_node):
            nonlocal count, result # Cho biết count và result thuộc phạm vi bên ngoài
            if current_node.left is not None:
                traverse(current_node.left)
            count += 1
            if count == k:
                result = current_node.value
                return
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return result

my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)
my_tree.insert(15)
my_tree.insert(20)
my_tree.insert(22)
my_tree.insert(29)

print(my_tree.dfs_pre_order())
print(my_tree.dfs_post_order())
print(my_tree.dfs_in_order())

print("BST is valid:")
print(my_tree.is_valid_bst())

print(my_tree.kth_smallest(1))
print(my_tree.kth_smallest(3))
print(my_tree.kth_smallest(6))

"""
    EXPECTED OUTPUT:
    ----------------
    [47, 21, 18, 15, 20, 27, 22, 29, 76, 52, 82]
    [15, 20, 18, 22, 29, 27, 21, 52, 82, 76, 47]
    [15, 18, 20, 21, 22, 27, 29, 47, 52, 76, 82]
 """
