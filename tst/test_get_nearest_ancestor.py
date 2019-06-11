import pytest
from src.algorithms.get_nearest_ancestor import get_nearest_ancestor
from src.algorithms.node import Node

def test_typical_case():
    root = Node(20)
    root.left = Node(10)
    root.right = Node(30)
    assert get_nearest_ancestor(root, 10, 30) == root
