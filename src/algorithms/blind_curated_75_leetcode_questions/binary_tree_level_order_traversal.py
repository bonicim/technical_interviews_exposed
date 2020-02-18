def level_order(root):
    return level_order_bfs(root)


def level_order_bfs(root):
    levels = []
    # Handle the null edge case
    if not root:
        return levels

    current_level = 0
    queue = [root]

    while queue:
        # Step 1: Append an empty list to the list of levels
        levels.append([])

        # Step 2: Loop through the nodes on the current level, which is the length of the queue
        # and build the list of current nodes
        number_of_nodes_on_current_level = len(queue)

        for _ in range(number_of_nodes_on_current_level):
            # get the current node
            node = queue.pop(0)

            # add the node to the current levels list
            nodes_at_level = levels[current_level]
            levels[current_level] = nodes_at_level.append(node.val)

            # add the node's children to the queue
            # we will not iterate through these children since we are only iterating through current nodes in the queue before we entered this for loop
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # Step 3: Increase the current level
        current_level += 1

    return levels


def level_order_dfs_preorder(root):
    levels = []
    # Handle the null edge case
    if not root:
        return levels

    def level_order_helper(levels, node, level):
        # Since a level on a binary tree starts at 0, every time we our level is equal to the number of levels
        # in the levels list, we know that we need to insert a new list for that level

        # For example, if our current list of levels has 5 lists, that means we are keeping track
        # of 4 levels. And if the current level that we are on, level, is 5, then we need to append a
        # new list to levels. That new list will contain all the nodes on that level
        if len(levels) == level:
            levels.append([])

        # append the current node to the current level list
        # this is equivalent of printing the root node during a preorder traversal
        levels[level].append(node.val)

        # append the children on the left and right subtrees just like in preorder traversal
        if node.left:
            levels = level_order_helper(levels, node.left, level + 1)
        if node.right:
            levels = level_order_helper(levels, node.right, level + 1)

        return levels

    return level_order_helper(levels, root, 0)
