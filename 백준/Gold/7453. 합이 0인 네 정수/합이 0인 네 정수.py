import sys
input = sys.stdin.readline

def sol_7453() :
    n = int(input())
    res = 0
    A = []
    B = []
    C = []
    D = []

    for _ in range(n) :
        a, b, c, d = map(int, input().split())
        A.append(a)
        B.append(b)
        C.append(c)
        D.append(d)

    AB = list(a + b for a in A for b in B)
    CD = list(c + d for c in C for d in D)
    AB.sort()
    CD.sort()

    left, right = 0, len(CD) - 1
    while left < len(AB) and right >= 0 :
        sumval = AB[left] + CD[right]
        if sumval == 0:
            nxt_left, nxt_right = left + 1, right - 1
            while nxt_left < len(AB) and AB[left] == AB[nxt_left] :
                nxt_left += 1
            while nxt_right >= 0 and CD[right] == CD[nxt_right] :
                nxt_right -= 1

            res += (nxt_left - left) * (right - nxt_right)
            left, right = nxt_left, nxt_right

        elif sumval < 0 :
            left += 1
        else :
            right -= 1

    print(res)


sol_7453()