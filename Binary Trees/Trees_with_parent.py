"""
This demonstrates a tree with a parent and ID
"""

class Tree:
    def __init__(self, parent, id, left=None,right=None):
        self.parent = parent 
        self.id = id 
        self.left = left 
        self.right = right
        
        
# return whether it is the the root node
def is_root(node):
    return not node.parent

# return the id's of all of its ancestors as an array in any order
def ancestor_ids(node):
    ids = []
    while node.parent:
        node = node.parent 
        ids.append(node.id)
    return ids 

# return the depth of the node 
def depth(node):
    res = 0 
    while node.parent:
        node = node.parent 
        res += 1 
    return res

# Given two non-nullnodes from the same tree, node1 and node2, return the Id of the Lowest Common
# Ancestor (LCA).The LCA of twonodes is the deepest nodein the tree which is the non-strct
# ancestor of both. 'Non-strict means that a node is considered its own ancestor
def LCA(node1, node2):
    depth1 = depth(node1)
    depth2 = depth(node2) 
    while depth1 > depth2:
        node1 = node1.parent 
        depth1 -= 1 
    while depth2 > depth1: 
        node2 = node2.parent 
        depth2 -= 1 
    while node1.id != node2.id:
        node1 = node1.parent 
        node2 = node2.parent 
    return node1.id

# Given two non-null nodes from the same tree, return the distance betwen them.The sequence of edges between two
# nodes is called a path,and the number of edges in the path is the distance between the
# two nodes. Note that, in a binary tree, the path between any two nodes is unique.
def distance(node1, node2):
    lca_id = LCA(node1, node2)
    dist = 0 
    while node1.id != lca_id:
        dist += 1 
        node1 = node1.parent 
    while node2.id != lca_id:
        dist += 1 
        node2 = node2.parent 
    return dist


def build_example_tree():
    """
            A
          /   \
         B     C
        / \     \
       D   E     F
          /
         G
    """
    A = Tree(None, "A")
    B = Tree(A, "B")
    C = Tree(A, "C")
    D = Tree(B, "D")
    E = Tree(B, "E")
    F = Tree(C, "F")
    G = Tree(E, "G")

    A.left, A.right = B, C
    B.left, B.right = D, E
    C.right = F
    E.left = G

    return A, B, C, D, E, F, G


def main():
    A, B, C, D, E, F, G = build_example_tree()

    # ---------------------------
    # LCA TESTS
    # ---------------------------
    print("LCA tests...")
    assert LCA(D, G) == "B"   # D is under B, G is under E->B
    assert LCA(E, G) == "E"   # non-strict ancestor case (E is ancestor of G)
    assert LCA(D, E) == "B"   # siblings under B
    assert LCA(D, F) == "A"   # across left and right subtrees
    assert LCA(C, F) == "C"   # C is ancestor of F
    assert LCA(A, G) == "A"   # root with any node -> root
    assert LCA(G, G) == "G"   # same node -> itself

    print("  ✅ LCA tests passed")

    # ---------------------------
    # DISTANCE TESTS
    # ---------------------------
    print("Distance tests...")
    assert distance(D, G) == 3   # D->B->E->G
    assert distance(E, G) == 1   # E->G
    assert distance(D, E) == 2   # D->B->E
    assert distance(D, F) == 4   # D->B->A->C->F
    assert distance(A, G) == 3   # A->B->E->G
    assert distance(G, G) == 0   # same node distance 0
    assert distance(C, F) == 1   # C->F

    print("  ✅ Distance tests passed")

    # Optional: show some outputs
    print("\nSample outputs:")
    print("LCA(D, G) =", LCA(D, G))
    print("distance(D, G) =", distance(D, G))


if __name__ == "__main__":
    main()