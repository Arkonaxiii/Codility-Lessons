def solution(A):
    result = 0

    for index in range(len(A)):
        result = result ^ A[index] ^ (index + 1)
    if result == 0:
        return 1
    else:
        return 0