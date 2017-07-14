def solution(X, A):
    completedsteps = [0] * X
    index = 0
    covered = 0

    for element in A:
        index += 1
        if completedsteps[element - 1] == 0:
            completedsteps[element - 1] = 1
            covered += 1
            if covered == X:
                return index - 1
    return -1

# shame, lepiej na enumerate:

def solution(X,A):
    H = [0] * X
    counter = 0
    for index, element in enumerate(A):
        if H[element-1] == 0:
            H[element-1] = 1
            counter += 1
            if counter == X:
                return index
    return -1
