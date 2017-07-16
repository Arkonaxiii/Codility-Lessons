def solution(A):
   
    if len(A) == 0:
        return 0
    S = sorted(A)
    last = 0
    D = [0]*len(S)
    for index in range(len(S)):
        if index == 0:
            D[last] = S[index]
        if S[index] != D[last]:
            D[last+1] = S[index]
            last += 1           
            
    return last+1

# lub

def solution(A):
    
    if len(A) == 0:
        return 0
        
    S = sorted(A)
    counter = 1
    last = S[0]
    
    for number in S:
        if number > last:
            counter += 1
            last = number
    return counter
