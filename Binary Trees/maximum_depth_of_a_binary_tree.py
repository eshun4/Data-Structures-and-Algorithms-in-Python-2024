"""
104. Maximum Depth of Binary Tree

Easy

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100

"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
       
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        3
    9       20
         15      7

    At each node we have to check the length of the longest chain of nodes downward form that sepecific node.
    at.
    Traversal:
    at 3: check left and right
           - left = 1 node exists so return 1 as lenght
           -  right = node 20 and it checks the left and right 
               - left 20 returns 1 and right 20 return 1 too 
            - so at node 20 we have the maximum of the left and right plus the current node which is of length 1.
            = 1 + max(left, right) = 1 + max(1, 1) = 2
           - node 20 returns: 2 
           - node 8 returns 1 since there is only 1 node there 
           - then it goes back to the root node of 3 and returns:
                1 + max(1, 2) = 3
        output returns 3 

        Now what if the root node is empty?
        Then return None.
        Time complexty of the traversal DFS is: O()
        """
        if not root:
            return 0
        # check the left subtree
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        # return the length of the longest chain of nodes from the root node given'
        return 1 + max(left, right)
    
    
def main():
    pass 

if __name__ == "__main__":
    main()
        
    
        


        