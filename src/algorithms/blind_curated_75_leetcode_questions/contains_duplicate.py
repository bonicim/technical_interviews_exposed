"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
"""

""" Commentary

Easy question that tests your ability to solve a question in many different ways. When I hear duplicates,
I immediately think of using sets to filter out duplicates. Or using a hash table to count frequencies.

The clever one line solution is to put the list into a set and compare if the sizes of the set and the original
list are equal.

Another way is to build a hash table as you iterate through the list. Check the hash table for each item.
If item was already in the hash table, that is a duplicate.

"""


def contains_duplicate(nums):
    return len(nums) != len(set(nums))


def contains_duplicate_iterative(nums):
    visited = dict()

    for num in nums:
        count = visited.get(num, 0)
        if count:
            return True
        visited.update({num: count + 1})
    return False
