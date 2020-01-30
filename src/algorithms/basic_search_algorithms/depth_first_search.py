def dfs_iterative(start, graph, target):
    visited = set()
    stack = []
    path = []

    stack.append(start)
    visited.add(start)

    while stack:
        current = stack.pop
        path.append(current)
        if current == target:
            return path

        neighbors = graph.get(current)

        # we hit a deadend, so update the path to remove this current node
        if not neighbors:
            path.pop()

        for neighbor in neighbors:
            if neighbor not in visited:

                # do logic if neighbor is the target
                if neighbor == target:
                    path.append(neighbor)
                    return path

                visited.add(neighbor)
                stack.append(neighbor)
                # perform logic such as recording our path, checking if we found our target, print our path, record when we backtrack

    return "Path to target not found"
    # depending on the search logic, we can return a list of all paths, a path, or that we've finished searching all nodes


# this version of DFS searches until it hits the target and then returns the path
def dfs_recursive(curr, graph, visited, path, target):
    if curr == target:
        return path

    visited.add(curr)

    # perform logic such as recording our path, checking if we found our target, print our path, record when we backtrack
    path.append(curr)

    neighbors = graph.get(curr)

    # if we hit a dead end, then backtrack
    if not neighbors:
        path.pop()
        return path

    # otherwise, keep searching
    for neighbor in neighbors:
        if neighbor not in visited:

            # if we found our target return the path
            if neighbor == target:
                path.append(neighbor)
                return path

            # otherwise, go deep in the tree and search
            path = dfs_recursive(neighbor, graph, visited, path, target)
