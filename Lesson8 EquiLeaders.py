def solution(A):
    
    size = 0
    
    # finding lider
    for i in range(len(A)):
       if size == 0:
           value = A[i]
           size += 1
       else:
           if value != A[i]:
               size -= 1
           else:
               size += 1
    if size > 0:
       candidate = value
       count = 0
       for element in A:
           if element == candidate:
               count +=1
       if count > len(A)//2:
           leader = candidate
       else:
           return 0
    else:
        return 0 
        
    
   # finding equi liders   
    
    leaders_found_so_far = 0
    equi_liders = 0
    
    for index in range(len(A)):
        if A[index] == leader:
            leaders_found_so_far += 1
        if leaders_found_so_far > (index+1)//2 and count-leaders_found_so_far > (len(A)-index-1)//2:
            equi_liders += 1
    return equi_liders
