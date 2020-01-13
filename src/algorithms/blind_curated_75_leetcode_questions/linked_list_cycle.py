from src.algorithms.node import Node

""" Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
"""

""" Commentary

This question, with the constraint that it must use constant space, tests your ability to think in terms of pointers. In this case, we use two pointers to do a job for us.
This is a common pattern among linked list, tree, or graph questions. We create two pointers and move them in such a way to help us solve the problem.
In this case the problem is to detect a cycle in a linked list. So how do we use two pointers to do it? Have a slow and fast pointer. Eventually, the fast pointer will
either end on Null, which means we have no cycles, or it will eventually catch up with the slow pointer, thereby signifying a cycle.

One way to think about cycles in a linked list is that if imagine a racetrack and having a fast and slow runner. Eventually the fast runner will lap the slow one. We use the same idea
to detect a cycle in a linked list given the constraint of constant space.
"""


def has_cycle(head):
    return no_space_two_pointers_solution(head)


def no_space_two_pointers_solution(head):
    if not head or not head.next:
        return False

    slow_pointer = head
    fast_pointer = head.next

    while slow_pointer != fast_pointer:
        # we've reached the end of the linked list; there is no cycle
        if not fast_pointer or not fast_pointer.next:
            return False

        fast_pointer = fast_pointer.next.next
        slow_pointer = slow_pointer.next

    # If we end here, that means the fast pointer has caught up with the slow pointer and that we have a cycle
    return True


def iterative_solution(head):
    temp = Node(-11)
    temp.next = head
    visited = set()

    while temp:
        if temp.next in visited:
            return True

        visited.add(temp.next)
        temp = temp.next

    return False
