def length_of_longest_substring(string):
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

    left = 0
    right = 0
    max_len = 0
    unique_chars = set()
    substring = ""

    while right < len(string):
        char = string[right]

        if char not in unique_chars:
            unique_chars.add(char)
            if max_len < len(unique_chars):
                max_len = len(unique_chars)
                substring = string[left : right + 1]
            right += 1

        else:
            unique_chars.remove(string[left])
            left += 1

    print(substring)

    return max_len
