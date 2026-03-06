"""
1644. Lowest Common Ancestor of a Binary Tree II 🔒

Description
Given the root of a binary tree, return the lowest common ancestor (LCA) of two given nodes, p and q. If either node p or q does not exist in the tree, return null. All values of the nodes in the tree are unique.

According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a binary tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)". A descendant of a node x is a node y that is on the path from node x to some leaf node.

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:



Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5. A node can be a descendant of itself according to the definition of LCA.
Example 3:



Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 10
Output: null
Explanation: Node 10 does not exist in the tree, so return null.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
 

Follow up: Can you find the LCA traversing the tree, without checking nodes existence?
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # create foundLeft and foundRight
        foundLeft, foundRight = False, False
        
        def dfs(node, left, right):
            nonlocal foundLeft, foundRight
            
            # check if node is empty 
            if node is None:
                return None 
            
            # do not return immediately
            current = None
            
            if node is left:
                foundLeft = True
                current = node 
                
            if node is right:
                foundRight = True
                current = node 
            
            # check the left side of the tree 
            left_res = dfs(node.left, left, right)
            right_res = dfs(node.right, left, right)
            
            # if one target is on the left and the other is on the right
            if left_res is not None and right_res is not None:
                return node 
            
            # if current node is one target, and the other target is below it
            if current is not None and (left_res is not None or right_res is not None):
                return node
            
            # otherwise return whichever target/LCA was found
            if current is not None:
                return current
            
            return left_res if left_res else right_res

        candidate = dfs(root, p, q)
        return candidate if foundLeft and foundRight else None

def main():
    def check(test_name, actual, expected):
        actual_val = actual.val if actual else None
        if actual_val == expected:
            print(f"{test_name}: PASSED (got {actual_val})")
        else:
            print(f"{test_name}: FAILED (got {actual_val}, expected {expected})")

    # Helper: build the example tree
    #
    #         3
    #       /   \
    #      5     1
    #     / \   / \
    #    6   2 0   8
    #       / \
    #      7   4
    #
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)

    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)

    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    sol = Solution()

    # Test 1: LCA of 5 and 1 => 3
    p = root.left
    q = root.right
    ans = sol.lowestCommonAncestor(root, p, q)
    check("Test 1", ans, 3)

    # Test 2: LCA of 5 and 4 => 5
    p = root.left
    q = root.left.right.right
    ans = sol.lowestCommonAncestor(root, p, q)
    check("Test 2", ans, 5)

    # Test 3: q does not exist in tree => None
    p = root.left
    q = TreeNode(10)
    ans = sol.lowestCommonAncestor(root, p, q)
    check("Test 3", ans, None)

    # Test 4: p does not exist in tree => None
    p = TreeNode(99)
    q = root.right
    ans = sol.lowestCommonAncestor(root, p, q)
    check("Test 4", ans, None)

    # Test 5: both do not exist => None
    p = TreeNode(100)
    q = TreeNode(200)
    ans = sol.lowestCommonAncestor(root, p, q)
    check("Test 5", ans, None)

    # Test 6: one node is ancestor of the other => 2
    p = root.left.right
    q = root.left.right.left
    ans = sol.lowestCommonAncestor(root, p, q)
    check("Test 6", ans, 2)

    # Test 7: nodes on different sides under node 2 => 2
    p = root.left.right.left
    q = root.left.right.right
    ans = sol.lowestCommonAncestor(root, p, q)
    check("Test 7", ans, 2)

    # Test 8: root is the LCA => 3
    p = root.left.left
    q = root.right.right
    ans = sol.lowestCommonAncestor(root, p, q)
    check("Test 8", ans, 3)

    # Test 9: single-node tree, missing second node => None
    single = TreeNode(42)
    p = single
    q = TreeNode(99)
    ans = sol.lowestCommonAncestor(single, p, q)
    check("Test 9", ans, None)

    # Test 10: two-node tree, valid nodes => 1
    small = TreeNode(1)
    small.left = TreeNode(2)
    p = small
    q = small.left
    ans = sol.lowestCommonAncestor(small, p, q)
    check("Test 10", ans, 1)


if __name__ == "__main__":
    main()

