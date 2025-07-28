from collections import deque
from node import Node


class BinarySearchTree:
    """Binary Search Tree implementation with common operations."""

    def __init__(self):
        self.root = None

    def insert(self, value):
        """Insert a value into the BST (iterative). Returns True if inserted, False if duplicate."""
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False  # Duplicate value
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
        """Check if value exists in BST (iterative)."""
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    def __r_insert(self, current_node, value):
        """Helper for recursive insert."""
        if current_node is None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node

    def r_insert(self, value):
        """Insert a value into the BST (recursive)."""
        if self.root is None:
            self.root = Node(value)
        else:
            self.__r_insert(self.root, value)

    def __r_contains(self, current_node, value):
        """Helper for recursive contains."""
        if current_node is None:
            return False
        if current_node.value == value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)

    def r_contains(self, value):
        """Check if value exists in BST (recursive)."""
        return self.__r_contains(self.root, value)

    def min_value(self, current_node):
        """Find the minimum value in a subtree."""
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    def __delete_node(self, current_node, value):
        """Helper for recursive node deletion."""
        if current_node is None:
            return None
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        else:
            # Node found
            if current_node.left is None and current_node.right is None:
                return None  # No children
            elif current_node.left is None:
                return current_node.right  # One child (right)
            elif current_node.right is None:
                return current_node.left  # One child (left)
            else:
                # Two children: replace with min value from right subtree
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__delete_node(
                    current_node.right, sub_tree_min
                )
        return current_node

    def delete_node(self, value):
        """Delete a node with the given value from the BST."""
        self.root = self.__delete_node(self.root, value)

    def bfs(self):
        """Breadth-First Search traversal. Returns list of values."""
        results = []
        if not self.root:
            return results
        queue = deque([self.root])
        while queue:
            current_node = queue.popleft()
            results.append(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        return results

    def dfs_pre_order(self):
        """Depth-First Search (Pre-Order) traversal."""
        results = []

        def traverse(node):
            if node:
                results.append(node.value)
                traverse(node.left)
                traverse(node.right)

        traverse(self.root)
        return results

    def dfs_post_order(self):
        """Depth-First Search (Post-Order) traversal."""
        results = []

        def traverse(node):
            if node:
                traverse(node.left)
                traverse(node.right)
                results.append(node.value)

        traverse(self.root)
        return results

    def dfs_in_order(self):
        """Depth-First Search (In-Order) traversal."""
        results = []

        def traverse(node):
            if node:
                traverse(node.left)
                results.append(node.value)
                traverse(node.right)

        traverse(self.root)
        return results
