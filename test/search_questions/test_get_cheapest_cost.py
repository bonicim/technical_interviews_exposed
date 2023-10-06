import pytest
from src.algorithms.search_questions.cheapest_sales_path import Node
from src.algorithms.search_questions.cheapest_sales_path import get_cheapest_cost


def test_regular_case():
    """
     0
    2   3
    5   1  6
    """
    n0 = Node(0)
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n6 = Node(6)
    n5 = Node(5)

    n0.children = [n2, n3]
    n3.children = [n1, n6]
    n2.children = [n5]

    expected = 4
    actual = get_cheapest_cost(n0)

    assert actual == expected


def test_single_node():
    n = Node(5)

    expected = 5
    actual = get_cheapest_cost(n)

    assert actual == expected
