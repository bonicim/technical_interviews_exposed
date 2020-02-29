def decode_ways(s):
    return recursive_top_down(s)
    # return bottom_up(s)


def recursive_top_down(s):
    def helper(s, pointer, cache):
        if pointer >= len(s):
            return 1

        if cache[pointer] > -1:
            return cache[pointer]

        decomp = 0
        for offset in range(1, 3):
            if pointer + offset <= len(s):
                substring = s[pointer : pointer + offset]

                if len(substring) > 0 and substring[0] != "0":
                    substring = int(substring)
                    if substring >= 1 and substring <= 26:
                        decomp += helper(s, pointer + offset, cache)

        cache[pointer] = decomp
        return cache[pointer]

    cache = [-1] * (len(s))
    return helper(s, 0, cache)


# def bottom_up(s):
