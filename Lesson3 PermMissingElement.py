def solution(A):
    sum1 = sum(range(len(A) + 2))
    sum2 = sum(A)
    return sum1 - sum2
