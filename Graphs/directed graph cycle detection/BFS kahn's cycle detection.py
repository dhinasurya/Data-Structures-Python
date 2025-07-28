from collections import defaultdict, deque


def hasCycleBFS(numCourses, prerequisites):
    graph = defaultdict(list)
    in_degree = [0] * numCourses

    for dest, src in prerequisites:
        graph[src].append(dest)
        in_degree[dest] += 1

    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    count = 0

    while queue:
        node = queue.popleft()
        count += 1
        for nei in graph[node]:
            in_degree[nei] -= 1
            if in_degree[nei] == 0:
                queue.append(nei)

    return count != numCourses  # If some nodes are never visited, cycle exists
