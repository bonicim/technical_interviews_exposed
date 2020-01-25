"""Reverse bits of a given 32 bits unsigned integer.

Example 1:

Input: 00000010100101000001111010011100
Output: 00111001011110000010100101000000
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
Example 2:

Input: 11111111111111111111111111111101
Output: 10111111111111111111111111111111
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.
"""


""" Commentary

This is a basic bit manipulation problem to show how well you know bit manipulation and low level
operations. Here we need to know several basics about bit manipulation.

First, if we want to grab the value of a bit we can simply do: &1
Second, if want to shift a binary to the left or right we simply do: <<=n for left and >>n for right, where n is the number of shifts to make
Finally, if we want to insert a bit at the far right, we simply do: |n, where n is the value of the bit, either 0 or 1

The algorithm is quite simple, iterate through the binary starting from the right side, then append
each bit in a collector.

"""


def reverseBits(n):
    ans = 0

    for _ in range(32):
        rightmost_bit = n & 1  # grab the rightmost bit
        ans <<= 1  # shift the ans to the left to make room for the captured bit
        ans |= rightmost_bit  # insert the bit into the answer
        n >>= 1  # shift the number to the right

    return ans
