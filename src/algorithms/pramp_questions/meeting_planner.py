def meeting_planner(slotsA, slotsB, dur):
    a_index = 0
    b_index = 0

    while a_index < len(slotsA) and b_index < len(slotsB):
        a_start = slotsA[a_index][0]
        b_start = slotsB[b_index][0]
        start = max(a_start, b_start)
        # get the latest start time

        a_end = slotsA[a_index][1]
        b_end = slotsB[b_index][1]
        end = min(a_end, b_end)
        # get the earliest end time

        if start + dur <= end:
            return [start, start + dur]
        # then check if the dur from start is less than or equal to the earliest end time
        # if so, return the interval
        # otherwise, increment of the pointer of the earliest end time because we want the first earliest interval. Thus, we want the get the next earliest time available between two ranges
        if a_end < b_end:
            a_index += 1
        else:
            b_index += 1

    return []
