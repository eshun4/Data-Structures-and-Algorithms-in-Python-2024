""" 
Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

Example 1:

Input:

   1
    \
     3
    / \
   2   4
        \
         5

Output: 3

Explanation: Longest consecutive sequence path is 3-4-5, so return 3.
Example 2:

Input:

   2
    \
     3
    / 
   2    
  / 
 1

Output: 2 

Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.
"""

class Node:
    def __init__(self, val, left=None, right= None):
        self.val = val 
        self.left = left 
        self.right = right 
        
    def longestConsecutiveSequence(root) -> int:
        """
         1
        
            3     = only 1 right child = returns 1 + max(1, 2) = 3

        2       4   = 2 children, left and right left child id not consecutive so 0, right include since it is 3 + 1 = 4 = 1 + max(0, 1 ) = 2
                 
                  5  = 1 child, right child 5 is equal to 4 + 1 so it returns 1
                  
     hence output returns 3
        """
        
        # track the global best as res
        res = 1
        
        # create a visit dfs function that keeps track of the parent val too 
        def visit(node):
            # set result to nonlocal
            nonlocal res 
            # check if node is empty
            if node is None:
                return 0 
            # traverse left and right 
            left_chain = visit(node.left)
            right_chain = visit(node.right)
            
            # track the current sequence
            sequence = 1
            
             # only extend through left child if it is consecutive
            if node.left and node.left.val == node.val + 1:
                sequence = max(sequence, 1 + left_chain)
            
            # only extend through right child if it is consecutive
            if node.right and node.right.val == node.val + 1:
                sequence = max(sequence, 1 + right_chain)
            
            # update global best
            res = max(res, sequence)
            return sequence
       
        visit(root)
        return res
            
def run_tests():
    # Test 1: empty tree
    print(Node.longestConsecutiveSequence(None) == 0)

    # Test 2: single node
    root = Node(7)
    print(Node.longestConsecutiveSequence(root) == 1)

    # Test 3: straight consecutive chain
    # 1 -> 2 -> 3
    root = Node(1, None, Node(2, None, Node(3)))
    print(Node.longestConsecutiveSequence(root) == 3)

    # Test 4: break then new chain starts lower
    # 10 -> 3 -> 4 -> 5  => best is 3 (3->4->5)
    root = Node(10, None, Node(3, None, Node(4, None, Node(5))))
    print(Node.longestConsecutiveSequence(root) == 3)

    # Test 5: no consecutive edges
    #     5
    #    / \
    #   9   2
    root = Node(5, Node(9), Node(2))
    print(Node.longestConsecutiveSequence(root) == 1)

    # Test 6: choose better side
    #       3
    #      / \
    #     4   4
    #    /     \
    #   5       5
    # best = 3
    root = Node(3,
                Node(4, Node(5), None),
                Node(4, None, Node(5)))
    print(Node.longestConsecutiveSequence(root) == 3)

    print("All tests passed!")


# Uncomment to run tests
# run_tests()
            
    
def main():
    run_tests()
    
if __name__ == "__main__":
    main()