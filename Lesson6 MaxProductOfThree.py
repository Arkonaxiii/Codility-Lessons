def solution(A):
    
    S = sorted(A)
    le = len(S)
    
    if le < 3:
        return 0
    elif S[0] < 0 and S[1] < 0: # two values below zero * max value
        return max(S[0]*S[1]*S[le-1], S[le-1]*S[le-2]*S[le-3])
    else:
        return S[le-1]*S[le-2]*S[le-3]
        
    #but it's not necessary, it's simpler to check the left and right side withou if statement:
    
def solution(A):
    
    S = sorted(A)
    le = len(S)
   
    return max(S[0]*S[1]*S[le-1], S[le-1]*S[le-2]*S[le-3])
