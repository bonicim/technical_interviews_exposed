import pytest
from src.algorithms.get_nearest_ancestor import get_nearest_ancestor
from src.algorithms.node import Node

def test_typical_case():
    node1 = Node(10)
    node2 = Node(30)
    root = Node(20)
    root.left = node1
    root.right = node2
    assert get_nearest_ancestor(root, node1, node2) == root
