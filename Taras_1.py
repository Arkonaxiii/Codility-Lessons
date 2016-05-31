def solution(A,B):
    
    if B < 0:
        return 0
    if A < 0:
        A = 0
    counter = 0
    i = 0
    while i*i<B:
        if i*i>=A:
            counter += 1 
        i += 1           
        if i*i > B:
            return counter
            
