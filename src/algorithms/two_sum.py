'''
You are given an array of n integers and a number k. Determine whether there is a pair
of elements in the array that sums to exactly k. For example, given the array [1, 3, 7] and
k = 8, the answer is “yes,” but given k = 6 the answer is “no"
'''
def two_sum(n, k):
    """Returns true if the sum of two numbers in a list equals the target; false otherwise

    :param n: List of integers.
    :type n: list.
    :param k: The number of the sum of two numbers in arr.
    :type k: int.
    :returns: bool -- true or false 
    :raises: None

    """
    return two_sum_sort_binary_search_sol(n, k)

def two_sum_brute_force_sol(n, k):
    for i, val in enumerate(n):
        diff = k - val
        for j in range(i + 1, len(n)):
            if n[j] == diff:
                return True 
    return False

def two_sum_hash_sol(n, k):
    diffs = {}
    for i, val in enumerate(n):
        indexes = diffs.get(val)
        if indexes:
            indexes.add(i)
            diffs[val] = indexes
        else:
            diffs[val] = {i}

    for i, val in enumerate(n):
        diff = k - val
        indexes = diffs.get(diff) 
        if indexes and ( (i not in indexes) or (len(indexes) > 1) ):
            return True
    
    return False

def two_sum_sort_binary_search_sol(n, k):
    n_sorted = sorted(n)
    
    for i, val in enumerate(n):
        diff_idx = binary_search(0, len(n_sorted) - 1, k - val, n_sorted)
        if diff_idx >= 0:
            if (diff_idx != i or 
                    (i > 0 and (n_sorted[i - 1] == n_sorted[i])) or 
                    (i < len(n_sorted) - 1 and (n_sorted[i + 1] == n_sorted[i]))):
                return True        
    return False

def binary_search(start, end, tgt, n_sorted):
    while (start <= end):
        mid = int((start + end) / 2)
        if tgt < n_sorted[mid]:
            end = mid - 1
        elif tgt > n_sorted[mid]:
            start = mid + 1
        elif n_sorted[mid] == tgt:
            return mid
    return -1       


def two_sum_sort_walk_inward_sol(n, k):
    return