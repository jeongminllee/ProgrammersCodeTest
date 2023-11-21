K, N = map(int, input().split())
line = [int(input()) for _ in range(K)]
start, end = 1, max(line)

while start <= end :
    mid = (start + end) // 2
    lines = 0
    for i in line :
        lines += i // mid

    if lines >= N :
        start = mid + 1
    else :
        end = mid - 1

print(end)