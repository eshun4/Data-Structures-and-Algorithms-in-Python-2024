"""
651 · Binary Tree Vertical Order Traversal

Medium

46%

Description
Solution43
Notes
Discuss99+
Leaderboard
Record

Description
Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

LintCode - Online Judge Solution

Candidate Written Test Screening, Team Competency Assessment, Programming Teaching Exercises, Online Exam Grading

WeChat for information


Example
Example1

Inpurt:  {3,9,20,#,#,15,7}
Output: [[9],[3,15],[20],[7]]
Explanation:
   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7
Example2

Input: {3,9,8,4,0,1,7}
Output: [[4],[9],[3,0,1],[8],[7]]
Explanation:
     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
"""
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def verticalOrder(root):
    """
    Args:
        root: TreeNode - root of the binary tree
    
    Returns:
        List[List[int]] - vertical order traversal
    """
    # TODO: Implement vertical order traversal
    # Hint: Use a queue with (node, column) information
    # Track the column range and group nodes by column
    # check if node is not null 
    if not root:
        return []
    # hashmap for the columns to node mappins 
    counter = {}
    # create a queue
    queue = deque([(root, 0)])
    # iterate through the queue
    while queue:
        node, column = queue.popleft()
        # if node is not empty
        if column not in counter:
            counter[column] = []
        counter[column].append(node.val)
        
        if node.left:
            queue.append((node.left, column - 1))
            
        # if node right is not empty
        if node.right:
            queue.append((node.right, column + 1))
            
    return [counter[c] for c in sorted(counter.keys())]
                
def main():
    # Test case 1: Example from description
    #    3
    #   /\
    #  9  20
    #    /\
    #   15  7
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    print("Test 1:", verticalOrder(root1))  # Expected: [[9], [3, 15], [20], [7]]

    # Test case 2: Example from description
    #       3
    #      /\
    #     9  8
    #    /\ /\
    #   4 0 1 7
    root2 = TreeNode(3)
    root2.left = TreeNode(9)
    root2.right = TreeNode(8)
    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(0)
    root2.right.left = TreeNode(1)
    root2.right.right = TreeNode(7)
    print("Test 2:", verticalOrder(root2))  # Expected: [[4], [9], [3, 0, 1], [8], [7]]

    # Test case 3: Single node
    root3 = TreeNode(1)
    print("Test 3:", verticalOrder(root3))  # Expected: [[1]]

    # Test case 4: Empty tree
    root4 = None
    print("Test 4:", verticalOrder(root4))  # Expected: []

if __name__ == "__main__":
    main()
            
            
    
    
        
    