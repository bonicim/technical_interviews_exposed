"""
Write a function that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.

A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.
Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].
The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

In other words, it is the absolute difference between the sum of the first part and the sum of the second part.
For example, consider array A such that:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
We can split this tape in four places:

P = 1, difference = |3 − 10| = 7
P = 2, difference = |4 − 9| = 5
P = 3, difference = |6 − 7| = 1
P = 4, difference = |10 − 3| = 7
"""


def get_min_from_tape(arr):
    size = len(arr)
    total = sum(arr)
    left_sum = [None] * size
    left_sum[len(left_sum) - 1] = 0

    for index in range(len(left_sum)):
        left_sum[index] = left_sum[index - 1] + arr[index]

    min = total
    for index in range(len(arr)):
        curr_min = abs(left_sum[index] - (total - left_sum[index]))
        if curr_min < min:
            min = curr_min

    return min
