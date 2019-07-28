def find_missing_integer(arr):
    result = 1
    arr_set = set(arr)
    
    for num in arr_set:
        if (num > 0) and (result in arr_set):
            result += 1
    return result