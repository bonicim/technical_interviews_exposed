import random


def get_closest_points(points, kth):
    """
    We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

    (Here, the distance between two points on a plane is the Euclidean distance.)

    You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

    Example 1:

    Input: points = [[1,3],[-2,2]], K = 1
    Output: [[-2,2]]
    Explanation:
    The distance between (1, 3) and the origin is sqrt(10).
    The distance between (-2, 2) and the origin is sqrt(8).
    Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
    We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
    Example 2:

    Input: points = [[3,3],[5,-1],[-2,4]], K = 2
    Output: [[3,3],[-2,4]]
    (The answer [[-2,4],[3,3]] would also be accepted.)
    """
    # return sorting_solution(points, kth)
    return divide_conquer_solution(points, kth)


def sorting_solution(points, kth):
    """
    The key intution is to sort the distance from origin for each point and then return the closest points determined by target.
    The runtime would be the cost of sort, which would be n log n.
    """
    points_distances = [(pos, pos[0] ** 2 + pos[1] ** 2) for pos in points]
    points_sorted = sorted(points_distances, key=lambda tup: tup[1])
    return [tup[0] for tup in points_sorted[:kth]]


def divide_conquer_solution(points, kth):
    """
    The key idea is that we need to select the kth closest point to the origin.
    Unlike the sorting_solution which uses the quicksort algorithm and runs in O(n log n),
    this solution uses a selction algorithm called quickselect, which is related to quicksort.

    Quickselect uses the same overall approach as quicksort, choosing one element as a pivot and partitioning the data in two based on the pivot, accordingly as less than or greater than the pivot.
    However, instead of recursing into both sides, as in quicksort, quickselect only recurses into one side – the side with the element it is searching for.
    This reduces the average complexity from O(n log n) to O(n), with a worst case of O(n2).
    You can think of quickselect as a partialsort sorting algorithm.

    This question basically tests your knowledge of sorting and selection algorithms.
    """
    dist = lambda index: points[index][0] ** 2 + points[index][1] ** 2

    def swap(x, y):
        points[x], points[y] = points[y], points[x]
        return

    def quick_select(low, high, kth):
        if low >= high:
            return

        mid = partition(low, high)

        if mid == kth:
            return
        elif mid < kth:
            quick_select(mid + 1, high, kth)
        else:
            quick_select(low, mid - 1, kth)

    def partition(low, high):
        pivot_index = random.randint(low, high)
        pivot_dist = dist(pivot_index)
        swap(high, pivot_index)  # put the pivot at the end of the array
        border = (
            low
        )  # every value to the right of border will be greater than the pivot; yes, this looks like an unnecessary variable but the name helps reinforce the purpose of this pointer

        for index in range(low, high + 1):
            current_dist = dist(index)
            if current_dist < pivot_dist:
                swap(index, border)
                border += 1

        swap(border, high)
        return border

    quick_select(0, len(points) - 1, kth)
    return points[:kth]
