def is_anagram(w1, w2):
    return is_anagram_brute_force(w1, w2)
    # return is_anagram_sort(w1, w2)
    # return is_anagram_count_char(w1, w2)
    # return is_anagram_histograms(w1, w2)

def is_anagram_brute_force(w1, w2):
    # returns a set of all permutations of a word
    # TODO: implement Heap algorithm
    def permutate(w1):
        return
    
    w1_permutations = permutate(w1)
    w2_permutations = permutate(w2)

    return w1_permutations == w2_permutations 

def is_anagram_sort(w1, w2):
    letters_1 = sorted(list(w1))
    letters_2 = sorted(list(w2))

    return letters_1 == letters_2

def is_anagram_count_char(w1, w2):
    counts_w1 = {}
    for letter in list(w1):
        counts_w1[letter] = counts_w1.get(letter, 0) + 1
    counts_w2 = {}
    for letter in list(w2):
        counts_w2[letter] = counts_w2.get(letter, 0) + 1

    return counts_w1 == counts_w2

def is_anagram_histograms(w1, w2):
    counts_w1 = {}
    for letter in list(w1):
        counts_w1[letter] = counts_w1.get(letter, 0) + 1
    for letter in list(w2):
        if letter not in counts_w1:
            return False
        else:
            counts_w1[letter] = counts_w1.get(letter) - 1
    
    return sum(counts_w1.values()) == 0        