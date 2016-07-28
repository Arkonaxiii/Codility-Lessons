def solution(A):
    factors = []
    i = 1
    while i*i <= A:
        if A%i == 0:
            factors.append(i)
            if A/i not in factors:
                factors.append(A/i)
        i+=1
    return len(factors)
