def solution(A):
    
    length = len(A)
    P = [0] * (length+1)
    best = [0] * (len(A)-1)
    
    for index in range (1, length + 1):
        P[index] = P[index-1] + A[index-1]
        
    for index in range(len(A)):
        if len(A)-index >= 3:
            best[index] = min((P[index+2] - P[index])/2.0, (P[index+3] - P[index])/3.0)
        if len(A)-index == 2:
            best[index] = (P[index+2] - P[index])/2.0       
    return best.index(min(best))
