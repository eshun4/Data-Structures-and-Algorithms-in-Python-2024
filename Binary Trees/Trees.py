"""
Code for a Binafry Tree Representation and basic operations on them
"""

class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 
        

# Return whether a node is a leaf 

def is_leaf(node):
    if not node:
        return False 
    return not node.left and not node.right

    
# Return the values of its children as an array of length at most 2 
def children_values(node):
    if not node:
        return []
    children_values = [] 
    if node.left:
        children_values.append(node.left.val)
    if node.right:
        children_values.append(node.right.val)
    return children_values

# return the values of its grandcildren as an array of length of at most 4 
def grandchildren_values(node):
    if not node:
        return []
    grandchildren = [] 
    for child in [node.left, node.right]:
        if child and child.left:
            grandchildren.append(child.left.val)
        if child and child.right:
            grandchildren.append(child.right.val)
    return grandchildren

# Return the size of the node's subtree. A node's subtree includes itslef and all of its descendants.
def tree_size(node):
    if not node:
        return 0 
    # get the left size 
    left_tree_size = tree_size(node.left)
    # get the right size 
    right_tree_size = tree_size(node.right)
    # finally combine them includeing the start node itself as 1
    return left_tree_size + right_tree_size + 1 

# Return the height of its subtree
def tree_height(node):
    # if the root node is empty return 0
    if not node:
        return 0 
    # get the height of the left tree
    left_height = tree_height(node.left)
    # get the height of the right tree 
    right_height = tree_height(node.right)
    # return the height of the maximumof the 2 since the one with the largest is the vale. Add 1 to include the root node itself
    return max(left_height, right_height) + 1

def main():
    def check(label, got, expected):
        status = "PASS" if got == expected else "FAIL"
        print(f"{status} | {label}: got={got}, expected={expected}")

    # -----------------------
    # Test 0: empty tree
    # -----------------------
    root0 = None
    check("is_leaf(None)", is_leaf(root0), False)
    check("children_values(None)", children_values(root0), [])
    check("grandchildren_values(None)", grandchildren_values(root0), [])
    check("tree_size(None)", tree_size(root0), 0)
    check("tree_height(None)", tree_height(root0), 0)

    # -----------------------
    # Test 1: single node
    # -----------------------
    root1 = Tree(10)
    check("is_leaf(single)", is_leaf(root1), True)
    check("children_values(single)", children_values(root1), [])
    check("grandchildren_values(single)", grandchildren_values(root1), [])
    check("tree_size(single)", tree_size(root1), 1)      # will PASS even with bug
    check("tree_height(single)", tree_height(root1), 1)

    # -----------------------
    # Test 2: root with one left child
    #    1
    #   /
    #  2
    # -----------------------
    root2 = Tree(1, Tree(2), None)
    check("is_leaf(root with left)", is_leaf(root2), False)
    check("children_values(root with left)", children_values(root2), [2])
    check("grandchildren_values(root with left)", grandchildren_values(root2), [])
    check("tree_size(root with left)", tree_size(root2), 2)   # should be 2 (bug still likely PASS here)
    check("tree_height(root with left)", tree_height(root2), 2)

    # -----------------------
    # Test 3: root with one right child
    #  1
    #   \
    #    3
    # -----------------------
    root3 = Tree(1, None, Tree(3))
    check("children_values(root with right)", children_values(root3), [3])
    check("tree_size(root with right)", tree_size(root3), 2)   # BUG will make this FAIL (likely gives 3)
    check("tree_height(root with right)", tree_height(root3), 2)

    # -----------------------
    # Test 4: perfect tree of height 3 (7 nodes)
    #        1
    #      /   \
    #     2     3
    #    / \   / \
    #   4  5  6  7
    # -----------------------
    root4 = Tree(
        1,
        Tree(2, Tree(4), Tree(5)),
        Tree(3, Tree(6), Tree(7))
    )
    check("is_leaf(root perfect)", is_leaf(root4), False)
    check("children_values(root perfect)", children_values(root4), [2, 3])
    check("grandchildren_values(root perfect)", grandchildren_values(root4), [4, 5, 6, 7])
    check("tree_height(root perfect)", tree_height(root4), 3)
    check("tree_size(root perfect)", tree_size(root4), 7)      # BUG will make this FAIL

    # -----------------------
    # Test 5: unbalanced chain (height 4, size 4)
    #    9
    #   /
    #  8
    # /
    #7
    #/
    #6
    # -----------------------
    root5 = Tree(9, Tree(8, Tree(7, Tree(6))), None)
    check("tree_height(chain left)", tree_height(root5), 4)
    check("tree_size(chain left)", tree_size(root5), 4)        # likely PASS despite bug (right sizes are 0)

    print("\nDone.")


if __name__ =="__main__":
    main()
        