def solution(A):
    
    xor_sum = len(A)+1
    for index,element in enumerate(A,1):
        xor_sum ^= index
        xor_sum ^= element
    return xor_sum
