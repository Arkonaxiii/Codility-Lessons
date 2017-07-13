def solution(A):
    table = [0] * (len(A) + 1)

    for element in A:
        if 0 < element <= (len(A) + 1):
            if table[element - 1] == 0:   # chyba można by bez ifa, i od razu zrobić przypisanie?
                table[element - 1] = 1
    for index in range(len(A) + 1):
        if table[index] == 0:
            return index + 1
        
        
       albo:
        
 def solution(A):
    D ={}
    for i in range(len(A)+1):
        D[i+1] = 0
    for i in range(len(A)):
        D[A[i]] = 1
    for k in D.keys():
        if D[k] == 0:
            return k       
