"""
Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).



Example 1:

Input: 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
Example 2:

Input: 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
Example 3:

Input: 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
"""


""" Commentary

Again, this problem tests you bit manipulation skills. In this case, the bit mask. We can use the
bit mask to grab the least significant bit and determine if it is a 1. If so, increase our counter.
Then shift the mask to the right to check the next digit. We know that the digit is 32 bits long,
so we iterate 32 times to check each bit. Very straightforward solution.

Another way to solve this, perhaps faster, is using a bit manipulation trick, namely the idea that
doing an AND operation between a number n and n - 1 will flip the least significant 1-bit to a zero.
Knowing this, we simply set up a while loop on the number, increase our counter, flip the least significant
1-bit to 0, and then repeat until all the 1's are zeroes and thus the number is zero. This avoids
visiting every bit and instead just targets the 1 bits.

"""


def hammingWeight(n):
    mask = 1
    bits = 0
    for _ in range(32):
        # check if the current position has a 1, if so, add to our counter
        if n & mask != 0:
            bits += 1
        # shift the mask to the right by 1 to go to the next least significant digit
        mask <<= 1
    return bits


def bit_manipulation(n):
    bits = 0
    while n != 0:
        bits += 1
        n = n & (
            n - 1
        )  # The Crux is that for any number n, when doing an AND operation with n and n-1, it flips the least significant 1-bit to 0

    return bits
