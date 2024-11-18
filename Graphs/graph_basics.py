"""
This file contains most of the basics you need to understand in building graphs.

"""

def create_adj_matrix(n):
    """
    n = The size of the input of our graph
    """
    return [[0] * n for _ in range(n)]
            

def create_adj_list(n):
    return {i: [] for i in range(n)}


def convert_adj_list_to_adj_matrix(n, adj_list):
    graph = [[0] * n for _ in range(n)]
    for vertex, edges in adj_list.items():
        for edge in edges:
            graph[vertex][edge] = 1
    return graph

def convert_adj_matrix_to_adj_list(n, graph):
    adj_list = {i:[] for i in range(n)}
    for row in range(len(graph)):
        for col in range(len(graph[0])):
            if graph[row][col] == 1:
                adj_list[row].append(col)
    return adj_list


def main():
    # Print multiplt adj matrixs within the rnge of 1-10
    n = 10
    for i in range(1, n + 1):
        print("--------------------")
        print(create_adj_matrix(i))
    
    # Print multiplt adj list within the rnge of 1-10
    n = 10
    for i in range(1, n + 1):
        print("--------------------")
        print(create_adj_list(i))
        
    # Test convert_adj_list_to_adj_matrix function
    adj_list = {
        0: [1, 2],
        1: [2],
        2: [0, 3],
        3: [3]
    }
    n = len(adj_list)
    adj_matrix = convert_adj_list_to_adj_matrix(n, adj_list)
    print("--------------------")
    print(adj_matrix)
    
    graph = [
        [0, 1, 1, 0], 
        [0, 0, 1, 0], 
        [1, 0, 0, 1], 
        [0, 0, 0, 1]
        ]
    n = len(graph)
    adj_list = convert_adj_matrix_to_adj_list(n, graph)
    print("--------------------")
    print(adj_list)

if __name__ == "__main__":
    main()