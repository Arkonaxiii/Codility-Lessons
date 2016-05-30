def solution(S):
    
    stack = []
    for s in S:
        if s == '(':
            stack.append(s)
        if s == ')':
            if len(stack) == 0:
                return 0
            stack.pop()
    if len(stack) == 0:
        return 1
    else:
        return 0
