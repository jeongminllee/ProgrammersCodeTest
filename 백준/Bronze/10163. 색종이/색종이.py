import sys
input = sys.stdin.readline

N = int(input())
arr = [[0] * 1001 for _ in range(1001)]
for n in range(1, N + 1) :
    sj, si, w, h = map(int, input().split())
    for i in range(si, si + h) :
        for j in range(sj, sj + w) :    # 해당 번호 색종이를 영역에 표시
            arr[i][j] = n

for n in range(1, N + 1) :
    cnt = 0
    for lst in arr :
        cnt += lst.count(n)
    print(cnt)