"""Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""

""" Commentary

The key to this problem is setting pointers on the left and right sides and then
itertating through the string to test certain conditions. In this case, if the letter doesn't match
on the left and right side, then we return False. Other wise we continue moving inwards toward the middle.
If it all matches, then we simply return True.

The trick in this question is that spaces, non-alphanumeric characters are ignored and are not considered
part of the string. So we ignore them. Thus we must validate those special cases first and skip those characters
and not let it be under consideration.
"""


def isPalindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if not s[left].isalnum():
            left += 1
            continue
        if not s[right].isalnum():
            right -= 1
            continue
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1

    return True


def is_palindrome_recursive_solution(string, left_index, right_index):
    if len(string) == 0 or left_index == right_index or left_index > right_index:
        return True

    left_char = string[left_index]
    right_char = string[right_index]

    while not left_char.isalnum() and left_index < right_index:
        left_index += 1
        left_char = string[left_index]
    while not right_char.isalnum():
        if right_index == 0:
            break
        right_index -= 1
        right_char = string[right_index]
    if left_char.isalnum() and right_char.isalnum():
        if left_char.lower() != right_char.lower():
            return False
    return is_palindrome_recursive_solution(string, left_index + 1, right_index - 1)
