def get_min_parenthesis(string):
    """Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

    Formally, a parentheses string is valid if and only if:

    It is the empty string, or
    It can be written as AB (A concatenated with B), where A and B are valid strings, or
    It can be written as (A), where A is a valid string.
    Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.

    Example: "())" => 1
    """
    return stack_solution(string)
    # return balance_solution(string)


def stack_solution(string):
    stack = []

    for char in string:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if stack:
                char_in_stack = stack.pop()
                stack.append(char_in_stack)
                if char_in_stack == "(":
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)

        else:
            raise Exception(
                "Illegal input. The string should only consist of open or closed parenthesis"
            )

    return len(stack)


def balance_solution(string):
    unpaired_open_paren = 0
    unpaired_closed_paren = 0

    for char in string:
        if char == "(":
            unpaired_open_paren += 1
        elif char == ")":
            unpaired_open_paren -= 1
        else:
            raise Exception(
                "Illegal input. Must contain only open and closed parenthesis."
            )

        if unpaired_open_paren == -1:
            unpaired_open_paren += 1
            unpaired_closed_paren += 1

    return unpaired_open_paren + unpaired_closed_paren
