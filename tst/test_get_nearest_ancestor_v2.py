import pytest
from src.algorithms.get_nearest_ancestor_v2 import get_nearest_ancestor_v2
from src.algorithms.node import Node

def test_easy_case():
    assert get_nearest_ancestor_v2(left_child, right_child) == Node(42)

def test_ancerstor_2nd_level():
    assert get_nearest_ancestor_v2(child1, child2) == Node(13)

def test_ancerstor_unbalanced():
    assert get_nearest_ancestor_v2(child1, child2_1_1) == Node(13)

def test_ancestor_unbalanced_v2():
    assert get_nearest_ancestor_v2(right_child, child2_1_1) == Node(42)

def test_ancestor_unbalanced_v3():
    assert get_nearest_ancestor_v2(child2_1, child2_1_1) == Node(7)

root = Node(42)
left_child = Node(13, parent=root)
right_child = Node(15, parent=root)
root.left = left_child
root.right = right_child

child1 = Node(32, parent=left_child)
child2 = Node(7, parent=left_child)
left_child.left = child1
left_child.right = child2

child2_1 = Node(8, parent=child2)
child1.left = child2_1
child2_1_1 = Node(10, parent=child2_1)
child2_1.left = child2_1_1