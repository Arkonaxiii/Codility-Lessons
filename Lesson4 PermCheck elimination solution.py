def solution(A):
    limit = len(A)
    table = [0] * len(A)

    for element in A:
        if 1 <= element <= limit:
            if table[element - 1] == 0:
                table[element - 1] = 1
            else:
                return 0
        else:
            return 0
    return 1