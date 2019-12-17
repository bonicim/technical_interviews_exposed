"""
Given a list of words, group the words by anagrams and return a list of sets of anagrams.

Example:

["cat", "dog", "god"] = > [ {"cat"}, {"dog", "god"} ]
"""


def group_anagrams(words):
    return get_list_anagrams_v1(words)


def get_list_anagrams_v2(words):
    """
    The solution is the same as v1 but is less verbose and takes advantage of setdefault method
    """
    anagram_groups = {}
    for word in words:
        group = anagram_groups.setdefault("".join(sorted(list(word))), set([word]))
        group.add(word)

    return list(anagram_groups.values())


def get_list_anagrams_v1(words):
    anagram_groups = {}
    for word in words:
        sorted_word = "".join(sorted(word))
        if sorted_word in anagram_groups:
            group = anagram_groups.get(sorted_word)
            group.add(word)
            anagram_groups.update({sorted_word: group})
        else:
            anagram_groups[sorted_word] = set([word])

    return list(anagram_groups.values())
