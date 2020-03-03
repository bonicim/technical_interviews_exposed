import heapq


def kth_smallest(root, k):
    return sorting_solution(root, k)


def in_order_solution(root, k):
    elements = []

    def in_order_traverse(root):
        if not root:
            return

        in_order_traverse(root.left)
        elements.append(root.val)
        in_order_traverse(root.right)

    in_order_traverse(root)

    return elements[k - 1]


def in_order_iterative_solution(root, k):
    temp = root
    stack = []

    while True:
        while temp:
            stack.append(temp)
            temp = temp.left
        temp = stack.pop()
        k -= 1
        if not k:
            return temp.data
        temp = temp.right


def heap_solution(root, k):
    root_array = []

    def in_order_traverse(root):
        if not root:
            return

        in_order_traverse(root.left)
        root_array.append(root.val)
        in_order_traverse(root.right)

    in_order_traverse(root)
    max_heap = []
    current_size = 0
    for element in root_array:
        if len(max_heap) < k:
            heapq.heappush(max_heap, element * -1)
            current_size += 1
        else:
            if element < (max_heap[0] * -1):
                heapq.heappushpop(max_heap, element)

    return max_heap[0] * -1


def quick_select_solution(root, k):
    elements = []

    def build_elements(root):
        if not root:
            return

        build_elements(root.left)
        elements.append(root.val)
        build_elements(root.right)

    build_elements(root)

    def swap(x, y):
        elements[x], elements[y] = elements[y], elements[x]

    def partition(left, right):
        pivot = left + ((right - left) // 2)
        pivot_val = elements[pivot]
        swap(right, pivot)
        tail = left

        for index in range(left, right - 1):
            if elements[index] < pivot_val:
                swap(tail, index)
                tail += 1
        swap(tail, right)
        return tail

    def quick_select(left, right, kth):
        if left >= right:
            return

        pivot_index = partition(left, right)

        if pivot_index == kth:
            return
        if kth < pivot_index:
            quick_select(left, pivot_index - 1, kth)
        else:
            quick_select(pivot_index + 1, right, kth)

    quick_select(0, len(elements) - 1, k - 1)

    return elements[k - 1]
