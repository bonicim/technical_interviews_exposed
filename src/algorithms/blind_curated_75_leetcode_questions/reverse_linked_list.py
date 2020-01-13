""" Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

""" Commentary

This question tests your ability to deal with pointers and recursion. It is a good question that measures an engineer's technical depth, ability
to deal with pointers, and recursion. I like this question because it appears deceptively easy.

The key to solving this question is knowing how to traverse the linked list in such a way that you don't lose track of where you
are, where you're going, and where you're coming from. The iterative solution keeps track of all these positions. It has a pointer to
the previous node, the upcoming node, and the current node. With this information, you very carefully change the pointers of each node.
In our while loop, we must first set the upcoming node. This ensures that we don't lose the reference to the next node that needs to be changed.
Second, we repoint the current node's pointer to the previous node. This will reverse the linked list at this point in the list. Then
the previous node needs to be changed to the current node. And then the current node is changed to the upcoming node. After all these steps are
done, we repeat the process until we hit a Null reference.

Now, what do we return? We return the reference to the previous node because it was the last node but now is the first node in a
reversed linked list. It helps to remember a biblical saying: "The first shall be last and the last shall be first". When we reverse a list, when
the last item will now be the first. And our pointer to the previous node, once all pointer changes have been completed, will eventually
end on the last item of the list, which now will be the first of a reversed linked list.

The recursive solution is a bit more tricky. Instead of starting from the first element in the list, the solution starts at the end of the list.
When we reach the end of the list, we repoint the node in front of the current node to point to the current node. Then we repoint the current node's pointer to
None. Why? Because if we don't, we will have a cycle at the first node. It will still be pointing to the next node instead of Null. Finally, the
recursive solution will keep passing the last node to every previous call on the stack all the way up to the first call. And thus the first call
will correctly give the pointer to the last node which is what we want in a reversed linked list.
"""


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
