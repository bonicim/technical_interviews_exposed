def is_palindrome(string):
    return is_palindrome_helper(string, 0, len(string) - 1)


def is_palindrome_helper(string, left_index, right_index):
    if len(string) == 0 or left_index == right_index:
        return True
    if string[left_index] != string[right_index]:
        return False
    return is_palindrome_helper(string, left_index + 1, right_index -1)