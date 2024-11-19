## Graphs

- Building and Analyzing Graphs with Adjacency Matrix
  - Using adjacency mtrixes to drive a social network

- Adjacency Matrix
  - Connecting to someone on social media is equal to an edge in an adj matrix.
  - Square matrix, a two-dimensional array where each cell '(i,j)' represents the weight of the edge between vertices i nd j.
  - e.g. """ M = [
             [0, 1, 1],
             [1, 0, 0],
             [1, 0 ,0]
            ] """
  - 1 represents a connection and 0 represents no edge.
  - When do we use an adj matrix?
    - It depends:
      - It is the best option for dense(One with mny edges relative to the number od vertices) graphs.
      - Not best for sparse graphs.
      - Adj matrix has high space complexity.
- Adjacency List
  - Real-world problems of adjacency lists
  - It simplifies a graph into its simplest and most crucial form
  - Best for sparse graphs(WIth few edges).
  - Space-efficency compared to matrixes.
- Depth - First Search Graphs
  - Used in fields like network engineering and genealogies.
  - Goes deep into the path to traverse all nodes and then backtracks if there is no pathway.
  - This process continues until all paths have been explored.
  - Time and SPace Complexity of DFS:
    - Time Complecity: O(V + E)
    - Space Complexity: O(V), where V represent the vertices and E represents the Edges.
    - Analysis of DFS:
      - Connections within graphs.
      - DFS leaves no stone unturned.
      - Time - wise it thrives on densely connected graphs where the probability of finding the target quickly is higher than that of other search algorithms like BFS.
      - DFS can see loops in graphs.
      - DFS is one of the most -efficient ways in traversing data sets
      - Real - world applications of DFS.
      - Good for cycle detection.
- Topological Sort also uses DFS or another algorithm known as Khan's algorithm.
- Directed Acyclic Graphs (DAGs)
  - Definition: A DAG is a directed graph with no cycles. This means there is no way to start at a node and follow a consistently directed path that eventually loops back to the starting node.
  - Properties:
  - Acyclic: No cycles exist.
  - Directed: All edges have a direction.
  - Applications: Used in scheduling problems, data processing pipelines, and more.
- Topological Sorting
  - Purpose: To order the vertices of a DAG such that for every directed edge u -> v, u comes before v.
  - Characteristics:
    - Linear Order: Provides a sequence of nodes.
    - Multiple Valid Orders: A DAG can have more than one valid topological sort.
- Algorithms for Topological Sort
  - DFS-Based Approach:
    - Perform a DFS on the graph.
    - Once a node has no unvisited neighbors, add it to a stack.
    - After DFS completes, the stack contains nodes in topologically sorted order.
  - Steps:
    - Mark all nodes as unvisited.
    - For each unvisited node, perform DFS.
    - On finishing a node, push it onto a stack.
    - Pop nodes from the stack to get the topological order.
  - Khan's algorithm Steps:
    - Calculate In-Degrees:
    - Initialize an in-degree count for each node in the graph. The in-degree represents the number of incoming edges to a node.
    - Initialize the Queue:
    - Create a queue and enqueue all nodes with an in-degree of 0 (nodes with no dependencies).
    - Process the Queue:
    - While the queue is not empty:
    - Dequeue a node and add it to the topological order.
    - For each neighbor of the dequeued node, reduce its in-degree by 1.
    - If a neighbor's in-degree becomes 0, enqueue it.
    - Check for Cycles:
    - After processing all nodes, check if the topological order includes all nodes in the graph.
    - If not, the graph contains a cycle, and a topological sort is not possible.
    - Return the Topological Order:
    - Khan's algorithm follows a reverse post-order pattern.

If the graph is a DAG, return the topological order obtained from the queue processing.

- In a topological sort problem, to increase the complexity, you might encounter additional challenges such as:
  - Cycle Detection: You may be asked to first check if the graph is a DAG. If a cycle is detected, topological sorting isn't possible.
  - Multiple Valid Orders: You might need to find all possible topological orders, not just one.
  - Weighted Edges: Incorporating weights and finding a topological order that minimizes or maximizes a certain criterion.
  - Dynamic Graphs: Handling graphs where nodes or edges can be added or removed, requiring updates to the topological order.
  - Parallel Processing: Optimizing the order for parallel execution, considering resource constraints.
  - Real-World Constraints: Incorporating additional constraints like deadlines or resource availability.
  - These variations require a deeper understanding of graph theory and algorithmic strategies to solve effectively.
  
- When trying to determine the best approach for a problem involving topological sorting, consider the following steps:
- Understand the Problem Requirements:
- Identify if the problem involves ordering tasks, courses, or dependencies.
- Check if the problem specifies a particular traversal order or method.
- Analyze the Sample Output:
- Look for patterns in the sample output that suggest depth-first (DFS) or breadth-first (Kahn's algorithm) exploration.
- Consider Graph Characteristics:
- Ensure the graph is a Directed Acyclic Graph (DAG), as topological sorting is only applicable to DAGs.
- Evaluate Constraints and Performance:
- Consider the size of the graph and any performance constraints.
- DFS is recursive and may be more intuitive for smaller graphs.
- Kahn's algorithm is iterative and may be more suitable for larger graphs or when cycle detection is crucial.
- Check for Additional Requirements:
- Determine if cycle detection is necessary.
- Consider if multiple valid topological orders are needed.
- Choose Based on Familiarity and Simplicity:
- If both methods are applicable, choose the one you are more comfortable with or find simpler to implement.

### Why do you use the parent method for undirectd graphs and the path method for dags?
The use of the parent method in undirected graphs and the path method in directed acyclic graphs (DAGs) is due to the nature of these graph types:

Undirected Graphs:

In undirected graphs, edges don't have a direction, so when you traverse from one node to another, you can easily end up backtracking to the node you just came from.
The parent method helps avoid counting this immediate backtrack as a cycle by keeping track of the node you came from. If you encounter a visited node that isn't the parent, it indicates a cycle.
Directed Acyclic Graphs (DAGs):

In DAGs, edges have a direction, and by definition, they don't contain cycles.
The path method is used to track the current path of nodes being visited. If a node is revisited while still in the current path, it indicates a cycle. However, since DAGs are acyclic, this method is more about ensuring the graph remains acyclic when adding edges or nodes.
Each method is tailored to the specific properties and challenges of the graph type it addresses.