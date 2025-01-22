def main() :
    S1 = input()
    S2 = input()
    n = len(S1)
    res = ''

    for i in range(n) :
        diff = ord(S2[i]) - ord(S1[i])

        if diff < 1 :
            diff += 26

        res += chr(diff + 64)

    pi = [0] * n
    for i in range(1, n) :
        j = pi[i - 1]
        while j > 0 and res[i] != res[j] :
            j = pi[j - 1]

        if res[i] == res[j] :
            j += 1
        pi[i] = j

    k = n - pi[-1]
    if n % k == 0 :
        return res[:k]
    return res

print(main())