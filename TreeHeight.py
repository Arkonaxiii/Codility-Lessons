def solution(T):
    if T.l == None and T.r == None:
        return 0
    if T.l == None:
        return 1 + solution(T.r)
    if T.r == None:
        return 1 + solution(T.l)
    else:
        return 1 + max(solution(T.r), solution(T.l))
