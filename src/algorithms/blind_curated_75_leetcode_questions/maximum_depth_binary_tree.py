def max_depth(root):
    if not root:
        return 0

    left_depth = 1 + max_depth(root.left)
    right_depth = 1 + max_depth(root.right)

    return max(left_depth, right_depth)
