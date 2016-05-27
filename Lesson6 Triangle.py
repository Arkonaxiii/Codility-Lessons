def solution(A):
    if len(A) < 3:
        return 0
    S = sorted(A)
    for index in range(len(S) - 2):
        if S[index] + S[index + 1] > S[index + 2]:
            return 1
    return 0