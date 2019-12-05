def reverse_words(message):
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

    def reverse_chars(left, right):
        while left < right:
            message[left], message[right] = message[right], message[left]
            left += 1
            right -= 1

    current_start = 0

    for current_end in range(len(message) + 1):

        if current_end == len(message) or message[current_end] == " ":
            reverse_chars(current_start, current_end - 1)
            current_start = current_end + 1

    reverse_chars(0, len(message) - 1)

    return "".join(message)
