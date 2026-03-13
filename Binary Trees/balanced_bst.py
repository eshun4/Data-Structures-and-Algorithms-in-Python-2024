"""
Balanced Binary Tree
Prereq: DFS Fundamentals

A binary tree is considered balanced if, for every node in the tree, the difference in the height (or depth) of its left and right subtrees is at most 1.

In other words, the depth of the two subtrees for every node in the tree differs by no more than one.

The height (or depth) of a tree is defined as the number of edges on the longest path from the root node to any leaf node.

Note: An empty tree is considered balanced by definition.

In that case, given a binary tree, determine if it is balanced.

Parameter
tree: A binary tree.
Result
A boolean representing whether the tree given is balanced.
Examples
Example 1
Input:



Output: true

Explanation: By definition, this is a balanced binary tree.

Example 2
Input:



Output: false

Explanation: The subtrees of the node labelled 3 has a height difference of 2 (right subtree has height 2 and left subtree is empty with height 0), so it is not balanced.
"""



class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(tree: Node) -> bool:
    # WRITE YOUR BRILLIANT CODE HERE
    # going down we dont keep track of any state
    # going up we return an in value to the parent node in the traversal
    def dfs(node):
        # if the node is None then return True
        if node is None:
            return (True, -1)
        # check if left is balanced and height
        left_ok, left_h = dfs(node.left)
        # check if right is balanced and right height 
        right_ok, right_h = dfs(node.right)
        # check if its balanced and the difference in left and right is just 1 
        balanced = left_ok and right_ok and abs(left_h - right_h) <= 1
        return (balanced, max(left_h, right_h) + 1)

    # call dfs function
    return dfs(tree)[0]

# this function builds a tree from input; you don't have to modify it
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    if val == "x":
        return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == "__main__":
    tree = build_tree(iter(input().split()), int)
    res = is_balanced(tree)
    print("true" if res else "false")

