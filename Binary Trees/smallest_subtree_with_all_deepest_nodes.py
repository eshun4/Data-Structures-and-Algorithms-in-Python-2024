"""
865. Smallest Subtree with all the Deepest Nodes

Medium

Given the root of a binary tree, the depth of each node is the shortest distance to the root.

Return the smallest subtree such that it contains all the deepest nodes in the original tree.

A node is called the deepest if it has the largest depth possible among any node in the entire tree.

The subtree of a node is a tree consisting of that node, plus the set of all descendants of that node.

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation: We return the node with value 2, colored in yellow in the diagram.
The nodes coloured in blue are the deepest nodes of the tree.
Notice that nodes 5, 3 and 2 contain the deepest nodes in the tree but node 2 is the smallest subtree among them, so we return it.
Example 2:

Input: root = [1]
Output: [1]
Explanation: The root is the deepest node in the tree.
Example 3:

Input: root = [0,1,3,null,2]
Output: [2]
Explanation: The deepest node in the tree is 2, the valid subtrees are the subtrees of nodes 2, 1 and 0 but the subtree of node 2 is the smallest.
 

Constraints:

The number of nodes in the tree will be in the range [1, 500].
0 <= Node.val <= 500
The values of the nodes in the tree are unique.
 

Note: This question is the same as 1123: https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/
"""

from typing import Optional 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        return: the smallest subtree such that it contains all the deepest nodes in the original tree
        """
        def postorder(node, depth):
            # check if the node is empty
            if node is None:
                return (depth -1 , None)
            
            # check the left part of the tree 
            left_depth, lca_left = postorder(node.left, depth + 1)
            right_depth, lca_right = postorder(node.right, depth + 1)

            # check if the left depth is greater than the right depth
            if left_depth > right_depth:
                return (left_depth, lca_left)
            if right_depth > left_depth:
                return (right_depth, lca_right)
            if left_depth == right_depth:
                return (left_depth, node)

        _, lca_node = postorder(root, 0)
        return lca_node
        

def main():
    pass 

if __name__ == "__main__":
    main()