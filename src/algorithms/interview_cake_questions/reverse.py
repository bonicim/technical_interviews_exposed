def reverse(chars):
    """
    Write a function that takes a list of characters and reverses the letters in place. ↴
    """

    def swap(index1, index2):
        chars[index1], chars[index2] = chars[index2], chars[index1]

    left = 0
    right = len(chars) - 1

    while left < right:
        swap(left, right)
        left += 1
        right -= 1

    return chars
