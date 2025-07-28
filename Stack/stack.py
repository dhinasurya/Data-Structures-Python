class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1 
    
    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True
    
    def pop(self):
        if self.top is None:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp


my_stack = Stack(23)
my_stack.print_stack()
print("-------------------------------")
my_stack.push(30)
my_stack.push(33)
my_stack.print_stack()
print("-------------------------------")
print("popped value is ", my_stack.pop().value)
print("popped value is ", my_stack.pop().value)
my_stack.print_stack()
print("-------------------------------")
my_stack.push(18)
my_stack.print_stack()
print("-------------------------------")
