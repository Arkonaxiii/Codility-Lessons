def solution(A):
    result = 0
    for number in A:
        result ^= number #XOR
    return result

#^ is XOR. X^X = 0, X^0 = X