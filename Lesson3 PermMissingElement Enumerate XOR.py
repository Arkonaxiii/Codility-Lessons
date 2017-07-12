def solution(A):
    
    xor_sum = len(A)+1
    for index,element in enumerate(A,1):
        xor_sum = xor_sum ^ index ^ element  # (P ^ Q) ^ R = P ^ (Q ^ R) = P ^ Q ^ R
    return xor_sum
