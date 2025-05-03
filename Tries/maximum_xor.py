"""
Biggest Xor of Two Numbers in an Array
------------------------------------------------

Given an array, find the maximum XOR that you can form by picking two numbers from the array!

Input = [3, 10, 5, 8, 2, 25]

Output: 28
------------------------------------------------

Explanation:
The maximum XOR can be formed by picking 5 and 25 = 28.

"""

class Node:
    def __init__(self, left, right):
        self.left = left # 0
        self.right = right # 1
        
class Trie:
    def __init__(self):
        self.root = Node(None, None) # Initialize the root of the Trie

    def insert(self, n):
        temp = self.root
        # Insert bits of the number into the Trie
        for i in range(31, -1, -1):
            bit = (n >> i) & 1
            if bit == 0:
                if temp.left is None:
                    temp.left = Node(None, None)
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = Node(None, None)
                temp = temp.right
        # Mark the end of the number in the Trie
        temp.value = n
        
    
    def max_xor_helper(self, value):
        current_ans = 0
        temp = self.root
        # Traverse the Trie to find the maximum XOR value
        for j in range(31, -1, -1):
            bit = (value >> j) & 1
            # Check if the opposite bit exists in the Trie
            if bit == 0:
                # find the opposite value
                if temp.right is not None:
                    current_ans += (1 << j)
                    temp = temp.right
                else:
                    temp = temp.left
            else:
                if temp.left is not None:
                    current_ans += (1 << j)
                    temp = temp.left
                else:
                    temp = temp.right
                    
        return current_ans # Return the maximum XOR value found
        
    
    def max_xor(self, arr, n):
        max_xor = 0
        # Insert all numbers into the Trie
        for i in range(n):
            self.insert(arr[i])
            current_xor = self.max_xor_helper(arr[i])
            # Update the maximum XOR value
            max_xor = max(max_xor, current_xor)
        return max_xor # Return the maximum XOR value
    

    
    
        


def main():
    # Example usage
    arr = [3, 10, 5, 8, 2, 25]
    n = len(arr)
    
    # Create a Trie object
    trie = Trie()
    
    # Find the maximum XOR value in the array
    result = trie.max_xor(arr, n)
    
    # Print the result
    print("The maximum XOR of two numbers in the array is:", result)

if __name__ == '__main__':
    main()