def remove_three_consecutive_characters(word):
    if len(word) == 0:
        return 0

    min_changes = 0
    current_char_count = 1
    prev_char = word[0]

    for index in range(1, len(word)):
        curr_char = word[index]

        if curr_char != prev_char:
            current_char_count = 1
            prev_char = curr_char
        else:
            current_char_count += 1
            if current_char_count % 3 == 0:
                min_changes += 1
                current_char_count = 0
            else:
                continue

    return min_changes
