def solution(A):
    max_left = 0
    max_right = 0
    for i in range(len(A)):
        if A[i] + i > max_left:
            max_left = A[i] + i
    for i in range(len(A)):
        if A[i] - i > max_right:
            max_right = A[i] - i
    print max_left
    print max_right
    return max_left + max_right
    
