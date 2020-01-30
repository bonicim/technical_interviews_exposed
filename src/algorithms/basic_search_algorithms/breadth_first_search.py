# BFS is typically used for finding paths, typically the shortest path, so we will track a path here
def bfs(graph, start, end):
    discovered = set()
    discovered.add(start)
    parents = {}
    parents.update({start: None})
    queue = []
    queue.append(start)

    while queue:
        current = queue.pop(0)
        # do some logic on the current node
        for neighbor in current.neighbors:
            # do some logic on the current neighbor
            if neighbor not in discovered:
                discovered.add(neighbor)
                parents[neighbor] = current
                queue.append(neighbor)

    return shortest_path(start, end, parents)


def shortest_path(start, end, parents):
    if start == end or not end:
        return start.data

    return str(end.data) + str(shortest_path(start, parents[end], parents))
