from collections import Counter

"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
"""

""" Commentary

This problem is hard because you are juggling many counters and maps to keep track of where you've been and how many
characters you have seen. The search entire string solution requires three categories of data:

First, you need a frequency table of required characters and another frequency table of characters already seen in the current window.

Second, you need the total number of unique characters that you need to find. Then you also need the current total number of unique characters
that have already been seen in the current substring. Note that this counter will be updated once the count of a unique characters in a substring
matches the total required count.

Third, you need a current minimum window length counter. This will help find the smallest window that seen in the search string.
You will also need to keep track of the left and right pointers of the current minimum window so that you can create the final substring.

Fourth, you need pointers for the window itself. The sliding window technique requires two pointers, a left pointer that contracts as required
and a right pointer that will expand are each iteration of the search string.

After you've setup everything you need to keep track of where you're at and what you've seen, you iterate through the search
string and apply the following algorithm:

Step 1: Get the right character and update the current frequency map

Step 2: Check if the current character is a required character of the target string. If so, proceed to Step 3. If not proceed to Step 9.

Step 3: Check if we have seen the total count of the required character. If so update, the current counter of total seen required characters. Regardless of the outcome, go to Step 4.

Step 4: Check if you have seen all the unique required characters and their required total counts. If so, go to Step 5. Otherwise, go to Step 9.

Step 5: Update the minimum window size and its pointers.

Step 6: Remove the furthest left character from the current character frequency map.

Step 7: Check if the removed character was also a required character. If so, then decrease the seen required character counter.

Step 8: Increase the left window pointer by 1

Step 9: Increase the right window pointer by 1

Step 10: Once the right pointer is greater than the length of the string, return the final substring.

"""


def min_window(string1, string2):
    return search_entire_string_solution(string1, string2)


def reduced_search_space_solution(string1, string2):
    return


def search_entire_string_solution(s, t):
    # this frequency table will never be changed; it is the information that is needed to determine if we have all the required characters
    required_chars_freq = Counter(t)
    # this is the frequency table of the current window substring; it includes both the required and not required characters
    window_char_mapping = dict()

    # these two counters are crucial. The first counter is the required count of characters that must be in the substring; this counter will never change
    # the second counter is the current count of required characters in the current window substring
    total_chars_to_match = len(required_chars_freq)
    current_required_chars_in_window = 0

    min_window_length_so_far = float("inf")
    min_window_left = 0
    min_window_right = 0

    left = 0
    right = 0

    while right < len(s):
        char_right = s[right]
        char_right_count = window_char_mapping.get(char_right, 0)
        window_char_mapping.update({char_right: char_right_count + 1})

        # check if the character on the right side is part of the required chars
        if char_right in required_chars_freq:
            # get the count of the required character
            # also get the current count of the required character in the current window in the search string
            req_char_count = required_chars_freq.get(char_right)
            req_char_count_in_window = window_char_mapping.get(char_right)

            # if we have the required total count of the required character in the search string
            # update the counter of required characters that have been found in the current window
            if req_char_count_in_window == req_char_count:
                current_required_chars_in_window += 1

        # check if we have seen all the required characters in our current window
        # if so, then the following three step process must occur
        while (
            current_required_chars_in_window == total_chars_to_match and left <= right
        ):

            # First update the minimum window size against the current window size and its left and right pointers
            current_window_size = right - left + 1
            if current_window_size < min_window_length_so_far:
                min_window_length_so_far = current_window_size
                min_window_left = left
                min_window_right = (
                    right + 1
                )  # we add one because slicing arrays does not include rightmost index, and we want the rightmost index

            # since we have found a valid substring that has all the required characters
            # let's contract the left side to discover more and potentially smaller valid substrings
            # Second, remove the furthest left character of the window from our window character count
            char_left = s[left]
            char_left_count = window_char_mapping.get(char_left)
            window_char_mapping.update({char_left: char_left_count - 1})

            # Third, check if the leftmost character was also part of the requirement
            # If so, then the counter of required characters that have been found in the current window must be reduced by 1 but only if the current count of the required character is less than the required count
            if char_left in required_chars_freq:
                char_left_count_in_window = window_char_mapping.get(char_left)
                char_left_count_required = required_chars_freq.get(char_left)
                if char_left_count_in_window < char_left_count_required:
                    current_required_chars_in_window -= 1

            # now that all our counters have been updated, contract the left pointer of the current window
            left += 1

        # regardless of whether the current character is a required character and/or we have found all the required characters
        # we have to expand the current window string, thus this solution is O(n) runtime
        right += 1

    return s[min_window_left:min_window_right]
