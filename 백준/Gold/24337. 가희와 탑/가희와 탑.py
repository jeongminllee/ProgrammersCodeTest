N, a, b = map(int, input().split())
ans = []
max_building = max(a,b)     # 가장 높은 건물 높이

for i in range(1, a) :      # 1 ~ a-1 까지 건물 세우기
    ans.append(i)

ans.append(max_building)    # 가장 높은 건물 세우기

for i in range(b-1, 0, -1): # b-1 ~ 1 까지 건물 세우기
    ans.append(i)

if len(ans) > N :           # 세운 건물이 N보다 많으면
    print(-1)
else :
    print(ans[0], end=' ')  # 제일 왼쪽 건물 하나 먼저 출력
    x = N - len(ans)        # 더 세워야 하는 건물 개수

    for i in range(x):      # 건물 개수 만족할 때 까지 1 출력
        print(1, end=' ')

    for i in range(1, len(ans)):    # 다음 건물 계속 출력
        print(ans[i], end=' ')