import sys
input = sys.stdin.readline

def distance(x1, y1, x2, y2) :
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2)

def sol_6003() :
    N = int(input())    # The number of cows
    cows = [[0, 0]]

    for _ in range(N) :
        cows.append(list(map(int, input().split())))


    mn_dist = 200_001
    res = [0, 0]
    for i in range(1, N) :
        for j in range(i + 1, N + 1) :
            # 같은 길이는 존재하지 않는다고 했으니까.
            if distance(cows[i][0], cows[i][1], cows[j][0], cows[j][1]) < mn_dist :
                mn_dist = distance(cows[i][0], cows[i][1], cows[j][0], cows[j][1])
                res = [i, j]

    print(*res)
sol_6003()