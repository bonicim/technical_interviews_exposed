def erase_overlap_intervals(intervals):
    """
    Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

    Example 1:

    Input: [[1,2],[2,3],[3,4],[1,3]]
    Output: 1
    Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
    Example 2:

    Input: [[1,2],[1,2],[1,2]]
    Output: 2
    Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
    Example 3:

    Input: [[1,2],[2,3]]
    Output: 0
    Explanation: You don't need to remove any of the intervals since they're already non-overlapping.


    Note:

    You may assume the interval's end point is always bigger than its start point.
    Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.

    """
    # return greedy_solution_v1(intervals)
    return greedy_solution_v2(intervals)


def greedy_solution_v1(intervals):
    if not intervals:
        return 0

    intervals_sorted = sorted(intervals)
    stack = [intervals_sorted[0]]

    for index in range(1, len(intervals_sorted)):
        curr_start_time, curr_end_time = (
            intervals_sorted[index][0],
            intervals_sorted[index][1],
        )
        end_time = stack[-1][1]

        if curr_start_time >= end_time and curr_end_time >= end_time:
            stack.append(intervals_sorted[index])
        elif curr_start_time < end_time and curr_end_time < end_time:
            stack.pop()
            stack.append(intervals_sorted[index])
        # elif curr_start_time < end_time and curr_end_time > end_time:
        #     continue

    return len(intervals) - len(stack)


def greedy_solution_v2(intervals):
    """
    This uses less space because it uses pointers instead of a stack.

    However, it is less readable and understandable
    """
    intervals_sorted = sorted(intervals)
    prev_index = 0
    count = 0

    for index in range(1, len(intervals_sorted)):
        prev_end_time = intervals_sorted[prev_index][1]
        curr_start_time, curr_end_time = (
            intervals_sorted[index][0],
            intervals_sorted[index][1],
        )

        if curr_start_time >= prev_end_time and curr_end_time >= prev_end_time:
            prev_index = index
        elif curr_start_time < prev_end_time and curr_end_time < prev_end_time:
            prev_index = index
            count += 1
        elif curr_start_time < prev_end_time and curr_end_time >= prev_end_time:
            count += 1
    return count
