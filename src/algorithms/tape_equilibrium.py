def get_min_from_tape(arr):
    size = len(arr)
    total = sum(arr)
    left_sum = [None] * size
    left_sum[len(left_sum) - 1] = 0

    for index, ele in enumerate(left_sum):
        left_sum[index] = (left_sum[index -1] + arr[index])
    
    min = total
    for index, ele in enumerate(arr):
        curr_min = abs(left_sum[index] - (total - left_sum[index]))
        if curr_min < min:
            min = curr_min
    
    return min
