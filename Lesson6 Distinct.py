def solution(A):
   
    if len(A) == 0:
        return 0
    S = sorted(A)
    last = 0
    D = [0]*len(S)
    for index in range(len(S)):
        if index == 0:
            D[last] = S[index]
        if S[index] != D[last]:
            D[last+1] = S[index]
            last += 1           
            
    return last+1
