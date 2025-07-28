def hasCycleDFS(graph, n):
    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for nei in graph[node]:
            if nei not in visited:
                if dfs(nei, node):
                    return True
            elif nei != parent:
                return True
        return False

    for node in range(n):
        if node not in visited:
            if dfs(node, -1):
                return True
    return False
