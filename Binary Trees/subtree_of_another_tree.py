"""
Subtree of Another Tree
Given two binary trees root and subRoot, determine if subRoot is a subtree of root. A subtree of a binary tree is a tree that consists of a node in the tree and all of its descendants. An empty tree is considered a subtree of any tree (including another empty tree).

Input:

Subtree of Another Tree

Output: true

"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_same_tree(tree1, tree2):
    # check to see if both trees are empty then return True
    if tree1 is None and tree2 is None:
        return True 
    # check if one of the trees is empty then return False
    if tree1 is None or tree2 is None:
        return False 
    # check if the values are equal and recursively check the child nodes too
    return (tree1.val == tree2.val and is_same_tree(tree1.left, tree2.left) and is_same_tree(tree1.right, tree2.right))
    
def subtree_of_another_tree(root: Node, sub_root: Node) -> bool:
    # WRITE YOUR BRILLIANT CODE HERE
    # check is subroot is None 
    if sub_root is None:
        return True
    # check if the root is None 
    if root is None:
        return False 
    
    # check the root and the child nodes
    return is_same_tree(root, sub_root) or subtree_of_another_tree(root.left, sub_root) or subtree_of_another_tree(root.right, sub_root)

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
    root = build_tree(iter(input().split()), int)
    sub_root = build_tree(iter(input().split()), int)
    res = subtree_of_another_tree(root, sub_root)
    print("true" if res else "false")
