def find_rotation_point(words):
    """
    I opened up a dictionary to a page in the middle and started flipping through, looking for words I didn't know. I put each word I didn't know at increasing indices in a huge list I created in memory. When I reached the end of the dictionary, I started from the beginning and did the same thing until I reached the page I started at.

    Now I have a list of words that are mostly alphabetical, except they start somewhere in the middle of the alphabet, reach the end, and then start from the beginning of the alphabet. In other words, this is an alphabetically ordered list that has been "rotated." For example:

    words = [
        'ptolemaic',
        'retrograde',
        'supplant',
        'undulate',
        'xenoepist',
        'asymptote',  # <-- rotates here!
        'babka',
        'banoffee',
        'engender',
        'karpatka',
        'othellolagkage',
    ]

    Write a function for finding the index of the "rotation point," which is where I started working from the beginning of the dictionary. This list is huge (there are lots of words I don't know) so we want to be efficient here.
    """
    first_word = words[0]
    left_index = 0
    right_index = len(words) - 1

    while left_index < right_index:
        distance_to_mid_index = (right_index - left_index) // 2
        mid_index = left_index + distance_to_mid_index

        guess_word = words[mid_index]

        if guess_word >= first_word:
            left_index = mid_index
        else:
            right_index = mid_index

        if right_index - left_index == 1:
            return right_index
