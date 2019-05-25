from src.algorithms.node import Node

def get_nearest_ancestor(root, node1, node2):
    while root is not None:
        if node1.data > root.data and node2.data > root.data:
            root = root.right
        elif node1.data < root.data and node2.data < root.data:
            root = root.left
        else:
            return root
    return None
        


