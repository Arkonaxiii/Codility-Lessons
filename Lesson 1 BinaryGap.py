def solution(N):
    s = str(bin(N))[2:]  # string z wersji binarnej bez dwoch pierwszych elementów

    length = len(s)
    gaplen = 0
    longest = 0

    for element in s:
        if element == "0":
            gaplen += 1
        else:
            if gaplen > longest:
                longest = gaplen  # nie przejmuje się jedynką na końcu bo zawsze jest jedynka na końcu?
            gaplen = 0
    return longest
