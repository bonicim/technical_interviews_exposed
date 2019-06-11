from src.algorithms.node import Node

# Given two children of a simple binary tree, get the nearest ancestor
# Assume children will never be null or empty
def get_nearest_ancestor_v2(child1, child2):
    current_parent = child1.parent
    child1_parents = []
    while current_parent:
        child1_parents.append(current_parent)
        current_parent = current_parent.parent
    
    child2_parent = child2.parent
    while child2_parent :
        if child2_parent in child1_parents:
            return child2_parent
        else:
            child2_parent = child2_parent.parent
    
    return child2