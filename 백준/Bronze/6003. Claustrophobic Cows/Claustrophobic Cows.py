import sys
input = sys.stdin.readline

def distance(x1, y1, x2, y2) :
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2)
def sol_6003() :
    N = int(input())    # The number of cows
    cows = [list(map(int, input().split())) for _ in range(N)]
    mn = 200_001 ** 2
    cow1 = cow2 = 0

    for i in range(N) :
        for j in range(i) :
            d = distance(cows[i][0], cows[i][1], cows[j][0], cows[j][1])
            if d < mn :
                mn = d
                cow1 = j + 1
                cow2 = i + 1
                
    print(cow1, cow2)

sol_6003()