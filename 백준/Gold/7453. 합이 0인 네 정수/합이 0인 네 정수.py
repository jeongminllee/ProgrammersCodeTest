import sys
input = sys.stdin.readline

def sol_7453() :
    n = int(input())
    res = 0
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr = list(map(sorted, zip(*arr)))

    AB = list(a + b for a in arr[0] for b in arr[1])
    CD = list(c + d for c in arr[2] for d in arr[3])
    AB.sort()
    CD.sort()

    left, right = 0, len(CD) - 1

    while left < len(AB) and right >= 0 :
        sumval = AB[left] + CD[right]
        if sumval == 0 :
            n_left, n_right = left + 1, right - 1
            while n_left < len(AB) and AB[left] == AB[n_left] :
                n_left += 1
            while n_right >= 0 and CD[right] == CD[n_right] :
                n_right -= 1

            res += (n_left - left) * (right - n_right)
            left, right = n_left, n_right

        elif sumval < 0 :
            left += 1
        else :
            right -= 1

    print(res)


sol_7453()