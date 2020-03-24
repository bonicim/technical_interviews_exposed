def maximum_possible_value(n):
    sign = 1
    if n < 0:
        sign *= -1
        n *= -1

    num = [int(digit) for digit in str(n)]  # space of 2n
    insertion = 0

    for index, digit in enumerate(num):
        insertion = index
        if (sign > 0 and digit < 5) or (sign < 0 and digit > 5):
            break

    result = num[:insertion] + [5] + num[insertion:]  # space of 2n
    result = [str(d) for d in result]
    return int("".join(result)) * sign
