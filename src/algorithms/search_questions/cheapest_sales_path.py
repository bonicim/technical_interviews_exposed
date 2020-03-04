""" Sales Path
The car manufacturer Honda holds their distribution system in the form of a tree (not necessarily binary). The root is the company itself, and every node in the tree represents a car distributor that receives cars from the parent node and ships them to its children nodes. The leaf nodes are car dealerships that sell cars direct to consumers. In addition, every node holds an integer that is the cost of shipping a car to it.

A path from Honda’s factory to a car dealership, which is a path from the root to a leaf in the tree, is called a Sales Path. The cost of a Sales Path is the sum of the costs for every node in the path. For example, in the tree above one Sales Path is 0→3→0→10, and its cost is 13 (0+3+0+10).

Honda wishes to find the minimal Sales Path cost in its distribution tree. Given a node rootNode, write a function getCheapestCost that calculates the minimal Sales Path cost in the tree.

Implement your function in the most efficient manner and analyze its time and space complexities.

For example:

Given the rootNode of the tree in diagram above

Your function would return:

7 since it’s the minimal Sales Path cost (there are actually two Sales Paths in the tree whose cost is 7: 0→6→1 and 0→3→2→1→1)
"""


""" Commentary
This is a classic BFS, DFS question. The best way to approach this question is to start with
simpler examples. By doing so, you can arrive much quicker at the base case and make a better and more
informed decision as to which implementation you should choose to code up.

A top-down approach would most likely use DFS and require a slightly complicated algorithm and
a complicated helper method. Moreover, you incur cost on the stack space. Most importantly, if you
are not that strong at recursion, you might get stuck at trying to implement DFS.

A bottom-up approach is the better approach because it forces you to look at the simplest
case, i.e. a tree of just one node. Moreover, the BFS approach avoids the problems of running out of
memory for a stack and forces you to visualize the problem by creating data structures to hold information
such as visited nodes, parent nodes, and a frontier of nodes to explore.
"""


class Node:
    def __init__(self, cost):
        self.cost = cost
        self.children = []


def get_cheapest_cost(rootNode):
    return get_cheapest_cost_bottom_up(rootNode)
    # return get_cheapest_cost_top_down(rootNode, rootNode.cost, float("inf"))


def get_cheapest_cost_bottom_up(rootNode):
    def get_path_cost(node, parents):
        parent = parents[node]
        if not parent:
            return node.cost

        return node.cost + get_path_cost(parent, parents)

    frontier = [rootNode]
    visited = set([rootNode])
    parents = {rootNode: None}
    min_cost = float("inf")

    while frontier:
        current_node = frontier.pop(0)
        # if we hit a leaf, then calculate the cost
        if not current_node.children:
            min_cost = min(min_cost, get_path_cost(current_node, parents))
        else:
            for child in current_node.children:
                parents[child] = current_node
                visited.add(child)
                frontier.append(child)

    return min_cost


def get_cheapest_cost_top_down(rootNode, acc_cost, min_cost):
    if not rootNode:
        return 0

    if not rootNode.children:
        return rootNode.cost

    for child in rootNode.children:
        current_cost = get_cheapest_cost_top_down(child, acc_cost, min_cost)
        min_cost = min(min_cost, current_cost + rootNode.cost + acc_cost)

    return min_cost
