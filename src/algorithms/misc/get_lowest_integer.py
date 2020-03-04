def get_lowest_integer(number, remove):
    digits = [int(digit) for digit in number]
    stack = [digits.pop(0)]

    for digit in digits:
        for num in stack[::-1]:
            if (remove > 0) and (digit < num):
                stack.pop()
                remove -= 1
        stack.append(digit)

    # handles edge cases where largest digits are in the rightmost part of the number
    if remove > 0:
        while stack and remove > 0:
            stack.pop()
            remove -= 1

    # required to ensure that 0 is returned when removing all the digits
    if not stack:
        stack.append("0")

    return "".join([str(x) for x in stack])
