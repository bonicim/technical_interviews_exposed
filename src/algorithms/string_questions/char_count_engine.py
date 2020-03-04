from collections import Counter

"""
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

"""

"""Commentary
Though it appears easy, the crux of this problem is how to sort the letters
in descending order and then print out the result. There are two main ways to sort the
frequency table:

1) Use bucket sort
2) Sort the freq table using some sorting algo: sorted

"""


def char_count_engine(word):
    return bucket_sort_solution(word)


def bucket_sort_solution(word):
    if not len(word):
        return ""

    freqs = Counter(word)
    highest_freq = freqs.most_common(1)[0][1] + 1
    chars_list = [None] * highest_freq

    for char, count in freqs.items():
        if not chars_list[count]:
            chars_list[count] = []
        chars_list[count].append(char)

    result = ""
    for count in range(highest_freq - 1, -1, -1):
        chars_coll = chars_list[count]
        if chars_coll:
            for _, char in enumerate(chars_coll):
                for _ in range(count):
                    result += char

    return result
