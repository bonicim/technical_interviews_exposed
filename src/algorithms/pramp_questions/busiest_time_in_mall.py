def find_busiest_period(data):
    # return solution_pointers_while_loop(data)
    return solution_elegant(data)


def solution_elegant(data):
    curr_count = 0
    busiest = curr_count
    busiest_time = 0

    for index, data_point in enumerate(data):
        timestamp, count, entry = data_point

        if entry == 1:
            curr_count += count
        elif entry == 0:
            curr_count -= count

        if index < len(data) - 1 and timestamp == data[index + 1][0]:
            continue

        # we have a change in time, update the count
        if curr_count > busiest:
            busiest = curr_count
            busiest_time = timestamp

    return busiest_time


def solution_pointers_while_loop(data):
    busiest_time = data[0][0]
    curr_count = 0
    busiest = curr_count
    left = 0

    while left < len(data):
        ts = data[left][0]
        right = get_slice_same_time(data, ts, left + 1)

        net_count_at_time = get_guest_count(data, left, right)
        if right + 1 - left > 1:
            left = right + 1
        else:
            left += 1

        curr_count += net_count_at_time
        if curr_count > busiest:
            busiest = curr_count
            busiest_time = ts

    return busiest_time


def get_slice_same_time(data, ts, ahead):
    if ahead >= len(data) or data[ahead][0] != ts:
        return ahead - 1
    return get_slice_same_time(data, ts, ahead + 1)


def get_guest_count(data, left, right):
    net_count = 0
    index = left
    while index < right + 1:
        _, count, entry = data[index]
        if entry == 0:
            count *= -1
        net_count += count
        index += 1

    return net_count
