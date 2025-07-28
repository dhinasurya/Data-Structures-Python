import heapq
from collections import defaultdict

def prims_algorithm(num_nodes, edges):
    # Step 1: Build the graph as an adjacency list
    graph = defaultdict(list)
    for u, v, wt in edges:
        if u != v:  # Skip self-loops
            graph[u].append((wt, v))
            graph[v].append((wt, u))  # Undirected graph

    visited = set()
    min_heap = []
    mst_cost = 0
    mst_edges = []

    # Start from node 0 (or any arbitrary node)
    visited.add(0)
    for wt, neighbor in graph[0]:
        heapq.heappush(min_heap, (wt, 0, neighbor))

    while min_heap and len(visited) < num_nodes:
        wt, u, v = heapq.heappop(min_heap)

        if v in visited:
            continue

        # Accept the edge into MST
        visited.add(v)
        mst_cost += wt
        mst_edges.append((u, v, wt))

        # Add all edges from the newly added node
        for next_wt, nei in graph[v]:
            if nei not in visited:
                heapq.heappush(min_heap, (next_wt, v, nei))

    # If not all nodes were visited, the graph is disconnected
    if len(visited) != num_nodes:
        return None, "Graph is not connected."

    return mst_cost, mst_edges


num_nodes = 5
edges = [
    (0, 1, 1),
    (0, 2, 4),
    (1, 2, 2),
    (1, 3, 5),
    (2, 3, 1),
    (3, 4, 3),
    (4, 4, 10)  # Self-loop, will be ignored
]

cost, mst = prims_algorithm(num_nodes, edges)

print("MST Cost:", cost)
print("Edges in MST:", mst) 