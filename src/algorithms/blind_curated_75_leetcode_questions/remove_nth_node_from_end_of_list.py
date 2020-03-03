from src.algorithms.node import Node

"""
    The Crux: Whenever we need to repoint a pointer in a linked list, we need to have a temporary pointer pointing at
    the node before the node which must be removed. Knowing how to get to that node can be done in two ways. First, get
    the length of the list and then do another pass to land on the node. The less obvious way is to use a two pointer
    approach in which the distance between both pointers is n.
"""


def remove_nth_from_end(head, n):
    return get_length_then_remove_nth_node(head, n)


def get_length_then_remove_nth_node(head, n):
    length = 0
    ans = Node(-1, next=head)
    temp = ans
    while temp:
        length += 1
        temp = temp.next

    steps_to_nth_plus_one_node = length - n
    temp = ans
    while steps_to_nth_plus_one_node > 0:
        steps_to_nth_plus_one_node -= 1
        temp = temp.next

    temp.next = temp.next.next

    return ans.next


def two_pointers_solution(head, n):
    ans = Node(-1, next=head)
    left = ans
    right = ans

    for _ in range(n + 1):
        right = right.next

    while right:
        right = right.next
        left = left.next

    left.next = left.next.next

    return ans.next
