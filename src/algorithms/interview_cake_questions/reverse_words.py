"""
    Your team is scrambling to decipher a recent message, worried it's a plot to break into a major European National Cake Vault. The message has been mostly deciphered, but all the words are backward! Your colleagues have handed off the last step to you.

    Write a function reverse_words() that takes a message as a list of characters and reverses the order of the words in place.

    For example:

    message = [ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]

    reverse_words(message)

    # Prints: 'steal pound cake'
    print(''.join(message))

"""

""" Commentary

Reverser words is a difficult problem although it looks easy at first glance. The hard part about this problem is how to deal with spaces, especially multiple spaces.
How you deal with the space problem is related how well you optimize for space. For example, you can use a data structure such as a list or a stack to store the
characters in reversed order. But then you will have to deal with appending the space at the very end of the word when building the final result.

But if you think about the problem in terms of pointers to the start and end of a word within the string, then you don't have to deal with the problem
and the error prone issues of handling spaces. For example: "life is ball". In this example, simply have pointers to the start and end of each word and reverse
them, giving you "efil si llab". Then you take this string and then reverse the whole string giving you "ball is life". By focusing on pointers and changing the
string in place, you avoid appending spaces at the very end of words. By treating spaces as simply another character instead of a very special case, we arrive at both
a more efficient, elegant, readable, and less error prone solution.
"""


def reverse_words(message):
    return reverse_words_optimal(message)
    # return reverse_word_space_suboptimal(message)
    # return stack_solution(message)


def reverse_words_optimal(message):
    def swap_chars(left, right):
        while left < right:
            message[left], message[right] = message[right], message[left]
            left += 1
            right -= 1

    current_start = 0
    # we extend the counter to the last letter because we want to reverse the whole array in cases where the word is more than one letter.
    # In other words, by going all the way to the last letter, we ensure that we reverse the word
    # If we don't, then we will never reverse the word in the array, which is required for this solution.
    for current_end in range(len(message) + 1):
        if current_end == len(message) or message[current_end] == " ":
            swap_chars(current_start, current_end - 1)
            current_start = current_end + 1

    swap_chars(0, len(message) - 1)

    return "".join(message)


# TODO: fix solution
def stack_solution(message):
    def reverse_word(word, left, right):
        while left < right:
            word[left], word[right] = word[right], word[left]
            left += 1
            right -= 1
        return word

    stack = [char for char in message]

    word = []
    result = []
    while stack:
        char = stack.pop()
        if char == " ":
            # append word to the result array
            new_word = reverse_word(word, 0, len(word) - 1)
            for letter in new_word:
                result.append(letter)
            word = []
            result.append(" ")
        else:
            word.append(char)

    return "".join(result)


def reverse_word_space_suboptimal(message):
    def reverse_word(word, left, right):
        while left < right:
            word[left], word[right] = word[right], word[left]
            left += 1
            right -= 1
        return word

    reversed_message = [message[x] for x in range(len(message) - 1, -1, -1)]

    word = []
    result = []
    for index in range(len(reversed_message)):
        char = reversed_message[index]
        if char != " ":
            word.append(char)
        elif char == " ":
            new_word = reverse_word(word, 0, len(word) - 1)
            for letter in new_word:
                result.append(letter)
            result.append(" ")
            word = []

    if word:
        new_word = reverse_word(word, 0, len(word) - 1)
        for letter in new_word:
            result.append(letter)

    return "".join(result)
