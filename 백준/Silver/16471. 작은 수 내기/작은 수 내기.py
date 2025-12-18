N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

win = (N+1) // 2
cnt = 0

left = 0
right = 0

while left < N and right < N :
    if A[left] >= B[right] :
        right += 1
    else :
        cnt += 1
        left += 1
        right += 1

if cnt >= win :
    print("YES")
else :
    print("NO")