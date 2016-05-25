def solution(N, A):
    counters = [0] * N
    max_counter = 0
    current_max = 0

    for element in A:
        if element <= N:
            if max_counter > counters[element - 1]:
                counters[element - 1] = max_counter
            counters[element - 1] += 1
            if current_max < counters[element - 1]:
                current_max = counters[element - 1]
        else:
            max_counter = current_max
    for index in range(N):
        if counters[index] < max_counter:
            counters[index] = max_counter
    return counters