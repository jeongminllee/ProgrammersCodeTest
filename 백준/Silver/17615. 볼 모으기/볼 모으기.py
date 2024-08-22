N = int(input())
arr = list(input())
ans = []
blue = red = cnt = 0

# 우측으로 레드 보내기
for i in range(N) :
    if arr[i] == 'R' :
        red += 1

    if arr[i] == 'B' and red :
        cnt += red
        red = 0

ans.append(cnt)

# 우측으로 블루 보내기
cnt = 0
for i in range(N):
    if arr[i] == 'B':
        blue += 1

    if arr[i] == 'R' and blue:
        cnt += blue
        blue = 0

ans.append(cnt)

# 좌측으로 레드 보내기
arr.reverse()
cnt = 0
red = 0

for i in range(N):
    if arr[i] == 'R':
        red += 1

    if arr[i] == 'B' and red:
        cnt += red
        red = 0

ans.append(cnt)

# 좌측으로 블루 보내기
blue = 0
cnt = 0
for i in range(N):
    if arr[i] == 'B':
        blue += 1

    if arr[i] == 'R' and blue:
        cnt += blue
        blue = 0

ans.append(cnt)

print(min(ans))