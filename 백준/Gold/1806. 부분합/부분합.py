N, M = map(int, input().split())
lst = list(map(int, input().split()))

left, right = 0, 0
target = 0
length = N + 1

while True :
    if target >= M :
        length = min(length, right - left)
        target -= lst[left]
        left += 1

    elif right == N :
        break

    else :
        target += lst[right]
        right += 1

if length == N + 1 :
    print(0)
else :
    print(length)