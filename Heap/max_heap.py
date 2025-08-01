class MaxHeap:
    def __init__(self):
        self.heap = list()

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def _sink_down(self, index):
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if (left_index < len(self.heap)) and self.heap[left_index] > self.heap[
                max_index
            ]:
                max_index = left_index

            if (right_index < len(self.heap)) and self.heap[right_index] > self.heap[
                max_index
            ]:
                max_index = right_index

            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def remove(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        max_value = self.heap[0]

        self.heap[0] = self.heap.pop()
        self._sink_down(0)

        return max_value


# Example usage
heap = MaxHeap()
heap.insert(10)
heap.insert(20)
heap.insert(5)
heap.insert(30)

print(heap.heap)  # Output: [30, 20, 5, 10]

heap.insert(28)
heap.insert(50)
heap.insert(310)

print(heap.heap)  # Output: [310, 50, 30, 10, 20, 5, 28]

max_value = heap.remove()
print(max_value)  # Output: 310
print(heap.heap)  # Output: [50, 28, 30, 10, 20, 5]


max_value = heap.remove()
print(max_value)
print(heap.heap)
