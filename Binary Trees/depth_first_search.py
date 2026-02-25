"""
DFS: Pre-order, In-order, Post-order
"""

class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 
        
class Node:
      def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def preorder(node):
    if not node:
        return 
    print(node.val)
    preorder(node.left)
    preorder(node.right)
    
def inorder(node):
    if not node:
        return 
    inorder(node.left)
    print(node.val)
    inorder(node.right)
    
def postorder(node):
    if not node:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.val)
    
def longest_aligned_chain(node):
    """
    Given a binary tree, we say a node is aligned if its value is the same as its depth. Return the length of the 
    longest descendant chain of aligned nodes. The chain does not need to start at the root .
    
    Example:       7
                  / \
                 1   3
                / \   /
               2   8  2 
              / \     /\
             4   3   3  3
             
    Output: 3. The longest chain of aligned nodes is 1 -> 2 -> 3.
    :param node: A root node 
    """
    # create a res ult variable to store the results of the traversal
    res = 0 
    # we need a helper function for the dfs traversal of our Tree
    def visit(node, depth):
        # set the res value to a nonlocal value 
        nonlocal res
        # check if the node is null and return 0
        if not node:
            return 0 
        # traverse left chain keeping track of the depth 
        left_chain = visit(node.left, depth + 1)
        # traverse right chain keeping track of the depth
        right_chain = visit(node.right, depth + 1)
        # keep gtrack of the current chain
        current_chain = 0 
        if node.val == depth:
            current_chain = 1 + max(left_chain, right_chain)
            res = max(res, current_chain)
        return current_chain
    
    visit(node, 0)
    return res

def aligned_path(node):
    # create a variable called res to keep track of the results
    res = 0 
    # create a dfs visit function that keeps track fo the depth of traversal as it traverse the tree 
    def visit(node, depth):
        # set res to be accessible within the function
        nonlocal res
        # check if the current node is not None
        if not node:
            return 0 
        left_chain = visit(node.left, depth + 1)
        right_chain = visit(node.right, depth + 1)
        # create a current streak tracker
        current_streak = 0 
        # check if the current node value is equal to the depth 
        if node.val == depth:
            current_streak = max(left_chain, right_chain) + 1
            res = max(res, left_chain + right_chain + 1)
        
        # return the current streak
        return current_streak

    visit(node, 0)
    return res

class MsgNode:
    def __init__(self, text, left=None, right=None):
        self.text = text      # like "bH", "iE", "a!"
        self.left = left
        self.right = right

def hidden_message(node):
    message = []

    def visit(node):
        if not node:
            return

        order = node.text[0]   # 'b', 'a', or 'i'
        ch = node.text[1]      # character to append

        if order == 'b':       # preorder
            message.append(ch)
            visit(node.left)
            visit(node.right)

        elif order == 'a':     # postorder
            visit(node.left)
            visit(node.right)
            message.append(ch)

        elif order == 'i':     # inorder
            visit(node.left)
            message.append(ch)
            visit(node.right)

        else:
            raise ValueError(f"Unknown order prefix: {order}")

    visit(node)
    return "".join(message)


def run_hidden_message_tests():
    # ---------- Test 1: Empty tree ----------
    root = None
    assert hidden_message(root) == ""
    print("Test 1 passed")

    # ---------- Test 2: Single node, each mode ----------
    assert hidden_message(MsgNode("bH")) == "H"  # preorder
    assert hidden_message(MsgNode("aH")) == "H"  # postorder
    assert hidden_message(MsgNode("iH")) == "H"  # inorder
    print("Test 2 passed")

    # ---------- Test 3: Pure preorder over 3 nodes ----------
    #        bA
    #       /  \
    #     bB   bC
    # Preorder output: A B C
    root = MsgNode("bA", MsgNode("bB"), MsgNode("bC"))
    assert hidden_message(root) == "ABC"
    print("Test 3 passed")

    # ---------- Test 4: Pure inorder over 3 nodes ----------
    #        iA
    #       /  \
    #     iB   iC
    # Inorder output: B A C
    root = MsgNode("iA", MsgNode("iB"), MsgNode("iC"))
    assert hidden_message(root) == "BAC"
    print("Test 4 passed")

    # ---------- Test 5: Pure postorder over 3 nodes ----------
    #        aA
    #       /  \
    #     aB   aC
    # Postorder output: B C A
    root = MsgNode("aA", MsgNode("aB"), MsgNode("aC"))
    assert hidden_message(root) == "BCA"
    print("Test 5 passed")

    # ---------- Test 6: Mixed modes (each node chooses its own) ----------
    #          iX
    #         /  \
    #       bA    aB
    #
    # Visit iX: left subtree, then 'X', then right subtree
    # left bA: append 'A'
    # right aB: append 'B'
    # Result: A X B
    root = MsgNode("iX", MsgNode("bA"), MsgNode("aB"))
    assert hidden_message(root) == "AXB"
    print("Test 6 passed")

    # ---------- Test 7: Mixed + deeper structure ----------
    #              bH
    #             /  \
    #           iE    aY
    #          / \    / \
    #        bL  aL  b!  i?
    #
    # Let's compute expected carefully:
    # bH: append 'H'
    #   iE: visit left (bL => 'L'), append 'E', visit right (aL => 'L')
    #   aY: visit left (b! => '!'), visit right (i? => '?'), append 'Y'
    # => "H" + "LEL" + "!?" + "Y" = "HLEL!?Y"
    root = MsgNode("bH",
                   MsgNode("iE", MsgNode("bL"), MsgNode("aL")),
                   MsgNode("aY", MsgNode("b!"), MsgNode("i?")))
    assert hidden_message(root) == "HLEL!?Y"
    print("Test 7 passed")

    # ---------- Test 8: One-sided chain ----------
    # bA -> iB -> aC -> bD  (all left children)
    # Evaluate:
    # bA: 'A'
    #   iB: left subtree then 'B'
    #     aC: left subtree then 'C'
    #       bD: 'D'
    #
    # Order: A D C B  (because iB appends after left; aC appends after left; bD immediate)
    root = MsgNode("bA",
                   MsgNode("iB",
                           MsgNode("aC",
                                   MsgNode("bD"))))
    assert hidden_message(root) == "ADCB"
    print("Test 8 passed")

    # ---------- Test 9: Invalid prefix should raise ----------
    try:
        hidden_message(MsgNode("xZ"))
        assert False, "Expected ValueError for invalid prefix"
    except ValueError:
        pass
    print("Test 9 passed")

    print("All hidden_message tests passed ✅")


