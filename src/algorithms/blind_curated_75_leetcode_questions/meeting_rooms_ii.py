import heapq


def min_meeting_rooms(intervals):
    """
    Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

    Example 1:

    Input: [[0, 30],[5, 10],[15, 20]]
    Output: 2
    Example 2:

    Input: [[7,10],[2,4]]
    Output: 1
    """
    # return heap_data_structure_solution(intervals)
    return chronological_ordering_solution(intervals)


def heap_data_structure_solution(intervals):
    if not intervals:
        return 0

    rooms_heap = []

    intervals_sorted = sorted(intervals)
    end_time = intervals_sorted[0][1]

    heapq.heappush(rooms_heap, end_time)

    for index in range(1, len(intervals_sorted)):
        start_time_meeting, end_time_meeting = intervals_sorted[index]
        room_end_time = rooms_heap[0]

        if room_end_time <= start_time_meeting:
            heapq.heappop(rooms_heap)
        heapq.heappush(rooms_heap, end_time_meeting)

    return len(rooms_heap)


def chronological_ordering_solution(intervals):
    start_times = sorted([interval[0] for interval in intervals])
    end_times = sorted([interval[1] for interval in intervals])

    rooms = 0
    end_index = 0

    for start_index in range(len(start_times)):
        start = start_times[start_index]
        end = end_times[end_index]

        if start >= end:
            end_index += 1
        else:
            rooms += 1

    return rooms
