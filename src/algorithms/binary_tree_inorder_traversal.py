def inorder_traversal(root):
    tree = BinaryTree(root)
    tree.inorder_traversal_v1()
    return tree.inorder_traversal_display

    # return recursive_traversal(root, [])


# Unnecessarily creates a new list on every recursive call; not memory efficient
def recursive_traversal(root, acc):
    if not root:
        return []

    left = recursive_traversal(root.left, acc)
    right = recursive_traversal(root.right, acc)
    return left + [root.data] + right


class BinaryTree:
    def __init__(self, root):
        self.inorder_traversal_display = []
        self.root = root

    def inorder_traversal_v1(self):
        self.__recursive_traversal(self.root)

    def __recursive_traversal(self, root):
        if not root:
            return self.inorder_traversal_display

        self.__recursive_traversal(root.left)
        self.inorder_traversal_display.append(root.data)
        self.__recursive_traversal(root.right)
