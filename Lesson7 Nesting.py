def solution(S):
    
    stack = []
    for s in S:
        if s == '(':
            stack.append(s)
        else:
            if len(stack) == 0:
                return 0
            stack.pop()
    if len(stack) == 0:
        return 1
    else:
        return 0
    
    #można bez stosu, sam counter
    
    def solution(S):
    if len(S) == 0:
        return 1
    res = 0
    for p in S:
        if p == '(':
            res += 1
        else:
            res -= 1
        if res < 0:
            return 0
    if res == 0:
        return 1
    else:
        return 0
    
