"""
Khan's lgorithm for topo sort.
"""


from collections import deque

def kahn_topological_sort(graph):
    # Calculate in-degrees of all nodes
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    # Initialize a queue with nodes having in-degree 0
    queue = deque([node for node in graph if in_degree[node] == 0])
    topological_order = []

    while queue:
        node = queue.popleft()
        topological_order.append(node)

        # Decrease the in-degree of neighbors
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            # If in-degree becomes 0, add to queue
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Check if topological sort is possible (i.e., no cycle)
    if len(topological_order) == len(graph):
        return topological_order
    else:
        return "Graph has a cycle, topological sort not possible."

# Example graph
graph = {
    'A': ['C'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['F'],
    'E': [],
    'F': []
}

print(kahn_topological_sort(graph))  # Output: ['A', 'B', 'D', 'F', 'C', 'E']