N = int(input())
M = int(input())
arr = [0] * (N + 1)
for _ in range(M) :
    x, y = map(int, input().split())
    for i in range(x, y) :
        arr[i] = 1

print(arr.count(0)-1)