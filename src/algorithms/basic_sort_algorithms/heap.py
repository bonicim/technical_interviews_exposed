def max_heapify(A, index, heap_size):
    largest = index
    # we assume that the heap starts at index 0
    left = index * 2 + 1
    right = index * 2 + 2

    # update the largest index if left child is bigger than current largest index
    if left < heap_size and A[left] > A[largest]:
        largest = left
    # update the largest index if right child is bigger than current largest index
    if right < heap_size and A[right] > A[largest]:
        largest = right

    # update and heapify only if the largest index is no longer the current node, meaning that at most one of the
    # children of the current node is bigger than the current node, thus violating the max heap invariant
    # if we have to do update the current node, then we have to ensure the invariant is enforced on the child that got swapped with the current node
    # otherwise, do nothing
    if largest != index:
        swap(index, largest, A)
        max_heapify(A, largest, len(A))


def build_heap(A):
    heap_size = len(A)
    # we start inte
    # Walk backwards on the array starting at the halfway point because it the rightmost and deepest node that has a child
    # We choose the halfway index because heap's are left-balanced, meaning that the tree is builds from left to right.
    # There is no need to enforce the heap invariant on leaves because they have no children.
    for i in range((heap_size / 2), -1, -1):
        max_heapify(A, i, len(A))


def heapsort(A):
    heap_size = len(A)
    build_heap(A)
    # print A #uncomment this print to see the heap it builds
    for index in range(heap_size - 1, 0, -1):
        # the largest element will always be in the first index for a maxheap. Thus to sort the array in-place in ascending order, we need
        # to swap the first element with the current index
        swap(0, index, A)

        # we decrement the heapsize by one because we need to maintain the heap invariant between the first index and the last item of the heap one before the index that we did the swap on
        heap_size -= 1
        max_heapify(A, 0, heap_size)
