def solution(A):
    left = A[0]
    right = sum(A[1:])

    bestdiff = abs(left - right)

    for i in range(1, len(A) - 1):
        left += A[i]
        right -= A[i]
        diff = abs(left - right)
        if diff < bestdiff:
            bestdiff = diff
    return bestdiff