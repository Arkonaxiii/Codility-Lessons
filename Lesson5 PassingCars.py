def solution(A):
    zeros = 0
    passed = 0

    for element in A:
        if element == 0:
            zeros += 1
        if element == 1:
            passed = passed + zeros
            if passed > 1000000000:
                return -1
    return passed