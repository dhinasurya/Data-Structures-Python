from collections import deque

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
        while True:
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
        if current_node is None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node

    def r_insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.__r_insert(self.root, value)

    def __r_contains(self, current_node, value):
        if current_node is None:
            return False
        if current_node.value == value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)

    def r_contains(self, value):
        return self.__r_contains(self.root, value)

    def min_value(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    def __delete_node(self, current_node, value):
        if current_node is None:
            return None
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        else:
            if current_node.left is None and current_node.right is None:
                return None
            elif current_node.left is None:
                current_node = current_node.right
            elif current_node.right is None:
                current_node = current_node.left
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)
        return current_node

    def delete_node(self, value):
        self.__delete_node(self.root, value)

    def bfs(self):
        current_node = self.root
        queue = deque()
        results = list()
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.popleft()
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results
    
    def dfs_pre_order(self):
        results = []

        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        
        traverse(self.root)
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

# Example usage and testing
my_bst_tree = BinarySearchTree()
print("Initial root:", my_bst_tree.root)  # Output: None

# Insert values
my_bst_tree.insert(14)
my_bst_tree.insert(15)
my_bst_tree.insert(13)
my_bst_tree.insert(16)

# Print root and its children
print("Root value:", my_bst_tree.root.value)  # Output: 14
print("Left child of root:", my_bst_tree.root.left.value)  # Output: 13
print("Right child of root:", my_bst_tree.root.right.value)  # Output: 15
print("Right child of right child of root:", my_bst_tree.root.right.right.value)  # Output: 16

# Check for presence of values (iterative)
print("Contains 100 (iterative):", my_bst_tree.contains(100))  # Output: False
print("Contains 23 (iterative):", my_bst_tree.contains(23))  # Output: False
print("Contains 16 (iterative):", my_bst_tree.contains(16))  # Output: True

# Check for presence of values (recursive)
print("Contains 100 (recursive):", my_bst_tree.r_contains(100))  # Output: False
print("Contains 23 (recursive):", my_bst_tree.r_contains(23))  # Output: False
print("Contains 16 (recursive):", my_bst_tree.r_contains(16))  # Output: True

# Attempt to insert duplicate values
print("Insert 14 again (should be False):", my_bst_tree.insert(14))  # Output: False
print("Insert 15 again (should be False):", my_bst_tree.insert(15))  # Output: False

# Insert more values
my_bst_tree.insert(10)
my_bst_tree.insert(20)

# Print updated tree structure
print("Left child of left child of root:", my_bst_tree.root.left.left.value)  # Output: 10
print("Right child of right child of root:", my_bst_tree.root.right.right.value)  # Output: 20

# Delete a value
my_bst_tree.delete_node(16)
print("Root value after deleting 16:", my_bst_tree.root.value)  # Output: 14
print("Right child of root after deleting 16:", my_bst_tree.root.right.value)  # Output: 15
print("Right child of right child of root after deleting 16:", my_bst_tree.root.right.right)  # Output: None

# Perform BFS traversal
print("BFS traversal:", my_bst_tree.bfs())  # Output: [14, 13, 15, 10, 20]
# Perform DFS Pre-Order traversal
print("DFS Pre-Order traversal:", my_bst_tree.dfs_pre_order())  

print("DFS Post-Order traversal:", my_bst_tree.dfs_post_order())  

print("DFS In-Order traversal:", my_bst_tree.dfs_in_order())  