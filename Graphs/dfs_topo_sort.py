"""
Topological sort with DFS

"""


def topological_sort_dfs(graph):
    visited = set()
    stack = []

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor)
        stack.append(node)

    for node in graph:
        if node not in visited:
            dfs(node)

    return stack[::-1]  # Reverse the stack to get the topological order

# Example graph
graph = {
    'A': ['C'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['F'],
    'E': [],
    'F': []
}

print(topological_sort_dfs(graph))  # Output: ['B', 'D', 'F', 'A', 'C', 'E']