def word_break(s, wordDict):
    return bottom_up_solution(s, wordDict)


def bottom_up_solution(s, wordDict):
    cache = [False] * (len(s) + 1)
    cache[0] = True

    for index in range(len(s)):
        for j in range(index, len(s)):
            if cache[index] and s[index : j + 1] in wordDict:
                cache[j + 1] = True

    return cache[len(s)]
