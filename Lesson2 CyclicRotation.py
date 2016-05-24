def solution(A, K):
    if len(A) == 0:
        return A
    if K > len(A):
        shift = K % len(A)
    else:
        shift = K

    return A[-shift:] + A[:-shift]