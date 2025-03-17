class StackList:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
    # return last item without taking of list
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)
    
    def print_list(self):
        print(self.items)

#
def is_balanced_parentheses(string):
    stack = StackList()
    for character in string:
        if character == "(":
            stack.push(character)
        elif character == ")":
            if stack.is_empty():
                return False
            else:
                stack.pop()
    return stack.is_empty()

#
def reverse_string(string):
    stack = StackList()
    reversed_string = ""
    for char in string:
        stack.push(char)
    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string            

# Ví dụ sử dụng:
stack_list = StackList()
stack_list.push(1)
stack_list.push(2)
stack_list.push(3)

stack_list.print_list()
print("Peek:", stack_list.peek())
stack_list.print_list()
print("Pop:", stack_list.pop())
stack_list.print_list()
print("Peek:", stack_list.peek())

print("is balanced parentheses ?:", is_balanced_parentheses("(((())))"))

my_string = 'hello'
print ( reverse_string(my_string) )