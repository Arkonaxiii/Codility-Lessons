# note that gap is only between 1s so e.g. 11000 has NO gap

def solution(N):
    
    B = bin(N)[2:]
    longest = 0
    temp = 0
    
    for digit in B:
        print digit
        if digit == "1":
            if temp > longest:
                longest = temp
                temp = 0
        else:
            temp += 1      
    return longest
