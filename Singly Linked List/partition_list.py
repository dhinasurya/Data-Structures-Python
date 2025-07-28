class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1 
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=" -> ")
            temp = temp.next
        print("None")
    
    def partition_list(self, x):
        if self.head is None:
            return
        
        dummy1 = Node(0)  # Dummy node for less-than-x list
        dummy2 = Node(0)  # Dummy node for greater-or-equal-to-x list
        prev1, prev2 = dummy1, dummy2
        current = self.head

        print("\nStarting Partitioning Process:")
        print("Original list:")
        self.print_list()
        
        while current:
            if current.value < x:
                print(f"Adding {current.value} to the 'less than {x}' list")
                prev1.next = current
                prev1 = prev1.next
            else:
                print(f"Adding {current.value} to the 'greater than or equal to {x}' list")
                prev2.next = current
                prev2 = prev2.next
            current = current.next

        prev2.next = None  # End the greater-than list
        prev1.next = dummy2.next  # Merge the two lists

        self.head = dummy1.next  # Update head to the start of the new list
        
        print("\nFinal partitioned list:")
        self.print_list()

# Test case
ll = LinkedList(3)
ll.append(8)
ll.append(5)
ll.append(10)
ll.append(2)
ll.append(1)
ll.partition_list(5)
