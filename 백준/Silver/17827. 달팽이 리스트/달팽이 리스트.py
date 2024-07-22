import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(M) :
    k = int(input())

    if k <= N - 1 :
        print(arr[k])
    else :
        dal = arr[V-1:]
        print(dal[(k - V + 1)%(N - V + 1)])