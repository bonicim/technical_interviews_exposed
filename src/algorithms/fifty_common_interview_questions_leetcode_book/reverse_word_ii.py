def reverse_word_ii(word):
    """ Given an input string , reverse the string word by word.

        Args:
            word (List of str): The list of individual characters composing a string.


        Returns:
            str. The reversed word

        Example:

        Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
        Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
    """
    return reverse_word_ii_v1(word)


def reverse_word_ii_v1(word):
    word.reverse()

    left = 0
    right = 0
    for index, letter in enumerate(word):
        if letter == " ":
            right = index
            word_slice = word[left:right]
            word_reversed = word_slice[::-1]
            word[left:right] = word_reversed
            left = index + 1
    right = len(word)
    word_slice = word[left:right]
    word_reversed = word_slice[::-1]
    word[left:right] = word_reversed

    return word
