from bst import BinarySearchTree

if __name__ == "__main__":
    bst = BinarySearchTree()
    # Insert values
    for v in [14, 15, 13, 16, 10, 20]:
        bst.insert(v)

    print("BST contains 16 (iterative):", bst.contains(16))  # True
    print("BST contains 100 (recursive):", bst.r_contains(100))  # False

    # Traversals
    print("BFS:", bst.bfs())  # [14, 13, 15, 10, 16, 20]
    print("DFS In-Order:", bst.dfs_in_order())  # [10, 13, 14, 15, 16, 20]
    print("DFS Pre-Order:", bst.dfs_pre_order())  # [14, 13, 10, 15, 16, 20]
    print("DFS Post-Order:", bst.dfs_post_order())  # [10, 13, 16, 20, 15, 14]

    # Delete a value
    bst.delete_node(16)
    print("BFS after deleting 16:", bst.bfs())  # [14, 13, 15, 10, 20]
