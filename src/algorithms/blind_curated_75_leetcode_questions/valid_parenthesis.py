def valid_parenthesis(string):
    stack = []
    closing = {")": "(", "]": "["}
    opening = set(["(", "["])

    for char in string:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if stack:
                peek = stack[-1]
                if peek == closing.get(char):
                    stack.pop()
                else:
                    return False
            # when we are here, we know that we have a closing parenthesis with no opening parenthesises at all, we should simply stop
            # checking because at this point, this is the earliest we know that the string is invalid, going from left to right
            else:
                return False
        else:
            raise Exception("Invalid character")

    return not stack
