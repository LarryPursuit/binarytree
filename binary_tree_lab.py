from typing import Optional

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None


def max_depth(root: Optional[TreeNode]) -> int:
    """
    Return the number of nodes on the longest root-to-leaf path.

    Recursive approach: an empty tree has depth 0. Otherwise the depth of a
    tree is 1 (for the current node) plus the depth of its deeper subtree.
    Runs in O(n) time and O(h) call-stack space, where h is the tree height.
    """
    # Base case: we've stepped past a leaf, so this path adds no nodes.
    if root is None:
        return 0

    # Measure each subtree independently, then keep the longer path
    # and count the current node.
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    return max(left_depth, right_depth) + 1


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Return the lowest common ancestor of p and q in a Binary Search Tree.

    BST property: everything in a node's left subtree is smaller than the
    node, and everything in its right subtree is larger. So:
      - If p and q are both smaller than root, their LCA lives on the left.
      - If p and q are both larger than root, their LCA lives on the right.
      - Otherwise they split here (or one of them *is* root), so root is the
        deepest node that has both as descendants.
    Runs in O(h) time, where h is the tree height.
    """
    # Both targets are smaller: the split point must be in the left subtree.
    if p.val < root.val and q.val < root.val:
        return lowest_common_ancestor(root.left, p, q)

    # Both targets are larger: the split point must be in the right subtree.
    if p.val > root.val and q.val > root.val:
        return lowest_common_ancestor(root.right, p, q)

    # p and q fall on different sides of root (or one equals root),
    # so root is their lowest common ancestor.
    return root
