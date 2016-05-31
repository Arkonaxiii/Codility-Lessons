def solution(A):
    
    P = [0]*(len(A)+1)
    counter = 0
    
    for i in range(len(A)):
        P[i+1] = P[i]+A[i]
    for i in range(len(A)):
        for j in range(1,len(A)):
            if j>=i:
                if P[j+1]-P[i] == 0:
                    counter += 1
                    print "i: " + str(i)
                    print "j: " + str(j)
                    print "sum: " + str(P[j+1]-P[i])
                    if counter > 1000000000:
                        return -1
    return counter
