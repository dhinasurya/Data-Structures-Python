from collections import deque


def hasCycleBFS(graph, n):
    visited = set()

    for start in range(n):
        if start in visited:
            continue
        queue = deque([(start, -1)])
        while queue:
            node, parent = queue.popleft()
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    queue.append((nei, node))
                elif nei != parent:
                    return True
    return False