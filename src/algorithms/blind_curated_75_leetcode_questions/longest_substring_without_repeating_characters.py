"""
    Given a string, find the length of the longest substring without repeating characters.

    Example 1:

    Input: "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.
    Example 2:

    Input: "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.
    Example 3:

    Input: "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


"""Commentary

Although this problem hints at dynamic programming, a simpler way to think about this problem is to use a technique
called the sliding window, in which you have two pointers that specify the range of a subset of items you are looking at
within an array. In combination with using a collection to determine if you've seen a char before (i.e. to track history),
the solution becomes fairly simple: if we've seen the character before, remove it from our seen list and move our left pointer.
If we have not seen it, then we have increased our longest substring. Add that to our list of seen characters, update our maximum unique substring, and move the pointer to the right.
A downside of this solution is that we don't move our right pointer continuously. When we encounter a duplicate, we revisit the right pointer
again.
"""


def length_of_longest_substring(string):
    left = 0
    right = 0
    max_so_far = 0
    unique_chars = set()
    substring = ""

    while right < len(string):
        char = string[right]

        if char not in unique_chars:
            unique_chars.add(char)

            if max_so_far < len(unique_chars):
                # we have found a new, longest substring
                max_so_far = len(unique_chars)
                substring = string[left : right + 1]

            right += 1
        else:
            # we remove the duplicated char in the our set of seen unique chars, but we don't move the right pointer forward because we need to include that char, which was duplicated from an earlier same char.
            unique_chars.remove(string[left])
            # instead of moving the right pointer, we simply move the left pointer forward
            # if the duplicated char was on the left pointer, then we have a new, albeit same length substring of left+1 to right
            # if not, then the duplicate must be somewhere in the middle of the current substring. on the next iteration, we'll eventually add the duplicated char back to the set
            left += 1

    print(substring)

    return max_so_far
