from collections import Counter
import string

"""Commentary

Similar to character count engine, except that we are dealing with words and more importantly,
the output is a list of list of word to count pairs in descending order and in the order that the
words appear from the original input.

The key part is breaking this problem into smaller pieces, i.e. splitting the strings,
removing punctuation, lowercasing all letters, and putting the words in descending order.

The hardest portion is sorting the words in descending order and in the order it originally
appeared in the input.

Sorting can be done using bucket sort or using a sorting algorithm on the dictionary.

The output must also be handled carefully to ensure that the words appear in the order that
it appeared in the original input. This order can be maintained if the data strucure to hold
the frequency count of words is an ordered dictionary or a linked list hashmap.

"""


def word_count_engine(str_input):
    words = split_strings(str_input)
    words = remove_punctuation(words)
    freqs = make_word_freqs(words)
    result = sort_freqs(freqs)
    return result


def split_strings(str_input):
    words = str_input.split()
    return [word.lower() for word in words]


def remove_punctuation(words):
    result = []
    punc = set(string.punctuation)
    for word in words:
        updated_word = [char for char in word if char not in punc]
        result.append("".join(updated_word))
    return result


def make_word_freqs(words):
    return Counter(words)


def sort_freqs(freqs):
    # use a variation of bucketsort to place same count items
    # create an array of the size of the most frequently occurring word
    count_most_frequent = freqs.most_common(1)[0][1] + 1
    bucket_words = [None] * (count_most_frequent)
    for word, count in freqs.items():
        if not bucket_words[count]:
            bucket_words[count] = []
        alist = bucket_words[count]
        alist.append(word)
        bucket_words[count] = alist

    # build the result in descending order by going backwards on the array of array of words, bucket_words
    result = []
    for count in range(count_most_frequent - 1, -1, -1):
        words_list = bucket_words[count]
        # if we have words for this count, then put it in the list
        if words_list:
            for _, word in enumerate(words_list):
                result.append([word, str(count)])

    return result
