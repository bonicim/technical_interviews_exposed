"""You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
"""

""" Commentary

The brute force solution would be to calculate every permutation of houses to rob without alerting the police and find the one with the
highest amount of money. But that would be inefficient.

A better way to think about this problem is to start with sub problems, mainly asking yourself what if there were only one house, two houses, and then three houses.
Going through those examples will reveal the logic needed to solve this problem efficiently, using Dynamic Programming.

With one house, we simply return the value of that house.
With two houses, we simply return the highest of the two houses.
With three houses, we have to make a choice: we can take the money in the third house and the first house OR we can take the money in the second house, whichever is larger.

Now imagine if we had ten houses. And we were on house number 5, deciding whether to rob it. How do we reason about it? Well, we ask ourselves, should I rob the
current house and the house two doors down from me OR do I simply rob the house one door down? Recall that I already have information about the maximum amount of
money I can steal in the previous 4 houses because I already solved those sub problems (i.e. bottom up solution). Thus we can generalize the logic of getting the most
money at any house by the following:

max ( current_house + house_two_away, previous_house)

This DP, bottom up solution prevents calculating the same permutation of houses in the brute force solution. It runs in O(n) run and space time complexity.
"""


def rob(nums):
    if not nums:
        return 0

    if len(nums) == 1:
        return nums[0]

    if len(nums) == 2:
        return max(nums[0], nums[1])

    cache = [0] * (len(nums))

    cache[0] = nums[0]
    cache[1] = max(nums[1], cache[0])

    for index in range(2, len(nums)):
        cache[index] = max(nums[index] + cache[index - 2], cache[index - 1])

    return cache[len(nums) - 1]
