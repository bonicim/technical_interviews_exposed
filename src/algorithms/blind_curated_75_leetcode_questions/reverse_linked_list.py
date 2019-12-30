def reverse_linked_list(head):
    # return iterative_solution(head)
    return recursive_solution(head)


def iterative_solution(head):
    curr = head
    prev = None
    upnext = None

    while curr:
        upnext = curr.next
        curr.next = prev
        prev = curr
        curr = upnext

    return prev


def recursive_solution(head):
    if not head or not head.next:
        return head

    in_front_node = recursive_solution(head.next)
    head.next.next = head
    head.next = None

    return in_front_node
