"""
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""

""" Commentary

This problem lends itself so well to recursion that the actual implementation almost looks like magic,
as if some engineer waved their hands and poof, a tree is now inverted.

To attack this problem, consider the very smalles case and build from there. This is a common
technique to use when you are simply stuck and don't know how to begin.

What is the inverted tree of a tree with just one node? The node itself.

What about a the most basic tree, a parent and two children. The inverted tree would be the
root itself and then the two children switched.

What about a more complicated tree with more descendents? The same would apply. The inverted tree
would be the root, then the two children switched, but we have to take a pause first. The children of the right child
need to be inverted first. Same with the left. So we do that. Then we need to switch those children of the right child
with the children of the left child. Then we can switch the left and right child of the parent. And on and on.

Draw out a picture of the switching and sequence of when and how it happens. Better yet, copy this code
and run the debugger to see it live.
"""


def invert_binary_tree(root):
    if not root:
        return None

    inverted_right_child = invert_binary_tree(root.right)
    inverted_left_child = invert_binary_tree(root.left)
    root.right, root.left = inverted_left_child, inverted_right_child

    return root
