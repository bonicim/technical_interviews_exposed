def get_min_parenthesis(string):
    """Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

    Formally, a parentheses string is valid if and only if:

    It is the empty string, or
    It can be written as AB (A concatenated with B), where A and B are valid strings, or
    It can be written as (A), where A is a valid string.
    Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.

    Example: "())" => 1
    """
    # return stack_solution(string)
    return balance_solution(string)


def stack_solution(string):
    stack = []
    closing_parens = {")": "("}

    for char in string:
        if char in closing_parens:
            if not stack:
                stack.append(char)
            else:
                # peek at the stack
                top_opening_paren = stack[-1]
                # check if the current closing_parens has its matching opening_parens
                # if it does, we have a match; remove it from the stack; otherwise add it to the stack
                if closing_parens.get(char) == top_opening_paren:
                    stack.pop()
                else:
                    stack.append(char)
        else:
            stack.append(char)

    # The remaining items in the stack have no matches. Thus the size is the number of items that require a matching pair
    return len(stack)


def balance_solution(string):
    unpaired_open_paren = 0
    unpaired_closed_paren = 0
    open_parens = {"("}
    closed_parens = {")"}

    for char in string:
        # if char == "(":
        # if we have an open_parenthesis, increase the open parens count. Otherwise, decrease it because we found its closing pair
        if char in open_parens:
            unpaired_open_paren += 1
        elif char in closed_parens:
            unpaired_open_paren -= 1
        else:
            raise Exception(
                "Illegal input. Must contain only open and closed parenthesis."
            )
        # an unpaired_open_parens count of -1 means that we have a closed parenthesis without its opening pair. Thus update the number of unpaired closed parenthesis and also update the number of unpaired opened parenthesis
        if unpaired_open_paren == -1:
            unpaired_open_paren += 1
            unpaired_closed_paren += 1

    return unpaired_open_paren + unpaired_closed_paren
