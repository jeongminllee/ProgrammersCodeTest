N = int(input())
row1 = list(map(int, input().split()))
row2 = list(map(int, input().split()))

ans = 0

# 첫 번째 행의 타일 경계 길이
for a in range(N) :
    if row1[a] == 1 :
        ans += 3

# 두 번째 행의 타일 경계 길이
for a in range(N) :
    if row2[a] == 1 :
        ans += 3

# 경계 겹침 처리
for a in range(N - 1) :
    if row1[a] == 1 and row1[a+1] == 1 :
        ans -= 2
    if row2[a] == 1 and row2[a+1] == 1 :
        ans -= 2

# 특정 위치의 경계 겹침 처리
for a in range(0, N, 2) :
    if row1[a] == 1 and row2[a] == 1 :
        ans -= 2

print(ans)