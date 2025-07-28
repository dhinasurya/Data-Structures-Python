def hasCycleDFS(graph):
    visited = set()
    recStack = set()

    def dfs(node):
        if node in recStack:
            return True
        if node in visited:
            return False
        recStack.add(node)
        for nei in graph[node]:
            if dfs(nei):
                return True
        recStack.remove(node)
        visited.add(node)
        return False

    for node in graph:
        if dfs(node):
            return True
    return False