def solution(A,M):
    
    markers = [0]*M
    for a in A:
        markers[a%M]+=1
    print markers
    return max(markers)
