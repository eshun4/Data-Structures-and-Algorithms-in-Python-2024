def dfs(graph, start, visited, discovery_time, finish_time, time):
    # Mark the node as visited
    visited.add(start)
    # Set discovery time
    discovery_time[start] = time
    # Increment time
    time += 1

    # Visit all adjacent nodes
    for neighbor in graph[start]:
        if neighbor not in visited:
            time = dfs(graph, neighbor, visited, discovery_time, finish_time, time)
    
    # Set finish time
    finish_time[start] = time
    # Increment time
    time += 1
    return time


def main():
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    start_node = 'A'
    visited = set()
    discovery_time = {node: -1 for node in graph}
    finish_time = {node: -1 for node in graph}
    time = 0

    time = dfs(graph, start_node, visited, discovery_time, finish_time, time)

    print("Discovery Time:", discovery_time)
    print("Finish Time:", finish_time)


if __name__ == "__main__":
    main()
