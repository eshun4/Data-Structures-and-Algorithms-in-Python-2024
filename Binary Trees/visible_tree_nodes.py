"""
Visible Tree Node | Number of Visible Nodes
Prereq: DFS on Tree

In a binary tree, a node is labeled as "visible" if, on the path from the root to that node, there isn't any node with a value higher than this node's value.

The root is always "visible" since there are no other nodes between the root and itself. Given a binary tree, count the number of "visible" nodes.

Input:



Output: 3

For example: Node 4 is not visible since 5>4, similarly Node 3 is not visible since both 5>3 and 4>3. Node 8 is visible since all 5<=8, 4<=8, and 8<=8.
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def visible_tree_node(root: Node) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    # going down we need to keep track of the max_encountered so far.
    # we need to return the total of the nodes that meet the creteria up
    def dfs(node, max_so_far):
        # check if the root node is None then return 0 as the count
        if node is None:
            return 0 

        # keep track of the total number of nodes that meet criteria
        total = 0
        # next keep track of the max so far 
        if node.val >= max_so_far:
            total += 1

        # add the nodes on the left to total 
        total += dfs(node.left, max(node.val, max_so_far))
        total += dfs(node.right,max(node.val, max_so_far))

        return total 

    # call dfs and return total
    return dfs(root, float("-inf"))
        

# this function builds a tree from input; you don't have to modify it
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    if val == "x":
        return None
    node = Node(f(val))
    node.left = build_tree(nodes, f)
    node.right = build_tree(nodes, f)
    return node

if __name__ == "__main__":
    # Example: "5 4 3 x x 8 x x 6 x x"
    test_input = "5 4 3 x x 8 x x 6 x x"
    root = build_tree(iter(test_input.split()), int)
    res = visible_tree_node(root)
    print(res)
