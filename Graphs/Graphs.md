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
      - Not best for sprse graphs.
      - Adj matrix has high space complexity.