def is_balanced(root):
    """ Given a binary tree, determine if it is height-balanced.

    For this problem, a height-balanced binary tree is defined as:
    a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

    Example 1:

    Given the following tree [3,9,20,null,null,15,7]:

         3
        / \
        9  20
            /  \
        15   7
    Return true.

    Example 2:

    Given the following tree [1,2,2,3,3,null,null,4,4]:

         1
        / \
        2   2
        / \
        3   3
        / \
        4   4
    Return false.
    """
    # return is_balanced_naive_solution(root)
    return is_balanced_optimal_solution(root)
    # return is_balanced_optimal_solution_using_classes(root)


def is_balanced_naive_solution(root):
    # This solution is naive because it checks the height at every node, starting at the root.
    # We start at the root and find the height of the left and right subrtree;
    # if they're balanced, then we have to check if the left and right nodes are balanced,
    # triggering each node to find the height at its respective subtrees, thus requiring us to
    # "recount" the height again. This is duplicate effort that is unnecessary.
    def height(node):
        if not node:
            return 0
        return max(height(node.left), height(node.right)) + 1

    if not root:
        return True

    height_diff = abs(height(root.left) - height(root.right))
    if height_diff > 1:
        return False
    else:
        return is_balanced_naive_solution(root.left) and is_balanced_naive_solution(
            root.right
        )


def is_balanced_optimal_solution(root):
    # The optimal solution runs in O(n) time because it doesn't recount the same height as in
    # in the naive solution. Rather, this solution is a bottom up approach. It recurses all the way
    # down to the leaf node, and returns -1 if its unbalanced or its height. This result is immediately
    # bubbled up to the root. The algorithm immediately stops once it finds an unbalanced node.
    def check_height(root):
        if not root:
            return 0

        left_height = check_height(root.left)
        if left_height == -1:
            return left_height

        right_height = check_height(root.right)
        if right_height == -1:
            return right_height

        height_diff_between_left_right_subtrees = abs(left_height - right_height)
        # this check is crucial, because it bubbles up the difference anywhere in the bottom of the tree to the root
        if height_diff_between_left_right_subtrees > 1:
            return -1

        max_height_at_this_node = max(left_height, right_height) + 1
        return max_height_at_this_node

    return check_height(root) != -1


def is_balanced_optimal_solution_using_classes(root):
    # This solution is the same approach as is_balanced_optimal solution except that it
    # uses a class to hold the height and the is_balanced status.
    # Using a class makes the code more clear and shows intent. The meaning of -1
    # is hidden and is wrapped around the is_balanced boolean flag of the TreeBalanceStatus class.
    tree_balance_status = check_balance(root)
    return tree_balance_status.is_balanced


class TreeBalanceStatus:
    def __init__(self, is_balanced, height):
        self.is_balanced = is_balanced
        self.height = height


def check_balance(root):
    if not root:
        return TreeBalanceStatus(True, -1)

    tree_balance_status_left = check_balance(root.left)
    if not tree_balance_status_left.is_balanced:
        return tree_balance_status_left

    tree_balance_status_right = check_balance(root.right)
    if not tree_balance_status_right.is_balanced:
        return tree_balance_status_right

    is_balanced_at_root = (
        abs(tree_balance_status_left.height - tree_balance_status_right.height) <= 1
    )
    height_at_root = (
        max(tree_balance_status_left.height, tree_balance_status_right.height) + 1
    )

    return TreeBalanceStatus(is_balanced_at_root, height_at_root)
