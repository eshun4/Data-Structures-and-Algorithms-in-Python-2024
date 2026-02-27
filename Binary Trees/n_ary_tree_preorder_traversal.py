"""
589. N-ary Tree Preorder Traversal

Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

 

Example 1:



Input: root = [1,null,3,2,4,null,5,6]
Output: [1,3,5,6,2,4]
Example 2:



Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]
 

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
    def preorder(self, root: 'Node') -> List[int]:
        # output result
        output = []
        # stack for iteratice solution
        stack = [root]

        # iterate through stack for noded
        while stack:
            node = stack.pop()
            # check if node is not None
            if node:
                output.append(node.val)
                for child in reversed(node.children):
                    stack.append(child)
        return output


        # below is the recursive solution
        
        # # create a recursive function
        # def visit(node, output):
        #     # check if the node is null
        #     if not node:
        #         return output
            
        #     # append the node if its not null
        #     output.append(node.val)
        #     # iterate through the children to append values
        #     for child in node.children:
        #         if child:
        #             visit(child, output)
        #     return output
        # result = []
        # visit(root, result)
        # return result


def main():
    pass 


if __name__ == "__main__":
    main()