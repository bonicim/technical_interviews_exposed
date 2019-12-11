def word_cloud(input_string):
    words = split_words(input_string)

    words_count = {}

    for word in words:
        if word in words_count:
            count = words_count.get(word)
            count += 1
            words_count.update({word: count})

        elif word.lower() in words_count:
            word_lowercase = word.lower()
            count = words_count.get(word_lowercase)
            count += 1
            words_count.update({word_lowercase: count})

        elif word.capitalize() in words_count:
            word_capitalized = word.capitalize()
            count = words_count.get(word_capitalized)
            count += 1
            words_count.update({word: count})
            del words_count[word_capitalized]

        else:
            words_count.update({word: 1})
    return words_count


# TODO: This is a problem in itself. Write tests for each case.
def split_words(input_string):
    def end_of_string(index):
        return index == len(input_string) - 1

    def end_word(char):
        return char == " " or char == "\u2014"

    def ellipses(index, char):
        return (
            char == "."
            and index + 2 <= len(input_string)
            and input_string[index + 1] == "."
            and input_string[index + 2] == "."
        )

    def alpha_or_apostrophe(char):
        return char.isalpha() or char == "'"

    def hyphen(char):
        return char == "-"

    def surrounded_by_letters(index):
        return (
            index > 0
            and input_string[index - 1].isalpha()
            and input_string[index + 1].isalpha()
        )

    words = []
    start = 0
    size = 0

    for index, char in enumerate(input_string):
        if end_of_string(index):
            if char.isalpha():
                size += 1
            if size > 0:
                word = input_string[start : start + size]
                words.append(word)

        elif end_word(char):
            if size > 0:
                word = input_string[start : start + size]
                words.append(word)
                size = 0

        elif ellipses(index, char):
            if size > 0:
                word = input_string[start : start + size]
                words.append(word)
                size = 0

        elif alpha_or_apostrophe(char):
            if size == 0:
                start = index
            size += 1

        elif hyphen(char):
            if surrounded_by_letters(index):
                if size == 0:
                    start = index
                size += 1
            elif size > 0:
                word = input_string[start : start + size]
                words.append(word)

    return words
