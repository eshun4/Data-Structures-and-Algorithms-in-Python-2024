"""
687. Longest Univalue Path

Medium

Given the root of a binary tree, return the length of the longest path, where each node in the path has the same value. This path may or may not pass through the root.

The length of the path between two nodes is represented by the number of edges between them.

 

Example 1:


Input: root = [5,4,5,1,1,null,5]
Output: 2
Explanation: The shown image shows that the longest path of the same value (i.e. 5).
Example 2:


Input: root = [1,4,5,4,4,null,5]
Output: 2
Explanation: The shown image shows that the longest path of the same value (i.e. 4).
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-1000 <= Node.val <= 1000
The depth of the tree will not exceed 1000.
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        """
        The length of path represents number of edges between them. 
              5
        4           5 
    
    1        1         5
        """

        # create a best path varuiable as res
        res = 0 
        # next create the dfs function to travers the tree starting from the root
        def visit(node):
            # declaring it a non-local variable
            nonlocal res
            # if node is empty return 0 
            if node is None:
                return 0 
            # we keep track of the sequence that we have so far
            sequence = 0 
            # now traverse left
            left = visit(node.left)
            # traverse right 
            right = visit(node.right)
            # create a value to extend left and right
            extend_left, extend_right= 0, 0
            # we went to check if the current node value is the same as its left and right child 
            if node.left and node.left.val == node.val:
                extend_left = left + 1
            if node.right and node.right.val == node.val:
                extend_right =  right + 1
            # update the sequence
            sequence = max(extend_left, extend_right)
            # update the global best valuesas res
            res = max(res, extend_left + extend_right)
            return sequence

        # call the visit function
        visit(root)
        # lastly return the results
        return res
         
def main():
    pass 
            
if __name__ == "__main__":
    main()