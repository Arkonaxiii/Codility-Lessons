def solution(N):
    result = 1
    while N != 1:
        if N%2 != 0:
            N -=1
            result +=1
        if N%2 == 0:
            N /= 2
            result += 1       
    return result 
