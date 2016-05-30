def solution(X,A):
    left = 0
    right = len(A)-1
    while left < right:
        while A[left] != X and left < right:
            left +=1
            print "l: " + str(left)
        while A[right] == X and right > left:
            right -= 1
            print "r: " + str(right)
        if left == right:
            return left +1
        if right-left == 1:
            return right
        left += 1
        right -= 1 
