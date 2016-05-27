def solution(A):
    
    P = [0]*(len(A)+1)
    if len(A) == 0:
        return -1
    for i in range(1,len(P)):
        P[i] = P[i-1] + A[i-1]
    
    for i in range(len(A)):
        if i == 0:
            left = 0
            right = P[len(A)] - P[i+1]
        elif i == len(A)-1:
            right = 0
            left = P[i] - P[0]
        elif i == 1:
            left = A[0]
            right = P[len(A)] - P[i+1]
        elif i == len(A)-1:
            right = A[len(A)-1]
            left = P[i] - P[0]
        else:
            left = P[i] - P[0]
            right = P[len(A)] - P[i+1]
        if left == right:
            return i
    return -1
