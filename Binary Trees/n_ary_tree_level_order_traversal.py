"""
429. N-ary Tree Level Order Traversal

Medium

Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

 

Example 1:



Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]
Example 2:



Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
 

Constraints:

The height of the n-ary tree is less than or equal to 1000
The total number of nodes is between [0, 104]
"""

from typing import List, Optional
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

from collections import deque

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # check if the root is None
        if root is None:
            return []
        # create a queue to store the root of the tree
        queue = deque([root])
        # result array for resukts 
        results = []
        # iterate through the queue while it has a value
        while queue:
            # we need the size of each level in order to perform a BFS
            level_size = len(queue)
            # keep second stack to keep track of the nodes
            stack_1 = []
            # iterate through each level of nodes
            for _ in range(level_size):
                # pop the nodes
                node = queue.popleft()
                # append the nodes value to the stack
                stack_1.append(node.val)
                # iterate through the children of the node
                for child in node.children:
                    queue.append(child)
            results.append(stack_1)
        # lastly return the results
        return results
                
        

def main():
    pass 

if __name__ == "__main__":
    main()