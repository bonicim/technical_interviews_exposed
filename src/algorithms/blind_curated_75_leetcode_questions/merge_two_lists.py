from src.algorithms.node import Node


def merge_two_lists(list1, list2):
    # return iterative_solution(list1, list2)
    return recursive_solution(list1, list2)


def iterative_solution(list1, list2):
    """
    Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

    Example:

    Input: 1->2->4, 1->3->4
    Output: 1->1->2->3->4->4

    """
    pre_root = Node(-1)
    current = pre_root

    while list1 and list2:
        if list1.data <= list2.data:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    if not list1:
        current.next = list2
    else:
        current.next = list1

    return pre_root.next


def recursive_solution(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1
    if list1.data < list2.data:
        list1.next = recursive_solution(list1.next, list2)
        return list1
    else:
        list2.next = recursive_solution(list1, list2.next)
        return list2
    return list1
