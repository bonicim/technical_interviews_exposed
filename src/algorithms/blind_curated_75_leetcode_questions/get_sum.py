"""
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = -2, b = 3
Output: 1
"""

""" Commentary

This problem tests your skills in binary manipulation. If you don't know and understand the following
bit manipulations, then you could not answer this question.

First, the sum of any two bits is the XOR operation: a ^ b
Second, the carry of any two bits that are being added is found by the AND operation: a & b
Third, shifting a bit to the left requires the following: j << n, where n is the number of shifts to the left.

To add two binary numbers, we need to be mindful of the carryover. That is the key part. We keep adding the bits
until there is nothing left to carryover. If we had two binaries that never had a carry, then this
would only enter the while loop one time.

"""


def get_sum(a: int, b: int):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1

    return a