def main():
    print("=== Test 1: Example tree (expected longest aligned chain = 3) ===")
    # Build the example tree:
    #
    #        7
    #       / \
    #      1   3
    #     / \  /
    #    2  8 2
    #   / \   /\
    #  4  3  3  3
    #
    root1 = Tree(7,
                 Tree(1,
                      Tree(2,
                           Tree(4),
                           Tree(3)),
                      Tree(8)),
                 Tree(3,
                      Tree(2,
                           Tree(3),
                           Tree(3)),
                      None))

    print("Preorder:")
    preorder(root1)
    print("Inorder:")
    inorder(root1)
    print("Postorder:")
    postorder(root1)

    ans1 = longest_aligned_chain(root1)
    print("Longest aligned chain:", ans1)
    assert ans1 == 3, f"Expected 3, got {ans1}"
    print()

    print("=== Test 2: Empty tree (expected 0) ===")
    root2 = None
    ans2 = longest_aligned_chain(root2)
    print("Longest aligned chain:", ans2)
    assert ans2 == 0, f"Expected 0, got {ans2}"
    print()

    print("=== Test 3: Single node aligned at depth 0 (val=0) (expected 1) ===")
    root3 = Tree(0)
    ans3 = longest_aligned_chain(root3)
    print("Longest aligned chain:", ans3)
    assert ans3 == 1, f"Expected 1, got {ans3}"
    print()

    print("=== Test 4: Single node NOT aligned at depth 0 (val=5) (expected 0) ===")
    root4 = Tree(5)
    ans4 = longest_aligned_chain(root4)
    print("Longest aligned chain:", ans4)
    assert ans4 == 0, f"Expected 0, got {ans4}"
    print()

    print("=== Test 5: Deep aligned chain down one side (expected 4) ===")
    # Depths: 0 -> 1 -> 2 -> 3
    # Values: 0 -> 1 -> 2 -> 3  (all aligned)
    root5 = Tree(0, Tree(1, Tree(2, Tree(3))))
    ans5 = longest_aligned_chain(root5)
    print("Longest aligned chain:", ans5)
    assert ans5 == 4, f"Expected 4, got {ans5}"
    print()

    print("=== Test 6: Chain starts NOT at root (expected 3) ===")
    # Root not aligned, but a subtree contains aligned chain:
    #       9
    #      /
    #     5
    #    /
    #   2
    #    \
    #     3
    #
    # Aligned chain can start at node with value=2 at depth=2, then 3 at depth=3 => length 2
    # Let's make a better one with length 3:
    #       9
    #      /
    #     5
    #    /
    #   2
    #  /
    # 3
    #/
    #4
    #
    # depths: 2->3->4 values: 2->3->4 => length 3
    root6 = Tree(9,
                 Tree(5,
                      Tree(2,
                           Tree(3,
                                Tree(4)))))
    ans6 = longest_aligned_chain(root6)
    print("Longest aligned chain:", ans6)
    assert ans6 == 3, f"Expected 3, got {ans6}"
    print()
    
    tests = [
      # Test 1: Example from the book
      (Node(7, Node(1, Node(2, Node(4), Node(3)),
                    Node(8)), Node(3, Node(2, Node(3), Node(3)))), 3),
      # Variation 1
      (Node(7, Node(1, Node(20, Node(4), Node(3)),
                    Node(8)), Node(3, Node(2, Node(3), Node(3)))), 3),
      # Variation 2
      (Node(7, Node(1, Node(2, Node(4), Node(3)),
                    Node(8)), Node(3, Node(20, Node(3), Node(3)))), 3),
      # Variation 3
      (Node(7, Node(1, Node(20, Node(4), Node(3)),
                    Node(8)), Node(3, Node(20, Node(3), Node(3)))), 1),
      # Test 2: Empty tree
      (None, 0),
      # Test 3: Single aligned node
      (Node(0), 1),
      # Test 4: Single unaligned node
      (Node(1), 0),
      # Test 5: Path through root
      (Node(0, Node(1), Node(1)), 3),
      # Test 6: No aligned nodes
      (Node(5, Node(4), Node(2)), 0),
      # Test 7
      (Node(0, Node(1, Node(2), Node(2)), Node(1)), 4),
  ]

    for i, (root, want) in enumerate(tests, 1):
        got = aligned_path(root)
        print(got == want, f"\naligned_path(): got: {got}, want: {want}\n")

    run_hidden_message_tests()

    print("All tests passed ✅")

if __name__ == "__main__":
    main()