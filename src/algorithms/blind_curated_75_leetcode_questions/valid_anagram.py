"""
Given two strings s and t , write a function to determine if t is an anagram of s.
"""

""" Commentary

Anagram tests your understaning of using properties of inputs to solve a problem and using certain sorting
algorithms to solve this problem.

Here we care about whether the letters of two words are the same. There are different approaches to checking for
this type of equality. We can sort the letters of each word and compare. Sorting takes nlogn time.

We can also build a dictionary of frequencies of each letter of each word and then compare those dictionaries.
That would take N run and space time.
"""


def is_anagram(s, t):
    t_sorted = sorted(t)
    s_sorted = sorted(s)

    return t_sorted == s_sorted


def is_anagram_dictionary(s, t):
    tdict = dict()
    sdict = dict()

    for letter in s:
        count = sdict.get(letter, 0)
        sdict.update({letter: count + 1})

    for letter in t:
        count = tdict.get(letter, 0)
        tdict.update({letter: count + 1})

    return tdict == sdict
