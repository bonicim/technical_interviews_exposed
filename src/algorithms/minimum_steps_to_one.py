""" Problem
On a positive integer, you can perform any one of the following 3 steps.
1.) Subtract 1 from it. ( n = n – 1 )  ,
2.) If its divisible by 2, divide by 2. ( if n % 2 == 0 , then n = n / 2  )  ,
3.) If its divisible by 3, divide by 3. ( if n % 3 == 0 , then n = n / 3  ).

Given a positive integer n, find the minimum number of steps that takes n to 1.

Examples:

For n = 1 , output: 0

For n = 4 , output: 2  ( 4  /2 = 2  /2 = 1 )

For n = 7 , output: 3  (  7  -1 = 6   /3 = 2   /2 = 1 )

"""
from time import process_time


def minimum_steps_to_one(n):
    t = process_time()

    # return memoization_top_down_approach(n)
    # return recusive_approach(n)
    # return greedy_approach(n)
    result = tabulation_bottom_up(n)
    elapsed_time = process_time() - t

    print(elapsed_time)
    return result


# shown here for instructional purposes
# fails when n = 10
def greedy_approach(n):
    if n == 1:
        return 0

    if n % 3 == 0:
        return 1 + greedy_approach(n // 3)
    elif n % 2 == 0:
        return 1 + greedy_approach(n // 2)
    else:
        return 1 + greedy_approach(n - 1)


# shown here for instructional purposes
# fails when n = 1000 because the function will exceed the call stack limit,
# resulting in RecursionError: maximum recursion depth exceeded in comparison
def recusive_approach(n):
    if n == 1:
        return 0

    min_steps = 1 + recusive_approach(n - 1)

    if n % 3 == 0:
        steps = 1 + greedy_approach(n // 3)
        min_steps = min(min_steps, steps)
    if n % 2 == 0:
        steps = 1 + greedy_approach(n // 2)
        min_steps = min(min_steps, steps)

    return min_steps


# shown here for instructional purposes
# fails when n = 1000 because the function will exceed the call stack limit,
# resulting in RecursionError: maximum recursion depth exceeded in comparison
def memoization_top_down_approach(n, cache=None):
    if cache == None:
        cache = [None] * (n + 1)
        cache[1] = 0

    if cache[n] is not None:
        return cache[n]

    min_steps = 1 + memoization_top_down_approach(n - 1, cache)
    cache[n] = min_steps

    if n % 3 == 0:
        steps = 1 + memoization_top_down_approach(n // 3, cache)
        min_steps = min(min_steps, steps)
    if n % 2 == 0:
        steps = 1 + memoization_top_down_approach(n // 2, cache)
        min_steps = min(min_steps, steps)

    cache[n] = min_steps

    return min_steps


def tabulation_bottom_up(n):
    cache = [0] * (n + 1)

    for index in range(2, (n + 1)):
        min_steps = 1 + cache[index - 1]
        if index % 3 == 0:
            steps_min = 1 + cache[index // 3]
            min_steps = min(min_steps, steps_min)
        if index % 2 == 0:
            steps_min = 1 + cache[index // 2]
            min_steps = min(min_steps, steps_min)
        cache[index] = min_steps

    return cache[n]
