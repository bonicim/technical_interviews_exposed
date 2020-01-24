"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

Example 1:

Input: [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: [[7,10],[2,4]]
Output: true

"""

""" Commentary

This problem centers on the idea that a meeting's start time can never be less than another meeting's end time.
We need to take this insight and use it to solve the problem. Moreover, to solve the problem efficiently, we need
a sorted list of meetings where they are sorted by ascending start times. This will allow us to quickly find
out if a meeting overlaps with another one. It avoids the unnecessary comparison of one meeting to every meeting
as seen in a brute force solution.

Finally, there are many ways to implement the solution. All solutions must first sort the list, which dominates the
runtime at nlogn for a typical sorting algorithm. The real cost in is space.

One solution uses constant space by using indexes to compare meetings.

The second solution also doesn't use space, but requires more variables to hold the last known end time.

The third solution uses at most N space because it uses a stack to keep track of previous meetings, which is
not necessary, since we only care about the most recent previous meeting at a certain point in time.
"""


def meeting_rooms_v1(intervals):
    meetings = sorted(intervals)
    for index in range(
        len(meetings) - 1
    ):  # don't check the very last meeting because there is nothing to compare it to
        previous_end_time = meetings[index + 1][0]
        current_start_time = meetings[index][1]
        if current_start_time > previous_end_time:
            return False
    return True


def meeting_rooms_v2(intervals):
    if not intervals:
        return True

    meetings = sorted(intervals)
    latest_end_time = meetings[0][1]
    for interval_index in range(1, len(meetings)):
        interval = meetings[interval_index]
        curr_start = interval[0]

        if curr_start < latest_end_time:
            return False
        latest_end_time = interval[1]
    return True


def meeting_rooms_v3(intervals):
    if not intervals:
        return True

    meetings = sorted(intervals)
    stack = [meetings[0]]
    for index in range(1, len(meetings)):
        curr_meeting = meetings[index]
        curr_start = curr_meeting[0]
        prev_meeting = stack[-1]
        prev_end = prev_meeting[1]

        if curr_start < prev_end:
            return False

        stack.append(curr_meeting)

    return True
