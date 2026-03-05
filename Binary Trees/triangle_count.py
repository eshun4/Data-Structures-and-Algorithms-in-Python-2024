"""
Problem 35.5 - Triangle Count
Get asked this question by our AI Interviewer
Interview now
Given the root of a binary tree, return the number of triangles. A triangle is a set of three distinct nodes, a, b, and c, where:

a is the lowest common ancestor of b and c.
b and c have the same depth.
the path from a to b only consists of left children (the nodes in the path can have right children).
the path from a to c only consists of right children (the nodes in the path can have left children).

Example 1:
         0
     /       \
    1         2
     \       / \
      3     4   5
     / \   /     \
    6   7 8       9

Output: 4.
The triangles are: (0, 1, 2), (3, 6, 7), (2, 4, 5), (2, 8, 9).
Triangle count 1

Example 2:
      0
   /      \
  1        4
 /  \       \
2    3       5
Output: 3.
The triangles are: (0, 1, 4), (1, 2, 3), (0, 2, 5).
Constraints:

The number of nodes is at most 10^5
The height of the tree is at most 500
The value at each node doesn't matter.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def triangle_count(root):
    # triangles_count 
    triangles_count = 0
    def visit(node):
        # declare triangle count in visit function
        nonlocal triangles_count
        # if the root is None
        if node is None:
            return (0, 0)
        
        # get the left and right chains
        left = visit(node.left)
        right = visit(node.right)
        
        # get lleft from left and rright from right
        L_left, _ = left
        _, Rright = right
        
        # get L and R
        L = 0 if node.left is None else 1 + L_left 
        R = 0 if node.right is None else 1 + Rright 
        
        # get thetriangles count
        triangles_count += min(L, R)
        
        # retrun L and R
        return (L, R)
    
    visit(root)
    
    return triangles_count
        

def main():
    # Example 1
    root1 = TreeNode(0)
    root1.left = TreeNode(1)
    root1.right = TreeNode(2)
    root1.left.right = TreeNode(3)
    root1.right.left = TreeNode(4)
    root1.right.right = TreeNode(5)
    root1.left.right.left = TreeNode(6)
    root1.left.right.right = TreeNode(7)
    root1.right.left.left = TreeNode(8)
    root1.right.right.right = TreeNode(9)
    
    print("Example 1 - Expected: 4")
    print(f"Result: {triangle_count(root1)}\n")
    
    # Example 2
    root2 = TreeNode(0)
    root2.left = TreeNode(1)
    root2.right = TreeNode(4)
    root2.left.left = TreeNode(2)
    root2.left.right = TreeNode(3)
    root2.right.right = TreeNode(5)
    
    print("Example 2 - Expected: 3")
    print(f"Result: {triangle_count(root2)}\n")

if __name__ == "__main__":
    main()