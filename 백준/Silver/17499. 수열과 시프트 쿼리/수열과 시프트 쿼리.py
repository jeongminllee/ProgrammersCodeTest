import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
lst = list(map(int, input().split()))
p = 0
for _ in range(Q) :
    query = list(map(int, input().split()))
    if query[0] == 1 :
        lst[(p + query[1] - 1) % N] += query[2]

    elif query[0] == 2 :
        p -= query[1]

    elif query[0] == 3 :
        p += query[1]

for i in range(N) :
    print(lst[(i+p)%N], end=' ')