def lowest_common_ancestor(root, node1, node2):
    # return iterative_solution(root, node1, node2)
    return recursive_solution(root, node1, node2)


def recursive_solution(root, node1, node2):
    parent_data = root.data
    node1_data = node1.data
    node2_data = node2.data

    if node1_data > parent_data and node2_data > parent_data:
        return recursive_solution(root.right, node1, node2)
    elif node1_data < parent_data and node2_data < parent_data:
        return recursive_solution(root.left, node1, node2)
    else:
        return root.data


def iterative_solution(root, node1, node2):
    node1_data = node1.data
    node2_data = node2.data
    current = root

    while current:
        current_data = current.data
        if node1_data > current_data and node2_data > current_data:
            current = current.right
        elif node1_data < current_data and node2_data < current_data:
            current = current.right
        else:
            return current.data
