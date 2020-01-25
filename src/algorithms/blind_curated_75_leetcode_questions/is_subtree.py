"""
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.
"""

""" Commentary

This problem demonstrates your comfort and knowledge with recursion. To solve this problem, we
would like to have a function that would check if two trees are the same.

Let's just assume that we did have a function that would tell us if two trees are the same, i.e.
they fulfill the requirement of being exact copies of each other in values and strucutre.

First, let's check if they are the same at the root level. If not, then check if the left subtree of s
is the same with t. If not, then check if the right subtree of s is the same with t.

The difficult part is implementing the fucntion that tells us if two trees are the same or not.
Given two nodes, if they're both null, then they are indeed the same tree. There is nothing left to check.
If one of them is null, then they are defintely not the same and and there is nothing more to check.
If both values at the root are not equal, they are not subtrees of each there is nothing more to check.

Finally, if both values are the same, then we check both the left and right subtrees (we have to check both) and then
return true if both left and right subtrees are equal; otherwise false. But how do we know if both left and right subtrees
are equal? Well, if only I had a function that would check if two subtrees are the same.......wait, I do have one. I was just
creating it. That is the beauty of recursion as you build your function you actually solve it by using that same recursive function.
"""


def is_subtree(s, t):
    def are_same_trees(s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val != t.val:
            return False
        # the roots are equal; we need to validate that the left and right subtrees are also equal
        return are_same_trees(s.left, t.left) and are_same_trees(s.right, t.right)

    if not s:
        return False

    return (
        are_same_trees(s, t) or are_same_trees(s.left, t) or are_same_trees(s.right, t)
    )
