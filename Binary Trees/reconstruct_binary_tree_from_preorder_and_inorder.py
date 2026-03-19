"""
Reconstruct Binary Tree from Preorder and Inorder Traversal
Given two arrays representing the preorder and inorder traversals of the same binary tree with unique values, reconstruct the original tree.

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7].

Output: The binary tree structure:

Construct Binary Tree from Preorder and Inorder Traversal
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def construct_binary_tree(preorder: list[int], inorder: list[int]) -> Node:
    # hashmap for inorder positions
    positions_map = {value: index for index, value in enumerate(inorder)}
    # WRITE YOUR BRILLIANT CODE HERE
    def build(pre_start, pre_end, in_start, in_end):
        # check if preorder is empty and return None
        if pre_start > pre_end or in_start > in_end:
            return None 
        # next get root from pre order
        root_value = preorder[pre_start]
        # get the root index from preorder
        root_index = positions_map[root_value]
        root = Node(root_value)
        # if root is None
        if root is None:
            return None
        # # split the inorder array
        
        # right_inorder = inorder_part[root_index + 1:]
    
        # count left size
        left_size = root_index - in_start
        # split preorder
        # left_preorder = preorder_part[1: 1 + left_size]
        # right_preorder = preorder_part[1 + left_size: ]
    
        # build the left subtree and right subtree
        root.left = build(pre_start + 1, pre_start + left_size, in_start, root_index - 1)
        root.right = build(pre_start + left_size + 1, pre_end, root_index + 1, in_end)
    
        return root

    return build(0, len(preorder) - 1, 0, len(inorder) - 1)

def format_tree(node):
    if node is None:
        yield "x"
        return
    yield str(node.val)
    yield from format_tree(node.left)
    yield from format_tree(node.right)

if __name__ == "__main__":
    preorder = [int(x) for x in input().split()]
    inorder = [int(x) for x in input().split()]
    res = construct_binary_tree(preorder, inorder)
    print(" ".join(format_tree(res)))
