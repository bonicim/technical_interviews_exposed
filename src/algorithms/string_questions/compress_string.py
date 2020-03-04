def compress_string(string):
    """
    Compress a string consisting of lowercase letters of the English alphabet by using the counts
    of repeated characters. For example, "aabcccccaaa" would be compressed to "a2b1c5a3".

    If the compressed string is not smaller than the original, return the original.
    """
    string_set = set(string)
    if len(string) == len(string_set):
        return string

    result = []
    current_char = string[0]
    count = 1

    for index in range(1, len(string)):
        char = string[index]
        if char == current_char:
            count += 1
        else:
            result.append(current_char)
            result.append(str(count))
            current_char = char
            count = 1

    result.append(current_char)
    result.append(str(count))

    compressed_string = "".join(result)

    if len(string) <= len(compressed_string):
        return string
    else:
        return compressed_string
