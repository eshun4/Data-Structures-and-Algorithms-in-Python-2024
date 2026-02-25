# Your previous Plain Text content is preserved below:

# Hello! Your interview question is below. Write code in this pad just like you would normally – your AI Interviewer will be able to see it.

# # Tree Layout

# You are given the root of a non-empty binary tree. We lay out the tree on a grid as follows:

# 1. We put the root at `(r, c) = (0, 0)`
# 2. We recursively lay out the left subtree one unit below the root (increasing `r` by one)
# 3. We recursively lay out the right subtree one unit to the root's right (increasing `c` by one)

# For instance, the left child of the root goes on `(1, 0)` and the right child goes on `(0, 1)`.

# Two nodes are _stacked_ if they are laid on the same `(r, c)` coordinates. For instance, `root.left.right` and `root.right.left` would overlap at `(1, 1)`.

# Return the maximum number of nodes stacked on the same coordinate.

# Example:

# Input:
#          1
#        /   \
#      2       3
#    /  \     /
#   4    5   6
#    \      / \
#     7    8   9

# Output: 2
# The layout looks like this:

# 1 -- 3
# |    |
# 2 - 5,6 - 9
# |    |
# 4 - 7,8

# The most stacked nodes are 5,6 or 7,8.

# https://iio-beyond-ctci-images.s3.us-east-1.amazonaws.com/trees_fig11.png

# Constraints:

# - The number of nodes is at most `10^5`
# - The height of the tree is at most `500`
# - The value at each node doesn't matter.
class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def most_stacked(node):
    # counting hashmap
    counter = {}

    def visit(node, r, c):
        # check if any of the nodes includeing the root to the children is empty 
        if not node:
            return 
        # if the row and the column is not in counter then set it to 0 else increase by w 
        if (r, c) not in counter:
            counter[(r,c)] = 0 
        counter[(r,c)] += 1

        # recursively place left and right node 
        visit(node.left, r + 1, c)
        visit(node.right,r, c + 1)
    
    visit(node, 0, 0)

    # return maximum of the values in hashmap
    return max(counter.values())

def run_tests():
    # Test 1: Example from the book - two nodes stacked
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.left.right = Node(5)
    root1.left.left.right = Node(7)
    root1.right.left = Node(6)
    root1.right.left.left = Node(8)
    root1.right.left.right = Node(9)

    root2 = Node(1)

    root3 = Node(1,
                Node(2),
                Node(3))

    # Test 4: Perfect binary tree of depth 4
    root4 = Node(1,
                Node(2,
                        Node(4,
                            Node(8),
                            Node(9, None, Node(16))),
                        Node(5,
                            Node(10, None, Node(17)),
                            Node(11, Node(18), None))),
                Node(3,
                        Node(6,
                            Node(12),
                            Node(13)),
                        Node(7,
                            Node(14, Node(19), None),
                            Node(15, Node(20), None))))

    tests = [
        (root1, 2),  # Example from book
        (root2, 1),  # Single node
        (root3, 1),
        (root4, 4),
    ]

    for i, (root, want) in enumerate(tests, 1):
        got = most_stacked(root)
        print(got == want, f"\nmost_stacked(): got: {got}, want: {want}\n")

run_tests()
        
        


