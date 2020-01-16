import math

"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

"""Commentary

This is a classic yet easy problem that demonstrates your understanding of recursion, memoization, pruning,
dynamic programming, and fibonacci's sequence.

The best way to really understand this problem is to draw the complete recursion tree. Only then will you be able to
see the inefficiency of the brute force solution and how it can be optimized using memoization or dynamic programming.

Look at the recursion tree when trying to climb a stairs of three steps. Notice how the leaves of the tree are the possible
paths or ways of climbing the stairs. That is the answer. Then notice how there's some repetitive calculations being
made on the tree. Memoization will prune the tree by recording the result and not having use redo the same call.

Notice that we have a lot of sub problems being created by recursion. This is a good hint that we could use dynamic programming
to build our answer from the bottom up instead of top down. Imagine we were on some step. Let's call it step 6. To get
to step 6 we can take either 1 step starting from step 5 or 2 steps starting from step 4. Now, ask yourself, how many ways can I get to
step 5? And step 4? If I knew that information, then I know how many total ways to get to step 6. Why?
Because once I know all the possibilities of getting to step 5, then I can get to step 6 with one step. And once I
know all the possibilities of getting to step 4, that I can get to step 6 with two steps. Thus, we've solved
our problem by solving sub-problems of that problem and using it to solve the more global problem.

This is dynamic programming (bottom up) at its essence. Understand this deeply and then you will be ready to move on to
harder problems.
"""


def climb_stairs(n):
    brute_force(0, n)


def brute_force(current, n):
    if current == n:
        return 1

    if current > n:
        return 0

    return brute_force(current + 1, n) + brute_force(current + 2, n)


def top_down_memoization(current, n, memo=None):
    if not memo:
        memo = [0] * len(n)

    if current == n:
        return 1

    if current > n:
        return 0

    # We've already calculated this sub problem; no need to do it again
    if memo[n] > 0:
        return memo[n]

    memo[n] = top_down_memoization(current + 1, n, memo) + top_down_memoization(
        current + 2, n, memo
    )
    return memo[n]


def rule_of_sum_dynamic_programming_solution(n):
    if n == 1:
        return 1

    cache = [0] * (n + 1)
    cache[1] = 1
    cache[2] = 2

    for step in range(3, n + 1):
        cache[step] = cache[step - 1] + cache[step - 2]
    return cache[n]


def fibonacci_algorithm_no_space(n):
    if n == 1:
        return 1
    first = 1
    second = 2

    for _ in range(3, n + 1):
        third = second + first
        first = second
        second = third

    return second
