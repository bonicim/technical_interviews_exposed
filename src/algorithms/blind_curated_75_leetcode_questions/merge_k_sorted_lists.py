from src.algorithms.node import Node


def merge_k_sorted_lists(lists):
    # return iterative_solution(lists)
    return heap_solution(lists)


def iterative_solution(lists):
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


def compare_one_by_one_solution(lists):
    return


# uses a heap to optimize the comparisons between the heads of all the lists
def heap_solution(lists):

    return
