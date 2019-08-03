def find_missing_integer(arr):
    # return find_missing_integer_set(arr)
    return find_missing_integer_pigeonhole_principle_sol(arr)

def find_missing_integer_set(arr):
    result = 1
    arr_set = set(arr)
    
    for num in arr_set:
        if (num > 0) and (result in arr_set):
         result += 1
    return result

def find_missing_integer_pigeonhole_principle_sol(arr):
    is_present = [False] * (len(arr) + 1)

    for num in arr:
        if 0 < num <= len(is_present) - 1:
            is_present[num] = True
    
    for num in range(1, len(is_present)):
        if not is_present[num]:
            return num
    
    return len(is_present)