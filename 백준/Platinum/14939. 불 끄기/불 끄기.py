import copy

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

def isValid(arr, x, y) :
    for d in range(5) :
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < 10 and 0 <= ny < 10 :
            arr[nx][ny] = not arr[nx][ny]

def solve(arr) :
    ans = float('inf')
    for first_row in range(1<<10) :   # 10개 전구에 대한 모든 조작 경우의 수
        cnt = 0
        narr = [copy.deepcopy(row) for row in arr]  # arr 상태 복사
        for i in range(10) :
            if first_row & (1 << i) :   # 첫 줄의 i번째 전구를 조작하는 경우
                isValid(narr, 0, i)
                cnt += 1

        for i in range(1, 10) : # 나머지 줄 처리
            for j in range(10) :
                if narr[i-1][j] :   # 위 전구가 켜져 있으면 해당 위치의 전구 조작
                    isValid(narr, i, j)
                    cnt += 1
        
        if all(not val for row in narr for val in row) :    # 모든 전구가 꺼져 있는지 확인
            ans = min(ans, cnt)

    return ans if ans != float('inf') else -1

arr = []
for _ in range(10) :
    row = list(map(lambda x: x == 'O', input().strip()))
    arr.append(row)

print(solve(arr))