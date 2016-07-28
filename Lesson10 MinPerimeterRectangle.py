def solution(N):
    factors = []
    i = 1
    bestPerim = N*4 # worst case N = 1 and Perimeter = 4
    while i*i <= N:
        if N%i == 0:
            factors.append((i,N/i))
            perim = 2*(i+N/i)
            if perim < bestPerim:
                bestPerim = perim
        i+=1
    return bestPerim
