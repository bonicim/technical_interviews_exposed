def is_palindrome(string):
    # return is_palindrome_walk_inward(string)
    return is_palindrome_recursive_solution(string, 0, len(string) - 1)


def is_palindrome_recursive_solution(string, left_index, right_index):
    if len(string) == 0 or left_index == right_index or left_index > right_index:
        return True

    string = string.lower()
    left_char = string[left_index]
    right_char = string[right_index]

    while not left_char.isalnum() and left_index < right_index:
        left_index += 1
        left_char = string[left_index]
    if not left_char.isalnum():
        left_char = ""

    while not right_char.isalnum():
        if right_index == 0:
            break
        right_index -= 1
        right_char = string[right_index]
    if not right_char.isalnum():
        right_char = ""

    if left_char != right_char:
        return False

    return is_palindrome_recursive_solution(string, left_index + 1, right_index - 1)


def is_palindrome_walk_inward(string):
    alphanum = set()
    for i in range(10):
        alphanum.add(str(i))
    for i in range(ord("a"), ord("z") + 1):
        alphanum.add(chr(i))

    # yes, I could have used the builtin function isalnum but I wanted to implement my version simply for learning
    def next_alphanumeric_character(string, index, start_from_left=True):
        char = string[index]
        if start_from_left:
            while char not in alphanum and index < len(string) - 1:
                index += 1
                char = string[index]
        else:
            while char not in alphanum and index >= 0:
                index -= 1
                char = string[index]

        if not char.isalnum():
            char = ""

        return string[index], index

    left = 0
    right = len(string) - 1
    string = string.lower()

    while left < right:
        left_char, left = next_alphanumeric_character(string, left)
        right_char, right = next_alphanumeric_character(
            string, right, start_from_left=False
        )
        if left_char == right_char:
            left += 1
            right -= 1
        else:
            return False
    return True
