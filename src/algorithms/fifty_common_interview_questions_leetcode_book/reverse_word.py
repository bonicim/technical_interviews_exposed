def reverse_word(word):
    return reverse_word_v2(word)


def reverse_word_v1(word):
    words = word.split()
    words.reverse()

    result = ""
    for elem in words:
        result += elem
        result += " "

    return result[: len(result) - 1]


def reverse_word_v2(word):
    stack = []
    result = ""

    for index in range(len(word) - 1, -1, -1):
        letter = word[index]
        if letter.startswith(" "):
            if len(stack) > 0:
                for _ in range(len(stack)):
                    result += stack.pop()
                result += " "
        else:
            stack.append(letter)

    if len(stack) > 0:
        for _ in range(len(stack)):
            result += stack.pop()
        return result

    return result[: len(result) - 1]
