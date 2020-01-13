"""
You are given an array of n integers and a number k. Determine whether there is a pair
of elements in the array that sums to exactly k. For example, given the array [1, 3, 7] and
k = 8, the answer is “yes,” but given k = 6 the answer is “no"
"""

"""Commentary
Every competent software engineer should complete this problem in blazing speed. This is a problem that will provide a lot
of information about the technical depth and skill of a candidate because this question has several possible solutions each with
its own pros and cons. An engineer should be able to implement the different solutions, analyze it in terms of time and space complexity,
and then be able to tweak the code if the requirements of the question change.

In this problem, the optimal solution is to a use a hashtable to find the other number that will equal to the sum. Although the hashtable
uses space of O(n), we get the benefit of an optimal time complexity: O(n). The brute force solution does not use space, but the time complexity
is bad: O(n^2). This is a common pattern in solving algorithm problems: using space complexity to improve time complexity. In general, you can't
have both the best space and time complexity--but not always.

Finally, this problem can also be solved using binary search. However it is not as optimal as the hashtable solution because sorting dominates
the time complexity at O(n log n).
"""


def two_sum(n, k):
    # return two_sum_hash_sol(n, k)
    return two_sum_hash_sol_v2(n, k)


def two_sum_brute_force_sol(n, k):
    for i, val in enumerate(n):
        diff = k - val
        for j in range(i + 1, len(n)):
            if n[j] == diff:
                return True
    return False


def two_sum_hash_sol(n, k):
    diffs = set()
    for val in n:
        if k - val in diffs:
            return True
        diffs.add(val)
    return False


def two_sum_hash_sol_v2(nums, target):
    """
    This solution keeps track of the indexes of the two pairs if found
    """
    complements = dict()
    for index, num in enumerate(nums):
        complement = target - num
        if complement in complements:
            complement_indexes = complements.get(complement)
            indexes = [index, complement_indexes.pop()]
            print(f"Indexes of target: {indexes}")
            return True
        complements.update({num: set([index])})
    return False


# only shown for educational purposes and to talk about different solutions
def two_sum_sort_binary_search_sol(n, k):
    def binary_search(start, end, tgt, n_sorted):
        while start <= end:
            mid = int((start + end) / 2)
            if tgt < n_sorted[mid]:
                end = mid - 1
            elif tgt > n_sorted[mid]:
                start = mid + 1
            elif n_sorted[mid] == tgt:
                return mid
        return -1

    n_sorted = sorted(n)

    for i, val in enumerate(n):
        diff_idx = binary_search(0, len(n_sorted) - 1, k - val, n_sorted)
        if diff_idx >= 0:
            if (
                diff_idx != i
                or (i > 0 and (n_sorted[i - 1] == n_sorted[i]))
                or (i < len(n_sorted) - 1 and (n_sorted[i + 1] == n_sorted[i]))
            ):
                return True
    return False


# only shown for educational purposes and to talk about different solutions
# this solution runs in n log n due to the sorting algorithm
def two_sum_sort_walk_inward_sol(n, k):
    n_sorted = sorted(n)
    lhs = 0
    rhs = len(n_sorted) - 1

    while lhs < rhs:
        sum = n_sorted[lhs] + n_sorted[rhs]
        if sum == k:
            return True
        elif sum > k:
            rhs -= 1
        else:
            lhs += 1

    return False
