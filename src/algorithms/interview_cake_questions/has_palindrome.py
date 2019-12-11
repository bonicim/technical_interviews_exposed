def has_palindrome(string):
    """
    Write an efficient function that checks whether any permutation of an input string is a palindrome.

    You can assume the input string only contains lowercase letters.

    Examples:

    "civic" should return True
    "ivicc" should return True
    "civil" should return False
    "livci" should return False
    """
    unpaired_chars = set()

    for char in string:
        if char not in unpaired_chars:
            unpaired_chars.add(char)
        else:
            unpaired_chars.remove(char)

    return len(unpaired_chars) <= 1
