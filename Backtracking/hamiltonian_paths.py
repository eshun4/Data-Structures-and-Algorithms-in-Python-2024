"""
A Hamiltonian path is a path in an undirected or directed graph that visits each vertex exactly once. 
Unlike a Hamiltonian cycle, a Hamiltonian path does not need to return to the starting vertex. 
This concept is widely used in graph theory and has applications in various fields such as 
optimization, routing, and scheduling.

Key characteristics:
- The path must visit every vertex in the graph exactly once.
- The graph can be directed or undirected.
- The path does not necessarily form a cycle.

Hamiltonian paths are often used to solve problems like the Traveling Salesman Problem (TSP) 
and are related to NP-complete problems in computational complexity theory.
"""


def hamiltonian_path(graph, current, count, visited, n):
    if count == n:
        return True

    visited[current] = 1

    for neighbor in graph[current]:
        if not visited[neighbor]:
            if hamiltonian_path(graph, neighbor, count + 1, visited, n):
                return True

    visited[current] = 0
    return False


def has_hamiltonian_path(graph):
    n = len(graph)
    for start in graph:
        visited = [0] * n
        if hamiltonian_path(graph, start, 1, visited, n):
            return True
    return False


def main():
    graph1 = {
        0: [1, 2],
        1: [0, 3],
        2: [0, 3],
        3: [1, 2]
    }
    print("Example 1:", has_hamiltonian_path(graph1))  # Expected: True

    graph2 = {
        0: [1],
        1: [0, 2],
        2: [1],
        3: [4],
        4: [3]
    }
    print("Example 2:", has_hamiltonian_path(graph2))  # Expected: False

    graph3 = {
        0: [1, 2, 3],
        1: [0, 2, 3],
        2: [0, 1, 3],
        3: [0, 1, 2]
    }
    print("Example 3:", has_hamiltonian_path(graph3))  # Expected: True

    graph4 = {
        0: [1],
        1: [0],
        2: [3],
        3: [2]
    }
    print("Example 4:", has_hamiltonian_path(graph4))  # Expected: False


if __name__ == "__main__":
    main()
