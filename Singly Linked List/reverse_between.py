import time

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
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1

    def print_list(self, highlight_nodes=None):
        """Prints the list and highlights given nodes."""
        temp = self.head
        result = []
        while temp:
            if highlight_nodes and temp in highlight_nodes:
                result.append(f"[{temp.value}]")  # Highlight important nodes
            else:
                result.append(str(temp.value))
            temp = temp.next
        print(" -> ".join(result) + " -> None")

    def visualize_reverse_between(self, start_index, end_index):
        if not self.head or start_index == end_index:
            return

        print("\nInitial Linked List:")
        self.print_list()
        time.sleep(1)

        # Step 1: Move `prev` to the node before the reversal section
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy

        for _ in range(start_index):
            prev = prev.next  # Move prev to node before reversal

        prev_sublist = prev
        current = prev.next
        tail = current  # Tail of the sublist to be reversed

        print("\nStep 1: Marking nodes before reversal")
        self.print_list(highlight_nodes=[prev, current])
        time.sleep(1)

        # Step 2: Reverse the sublist in place
        prev = None
        for i in range(end_index - start_index + 1):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

            print(f"\nStep {i+2}: Reversing nodes...")
            self.print_list(highlight_nodes=[prev, current])
            time.sleep(1)

        # Step 3: Reconnect reversed sublist back to the list
        prev_sublist.next = prev
        tail.next = current

        if start_index == 0:
            self.head = prev  # Update head if reversing from index 0

        print("\nFinal Reversed List:")
        self.print_list()

# 🧪 Test with your own examples!
linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

linked_list.visualize_reverse_between(2, 4)
