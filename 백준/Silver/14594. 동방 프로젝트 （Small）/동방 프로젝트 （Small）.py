N = int(input())
M = int(input())
arr = [0] * (N + 1)
for _ in range(M) :
    x, y = map(int, input().split())
    for room in range(x, y) :
        arr[room] = 1

answer = arr.count(0)
print(answer-1)