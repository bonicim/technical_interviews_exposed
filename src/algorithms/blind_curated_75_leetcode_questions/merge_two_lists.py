from src.algorithms.node import Node

"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

""" Commentary
The implementation of this solution is tricky because it requires the use of pointers and combining two lists into one.
However, the recurrence that highlights the solution is quite simple. Namely, if the current element at List1 is less than List2,
then point the current element at List1 to the merging of the elements of the rest of the elements of List1 and List2. Otherwise, point the
current element at List2 to the merging of the elements of the rest of the elements of List2 and List1. The result of that merge should be single list
and the current element will point at that newly merged list. The recursive solution is tricky to understand, but drawing a picture and working through
an example helps in understanding.

The iterative solution uses a previous pointer that will always be behind the List1 and List2 pointers. If List1 is less than or equal to to list2,
then the previous pointer will set its next to List1, List1 will then advance, and the previous pointer will advance. Otherwise, the previous pointer
will set its next to List2, List2 will advance, and previous pointer will advance. We have to catch the edge case in which one of the list is shorter than
the other. So once we've completed the iteration, we check which List is still not null and then set the previous.next to point to that non-null list.

"""


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
    prev = pre_root

    while list1 and list2:
        if list1.data <= list2.data:
            prev.next = list1
            list1 = list1.next
        else:
            prev.next = list2
            list2 = list2.next
        prev = prev.next

    if not list1:
        prev.next = list2
    else:
        prev.next = list1

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
