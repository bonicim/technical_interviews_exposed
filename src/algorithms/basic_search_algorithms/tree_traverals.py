def inorder(root, order=[]):
    if root:
        inorder(root.left, order)
        order.append(root.val)
        inorder(root.right, order)


def preorder(root, order=[]):
    if root:
        order.append(root.val)
        preorder(root.left)
        preorder(root.right)


def postorder(root, order=[]):
    if root:
        preorder(root.left)
        preorder(root.right)
        order.append(root.val)
