def solution(A):
    xor_sum = 0
    for index in range(len(A)):
        xor_sum = xor_sum ^ A[index] ^ (index+1)
    return xor_sum^(len(A)+1)