def str_str(haystack, needle):
    """Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

    Args:
        haystack (str): The string in which the search will take place.
        needle (str): The string to search for in the haystack.

    Returns:
        int. The index of the first occurence of needle in haystack; otherwise, -1

    Example 1:

    Input: haystack = "hello", needle = "ll"
    Output: 2

    Example 2:

    Input: haystack = "aaaaa", needle = "bba"
    Output: -1
    """
    if not needle:
        return 0

    if len(needle) > len(haystack):
        return -1

    for haystack_index in range(len(haystack)):
        haystack_slice = haystack[haystack_index : haystack_index + len(needle)]
        if haystack_slice == needle:
            return haystack_index

    return -1
