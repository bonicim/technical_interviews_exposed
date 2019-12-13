import random


def find_repeat(nums):
    """
    We have a list of integers, where:

    The integers are in the range 1..n
    The list has a length of n+1
    It follows that our list has at least one integer which appears at least twice. But it may have several duplicates, and each duplicate may appear more than twice.

    Write a function which finds an integer that appears more than once in our list. (If there are multiple duplicates, you only need to find one of them.)
    """
    # return set_solution(nums)
    # return brute_force_solution(nums)
    # return sort_in_place_solution(nums)
    return binary_search_modified_solution(nums)


def set_solution(nums):
    # O(n) time, O(n) space
    nums_seen = set()

    for num in nums:
        if num in nums_seen:
            return num
        else:
            nums_seen.add(num)

    raise Exception("No duplicates found. Input list must have at least one duplicate.")


def brute_force_solution(numbers):
    # O(n^2) time, O(1) space
    for target in range(1, len(numbers)):
        has_seen = False
        for num in numbers:
            if num == target:
                if has_seen:
                    return num
                else:
                    has_seen = True

    raise Exception("No duplicates found. Input list must have at least one duplicate.")


def sort_in_place_solution(nums):
    # O(nlogn) time, O(1) space; however, the input is mutated, potentially causing side-effects for other programs using that input
    def partition(arr, low, high):
        border = low
        pivot_index = random.randint(low, high)
        pivot = arr[pivot_index]

        for index in range(low, high):
            if arr[index] <= pivot:
                arr[border], arr[index] = arr[index], arr[border]
                border += 1
        arr[border], arr[high] = arr[high], arr[border]
        return border

    def quicksort(arr, low, high):
        if low < high:
            partition_index = partition(arr, low, high)

            quicksort(arr, low, partition_index - 1)
            quicksort(arr, partition_index + 1, high)

    quicksort(nums, 0, len(nums) - 1)

    for index, num in enumerate(nums):
        if index + 1 == len(nums):
            raise Exception(
                "No duplicates found. Input list must have at least one duplicate."
            )
        if num == nums[index + 1]:
            return num


def binary_search_modified_solution(nums):
    """O(nlogn) time, O(1) space; this is the most complex but optimal answer

    Algorithm:

    Step 1: Count the number of integers from the input list that are in the range 1...n/2
    Step 2: Compare that number to the number of unique integers in range 1...n/2
    Step 3: If the number of integers in the range of 1..n/2 from the input list is greater than the number of unique integers from range 1..n/2,
    that range has the duplicate integer by dint of the Pigeonhole principle. Repeat the same process on that range, updating the low and high value appropriately.
    Step 4: If not, then the duplicate is on the other half of the range n/2 + 1...n. Use the same approach on that range.
    Step 5: At some point, the algorithm will converge on a range of 1 item. That is the duplicated number and is the answer.
    """
    floor = 1
    ceiling = len(nums) - 1

    while floor < ceiling:
        midpoint = floor + ((ceiling - floor) // 2)
        floor_low_range = floor
        ceiling_low_range = midpoint
        floor_high_range = midpoint + 1
        ceiling_high_range = ceiling

        count_elements_floor_low_range = 0
        for num in nums:
            if floor_low_range <= num <= ceiling_low_range:
                count_elements_floor_low_range += 1

        count_unique_elements_low_range = ceiling_low_range - floor_low_range + 1
        if count_elements_floor_low_range > count_unique_elements_low_range:
            floor = floor_low_range
            ceiling = ceiling_low_range
        else:
            floor = floor_high_range
            ceiling = ceiling_high_range

    return floor
