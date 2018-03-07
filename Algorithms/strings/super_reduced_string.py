#!/bin/python3


def super_reduced_string(s):
    _stack = []
    for i in range(len(s)):
        if not _stack or s[i] != _stack[-1]:
            _stack.append(s[i])
        else:
            _stack.pop()

    if not _stack:
        return "Empty String"
    else:
        return "".join(_stack)


s = input().strip()
result = super_reduced_string(s)
print(result)
