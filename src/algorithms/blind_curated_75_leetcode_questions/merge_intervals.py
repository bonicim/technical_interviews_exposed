def merge(intervals):
    """
    Given a collection of intervals, merge all overlapping intervals.

    Example 1:

    Input: [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
    Example 2:

    Input: [[1,4],[4,5]]
    Output: [[1,5]]
    Explanation: Intervals [1,4] and [4,5] are considered overlapping.

    """
    return greedy_v1(intervals)


def greedy_v1(intervals):
    if not intervals:
        return intervals

    intervals_sorted = sorted(intervals)
    stack = [intervals_sorted[0]]

    for index in range(1, len(intervals_sorted)):
        prev_start_time, prev_end_time = stack[-1]
        curr_start_time, curr_end_time = intervals_sorted[index]

        if curr_start_time > prev_end_time:
            stack.append([curr_start_time, curr_end_time])
        elif curr_start_time <= prev_end_time and curr_end_time > prev_end_time:
            stack.pop()
            stack.append([prev_start_time, curr_end_time])

    return stack
