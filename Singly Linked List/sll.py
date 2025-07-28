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
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

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

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def bubble_sort(self):
        if not self.head or not self.head.next:
            return  # No need to sort if the list is empty or has only one node

        end = None  # Marks the end of the sorted portion
        while (
            end != self.head
        ):  # base condition to reduce the base no of elements after big element is sorted
            current = self.head
            while current.next != end:
                if current.value > current.next.value:  # Compare adjacent nodes
                    # Swap the values of the two nodes
                    current.value, current.next.value = (
                        current.next.value,
                        current.value,
                    )
                current = current.next
            end = current  # Move the end marker to the last sorted node

    def selection_sort(self):
        if not self.head or not self.head.next:
            return  # No need to sort if the list is empty or has only one node

        current = self.head
        while current:
            min_node = current  # Assume the current node is the smallest
            next_node = current.next
            while next_node:
                if next_node.value < min_node.value:  # Find the smallest node
                    min_node = next_node
                next_node = next_node.next
            # Swap the values of the current node and the smallest node
            current.value, min_node.value = min_node.value, current.value
            current = current.next

    def insertion_sort(self):
        if not self.head or not self.head.next:
            return  # No need to sort if the list is empty or has only one node

        sorted_head = None  # Start with an empty sorted list
        current = self.head

        while current:
            next_node = current.next  # Save the next node
            # Insert the current node into the sorted list
            if not sorted_head or current.value < sorted_head.value:
                current.next = sorted_head
                sorted_head = current
            else:
                sorted_current = sorted_head
                while sorted_current.next and sorted_current.next.value < current.value:
                    sorted_current = sorted_current.next
                current.next = sorted_current.next
                sorted_current.next = current
            current = next_node

        self.head = sorted_head  # Update the head to the new sorted list
