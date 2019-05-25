def get_lowest_integer(number, remove):
    if len(number) <= remove:
        return "0"
    
    digits = [int(digit) for digit in number]    
    stack = [digits.pop(0)]

    for digit in digits:
        for num in stack[::-1]:
            if remove > 0 and digit < num:
                stack.pop()    
                remove -= 1
        stack.append(digit)            

    return ''.join([str(x) for x in stack])