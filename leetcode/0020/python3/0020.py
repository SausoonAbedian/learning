def is_valid(s: str) -> bool:
    if len(s) == 1:
        return False
    stack = []
    for c in s:
        if c == '}' or c == ']' or c == ')':
            if len(stack) == 0:
                return False
            st = stack[-1]
            if ((c == '}' and st == '{') or
                    (c == ']' and st == '[') or
                    (c == ')' and st == '(')):
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return len(stack) == 0


assert is_valid("()")
assert is_valid("()[]{}")
assert not is_valid("(]")
assert is_valid("([])")
