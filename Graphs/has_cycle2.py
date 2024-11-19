"""
Finding a cycle in a directed acyclic graph.


(has_cycle) Function
Purpose: To check if there is a cycle in the given directed graph.

Parameters: Takes a graph represented as an adjacency list.

Logic:
Initializes two sets: visited to track all visited nodes and path to track the current path of nodes being explored.
Iterates over each vertex in the graph.
For each unvisited vertex, it calls the dfs function.
If dfs returns True, indicating a cycle is found, has_cycle returns True.
If no cycles are found after checking all vertices, it returns False.
dfs Function
Purpose: Performs a Depth-First Search to detect cycles in a directed graph.

Parameters:
vertex: The current node being explored.
visited: A set of nodes that have been visited.
path: A set of nodes in the current path.
graph: The graph represented as an adjacency list.

Logic:
Marks the current vertex as visited by adding it to the visited set.
Adds the vertex to the path set to track the current path.
Iterates over each neighbor of the current vertex.
If a neighbor hasn't been visited, it recursively calls dfs on that neighbor.
If dfs returns True, a cycle is detected, and it returns True.
If a neighbor is already in the path, it indicates a cycle, and it returns True.
After exploring all neighbors, removes the vertex from the path set to backtrack.
If no cycles are found, it returns False.

Test Case
The graph is represented as an adjacency list with nodes and their respective neighbors.
The print(has_cycle(graph)) statement tests the function with the provided graph.

Output
The output True indicates that a cycle was detected in the graph.
This approach is suitable for directed graphs, where the direction of edges is considered, and cycles are detected based on revisiting nodes within the current path. 

"""


def has_cycle(graph):
    visited = set()
    path = set()  # Track the current path
    for vertex in graph:
        if vertex not in visited:
            if dfs(vertex, visited, path, graph):
                return True
    return False

def dfs(vertex, visited, path, graph):
    visited.add(vertex)
    path.add(vertex)  # Add to the current path

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            if dfs(neighbor, visited, path, graph):
                return True
        elif neighbor in path:
            return True

    path.remove(vertex)  # Remove from the current path
    return False

# Test the function
graph = {
    'A': ['B', 'C'],
    'B': ['A'],
    'C': ['A', 'D'],
    'D': ['C'],
    'E': ['G', 'K'],
    'K': ['G', 'E'],
    'G': ['K', 'E']
}
print(has_cycle(graph))