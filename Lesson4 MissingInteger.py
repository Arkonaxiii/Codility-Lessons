def solution(A):
    table = [0] * (len(A) + 1)

    for element in A:
        if 0 < element <= (len(A) + 1):
            if table[element - 1] == 0:
                table[element - 1] = 1
    for index in range(len(A) + 1):
        if table[index] == 0:
            return index + 1