"""
Iterative Depth-First Search: Consider using an iterative DFS.

Why Iterative DFS Uses Less Memory:

Stack Control: Iterative DFS uses an explicit stack, which you control, 
avoiding the overhead of the call stack used in recursive DFS.

Avoids Recursion Depth Limits: In languages with limited recursion depth,
iterative DFS prevents stack overflow errors, making it more memory-efficient for deep graphs.

"""


def iterative_dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A'],
    'D': ['B'],
    'E': ['B'],
}

iterative_dfs(graph, 'A')  # Output: A C B E D