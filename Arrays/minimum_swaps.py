"""
Minimum Swaps to Sort

Given an array of size N, find the minimum number of swaps needed to make the array sorted.

Sample Input
a1 = [5, 4, 3, 2, 1]

Sample Output 
2
"""


def minimum_swaps(arr):
    """
    Given an array of size N, find the minimum number of swaps needed to make the array sorted.

    Args:
    arr (list): The input array.

    Returns:
    int: The minimum number of swaps needed.
    """
    ans = 0
    # Get the length of the array
    n = len(arr)
    
    # Create a list of tuples where each tuple contains the element and its original index
    pair = []
    for i in range(n):
        pair.append((arr[i], i))
        
    # Sort the list of tuples based on the array values to determine the target positions
    pair.sort()
    
    # Create a visited array to keep track of whether an element has been processed
    visited = [False] * n
    
    # Iterate through each element to find cycles
    for i in range(n):
        old_position = pair[i][1]
        
        # Skip if the element is already visited or is already in the correct position
        if visited[i] or old_position == i:
            continue
        
        # Start a new cycle
        node = i
        cycle = 0
        
        # Traverse the cycle
        while not visited[node]:
            visited[node] = True  # Mark the current node as visited
            next_node = pair[node][1]  # Move to the next node in the cycle
            node = next_node
            cycle += 1  # Increment the cycle size
        
        # Add the number of swaps needed for this cycle to the answer
        ans += (cycle - 1)
    
    # Return the total number of swaps needed
    return ans
        
        
    
    


def main():
    """
    Main function to demonstrate the minimum_swaps function.
    """
    # Sample input
    a1 = [5, 4, 3, 2, 1]
    
    # Call the minimum_swaps function and print the result
    result = minimum_swaps(a1)
    print(f"Minimum swaps needed: {result}")

if __name__ == "__main__":
    main()