def hasCycleUnionFind(edges, n):
    parent = [i for i in range(n)]

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX == rootY:
            return False  # Cycle found
        parent[rootY] = rootX
        return True

    for u, v in edges:
        if not union(u, v):
            return True
    return False