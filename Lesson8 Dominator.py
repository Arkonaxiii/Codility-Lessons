def solution(A):
    
    size = 0
    
    for i in range(len(A)):
        if size == 0:
            value = A[i]
            size += 1
        else:
            if value != A[i]:
                size -= 1
            else: 
                size += 1
    candidate = -1
    if size > 0:
        candidate = value
    leader = -1
    count = 0
    for element in A:
        if element == candidate:
            count += 1
    if count > (len(A)//2):
        leader = candidate
    else:
        return -1
    for i in range(len(A)):
        if A[i] == leader:
            return i
            break
