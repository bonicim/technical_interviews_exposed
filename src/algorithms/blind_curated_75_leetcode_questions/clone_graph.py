from src.algorithms.node import Node


def clone_graph(node):
    if not node:
        return None

    node_map = dict()
    queue = []

    queue.append(node)
    node_map[node] = Node(node.data, neighbors=[])

    while queue:
        current_node = queue.pop(0)

        for neighbor in current_node.neighbors:
            if neighbor not in node_map:
                # add it to the map
                node_map.update({neighbor: Node(neighbor.data, neighbors=[])})

                # add the neighbor to queue
                queue.append(neighbor)

            # update the cloned graph
            clone_of_current_node = node_map.get(current_node)
            clone_of_current_node.neighbors.append(node_map.get(neighbor))

    return node_map.get(node)
