from typing import List
class Solution:
    def kruskalMST(self, n: int, edges: List[List[int]]) -> int:
        # Step 1: Sort all edges by weight
        edges.sort(key=lambda x: x[2])  # Each edge: [u, v, weight]
        
        # Step 2: Initialize Union-Find
        parent = [i for i in range(n)]
        rank = [1] * n  # Optional: For union by rank
        
        # Find with path compression
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        # Union with rank
        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX == rootY:
                return False  # already connected (cycle)
            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            elif rank[rootY] > rank[rootX]:
                parent[rootX] = rootY
            else:
                parent[rootY] = rootX
                rank[rootX] += 1
            return True
        
        # Step 3: Kruskal's main loop
        mst_weight = 0
        edges_used = 0
        
        for u, v, weight in edges:
            if union(u, v):  # only add if no cycle
                mst_weight += weight
                edges_used += 1
                if edges_used == n - 1:
                    break
        
        return mst_weight if edges_used == n - 1 else -1  # -1 means MST not possible

n = 4
edges = [
    [0, 1, 1],
    [1, 2, 4],
    [0, 2, 3],
    [2, 3, 2],
    [0, 3, 5]
]

sol = Solution()
print(sol.kruskalMST(n, edges))  # Output: 6