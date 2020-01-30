"""Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:

It is the empty string, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.

Example: "())" => 1
"""

"""Commentary

Valid Parenthesis is an easy problem that tests an engineer's knowledge of data structures and why certain structures should be preferred over others, specifically the stack.
In this problem, we are asked to find if there are any missing pairs of parenthesis. The key point is understanding what pairs mean.

For example, "()" does not have any missing pairs. It is complete. But ")(" has two missing pairs. Why? Because order matters. From left to right,
we see that ")" and "(" cannot be each other's pair because they are out of order. Thus, when solving this problem, we need to keep track of history, specifically
what was the last character we saw in the string. And what is a good data structure that can help track history that gives us quick access to the
most recently seen item? The Stack! The Stack is a LIFO queue: last in, first out. But what goes in the stack? What matters to us? When we encounter
a closed parenthesis, we know that we had to have seen an open parenthesis in the most recent past. We use the stack to check if we've seen an open parenthesis.
If so, we remove it from the stack. Otherwise, we add that character to the stack. At the end, the stack is total number of unpaired parenthesis.

The solution takes space of O(n) because at worst the input could be a bunch of closed parentheses such as ")))))))".

There is a solution that takes time of O(n) with constant space of O(1). This is the best of both worlds. This solution uses a counter of unpaired open and closed parenthesis.
It is not as intuitive as the stack solution. But it essentially does the same thing without using space. However, it only works when there is
one type of parenthesis; anymore, then the solution breaks. Example: "((((])))" would errorneouly return true
"""


def get_min_parenthesis(string):
    return stack_solution(string)
    # return balance_solution(string)


def stack_solution(string):
    stack = []
    closing_parens = {")": "(", "]": "["}

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
