def solution(T):
    
    amplitudes = []
    
    def search(T, min_found, max_found):
        min_found = min(T.x, min_found)
        max_found = max(T.x, max_found)
        if T.l == None and T.r == None:
            amplitudes.append(max_found-min_found)
        if T.l == None:
            search(T.r, min_found, max_found)
        if T.r == None:
            search(T.l, min_found, max_found)
    search(T,1000000000, -1000000000)
    return max(amplitudes)
