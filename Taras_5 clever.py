def solution(A):
    
    sum_dict = {}
    sum_dict[0] = 1
    suma = 0
    counter = 0
    P = [0]*(len(A)+1)
    for i in range(len(A)):
        P[i+1] = P[i]+A[i]
    for i in xrange(len(A)):
        suma+=A[i]
        if suma not in sum_dict:
            sum_dict[suma] = 0
        counter += sum_dict[suma]
        if counter > 1000000000:
            return -1
        sum_dict[suma] += 1
    return counter
