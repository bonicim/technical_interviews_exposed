def contains_vowel(arr):
    # return contains_vowel_iterative_solution(arr)
    return contains_vowel_recursive_solution(arr)


def contains_vowel_iterative_solution(arr):
    vowel = ["a", "e", "i", "o", "u"]
    if arr == []:
        return False
    for word in arr:
        for letter in word:
            if letter in vowel:
                return True
    return False


def contains_vowel_recursive_solution(arr):
    vowels = ["a", "e", "i", "o", "u"]
    if not arr:
        return False
    word = arr[0]
    for letter in word:
        if letter in vowels:
            if len(arr) == 1:
                return True
            return True and contains_vowel_recursive_solution(arr[1:])
    return False
