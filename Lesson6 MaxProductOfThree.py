def solution(A):
    
    S = sorted(A)
    le = len(S)
    
    if le < 3:
        return 0
    elif S[0] < 0 and S[1] < 0:
        return max(S[0]*S[1]*S[le-1], S[le-1]*S[le-2]*S[le-3])
    else:
        return S[le-1]*S[le-2]*S[le-3]
