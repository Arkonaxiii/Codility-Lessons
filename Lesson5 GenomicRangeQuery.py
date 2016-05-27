def solution(S, P, Q):
    slownik = {"A": 1, "C": 2, "G": 3, "T": 4}
    S_list = [0] * len(S)
    Pref1 = [0] * (len(S) + 1)
    Pref2 = [0] * (len(S) + 1)
    Pref3 = [0] * (len(S) + 1)
    Pref4 = [0] * (len(S) + 1)
    for index in range(len(S)):
        S_list[index] = slownik[S[index]]

    for index in range(len(S)):
        Pref1[index + 1] = Pref1[index]
        Pref2[index + 1] = Pref2[index]
        Pref3[index + 1] = Pref3[index]
        Pref4[index + 1] = Pref4[index]

        if S_list[index] == 1:
            Pref1[index + 1] += 1
        elif S_list[index] == 2:
            Pref2[index + 1] += 1
        elif S_list[index] == 3:
            Pref3[index + 1] += 1
        else:
            Pref4[index + 1] += 1

    result = [0] * len(P)
    for i in range(len(P)):
        AsInRange = Pref1[Q[i] + 1] - Pref1[P[i]]
        CsInRange = Pref2[Q[i] + 1] - Pref2[P[i]]
        GsInRange = Pref3[Q[i] + 1] - Pref3[P[i]]

        if AsInRange > 0:
            result[i] = 1
        elif CsInRange > 0:
            result[i] = 2
        elif GsInRange > 0:
            result[i] = 3
        else:
            result[i] = 4
    return result