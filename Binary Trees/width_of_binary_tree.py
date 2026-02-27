"""
662. Maximum Width of Binary Tree

Medium

Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

It is guaranteed that the answer will in the range of a 32-bit signed integer.

 

Example 1:


Input: root = [1,3,2,5,3,null,9]
Output: 4
Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).
Example 2:


Input: root = [1,3,2,5,null,null,9,6,null,7]
Output: 7
Explanation: The maximum width exists in the fourth level with length 7 (6,null,null,null,null,null,7).
Example 3:


Input: root = [1,3,2,5]
Output: 2
Explanation: The maximum width exists in the second level with length 2 (3,2).
 

Constraints:

The number of nodes in the tree is in the range [1, 3000].
-100 <= Node.val <= 100
"""
from collections import Optional 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # basically the width is the length of the distance of the last index
        # and the leftmlost index plus 1 
        # create a queue which stores the root node and the index of that root
        queue = deque([(root, 0)])
        # keep track of max width
        max_width = 0
        # if root is None
        if root is None:
            return 0
        # keep track of left index and right indes
        left_index, right_index = 0, 0
        # iterte through the queue to get the nodes level by level
        while queue:
            # get the size of the each level
            level_size = len(queue)
            # base index from the root node
            base = queue[0][1]
            # get the width based on the last and first nodes at that level
            width = queue[-1][1] - queue[0][1] + 1
            # iterate through the levels in each node
            for _ in range(level_size):
                node, index = queue.popleft()
                # normalize the index 
                norm = index - base
                # check if the node is the left node
                if node.left:
                    left_index = (2 * norm) + 1
                    queue.append((node.left, left_index))
                if node.right:
                    right_index = (2 * norm) + 2
                    queue.append((node.right, right_index))
                max_width = max(max_width, width)
        return max_width


        

def main():
    pass 

if __name__ == "__main__":
    main()