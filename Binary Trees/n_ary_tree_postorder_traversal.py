"""
590. N-ary Tree Postorder Traversal

Easy

Given the root of an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

 

Example 1:


Input: root = [1,null,3,2,4,null,5,6]
Output: [5,6,3,2,4,1]
Example 2:


Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
0 <= Node.val <= 104
The height of the n-ary tree is less than or equal to 1000.
 

Follow up: Recursive solution is trivial, could you do it iteratively?
"""

from typing import List, Optional

# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # The iterative solution uses a stack 
        # create a stack
        # and append the root to it
        stack = [root]
        # create an output list to store the results
        results = []
        # iterate through the stack checking if it is empty
        while stack:
            # get the nodes one at a time
            node = stack.pop()
            # check if the node is empty
            if node:
                results.append(node.val)
                for child in node.children:
                    stack.append(child)
                
        # return the results
        return results[::-1]


        # # the recursive solution below 
        # # it uses O(n) time and O(h) space complexity for the recursive stack
        # # create a recursive dfs function for the traversal
        # def visit(node, output):
        #     # check if the root node is empty
        #     if not node:
        #         return output 
        #     # if node is not empty travers the children
        #     for child in node.children:
        #         visit(child, output)
        #     # lastly output the resuts in the array
        #     output.append(node.val)
        #     # return the output
        #     return output 
        
        # # create a result list to store the result of the traversal
        # result = []
        # # call the recursive dfs function
        # visit(root, result)
        # return result

def main():
    pass


if __name__ == "__main__":
    main()