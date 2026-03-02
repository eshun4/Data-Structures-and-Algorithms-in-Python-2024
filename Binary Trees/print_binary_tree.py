"""
655. Print Binary Tree

Medium

Given the root of a binary tree, construct a 0-indexed m x n string matrix res that represents a formatted layout of the tree. The formatted layout matrix should be constructed using the following rules:

The height of the tree is height and the number of rows m should be equal to height + 1.
The number of columns n should be equal to 2height+1 - 1.
Place the root node in the middle of the top row (more formally, at location res[0][(n-1)/2]).
For each node that has been placed in the matrix at position res[r][c], place its left child at res[r+1][c-2height-r-1] and its right child at res[r+1][c+2height-r-1].
Continue this process until all the nodes in the tree have been placed.
Any empty cells should contain the empty string "".
Return the constructed matrix res.

 

Example 1:


Input: root = [1,2]
Output: 
[["","1",""],
 ["2","",""]]
Example 2:


Input: root = [1,2,3,null,4]
Output: 
[["","","","1","","",""],
 ["","2","","","","3",""],
 ["","","4","","","",""]]
 

Constraints:

The number of nodes in the tree is in the range [1, 210].
-99 <= Node.val <= 99
The depth of the tree will be in the range [1, 10].
"""


from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        
        def depth(node):
            if node is None:
                return -1
            left_depth = depth(node.left)
            right_depth = depth(node.right)

            return max(left_depth, right_depth) + 1

        height = depth(root)
        col = (2 ** (height + 1)) - 1
        row = height + 1

        res = [["" for _ in range(col)] for _ in range(row)]
        
        # place nodes next 
        def place_nodes(node, r, c, height):
            nonlocal res
            # if node is null
            if node is None:
                return 
            offset = 2 ** (height - r - 1)
            # set node value
            res[r][c] = f"{node.val}"
            # if the left node exists
            if node.left:
                place_nodes(node.left, r + 1, c - offset, height)
            if node.right:
                place_nodes(node.right, r + 1, c + offset, height)

        start_col = (col - 1) // 2
        place_nodes(root, 0, start_col, height)
        return res



        
        

def main():
    pass 

if __name__ == "__main__":
    main()