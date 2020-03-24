def get_shortest_unique_substring(arr, str):
    req_chars = set(arr)
    seen_chars = dict()

    required_total_chars = len(req_chars)
    current_seen_req_chars = 0

    min_len_so_far = len(str) + 1
    min_left = 0
    min_right = 0

    left = 0
    right = 0

    while right < len(str):
        char_right = str[right]
        seen_chars[char_right] = seen_chars.get(char_right, 0) + 1

        if char_right in req_chars and seen_chars.get(char_right) == 1:
            current_seen_req_chars += 1

        while current_seen_req_chars == required_total_chars and left <= right:
            current_window_size = right - left + 1
            if current_window_size < min_len_so_far:
                min_len_so_far = current_window_size
                min_left = left
                min_right = right + 1

            char_left = str[left]
            seen_chars[char_left] = seen_chars.get(char_left) - 1

            if char_left in req_chars and seen_chars[char_left] < 1:
                current_seen_req_chars -= 1

            left += 1

        right += 1

    return str[min_left:min_right]
