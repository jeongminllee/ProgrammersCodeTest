# 굴린다 : +1 칸 이동, 눈덩이 크기 + a
# 던진다 : +2 칸 이동, (눈덩이 크기 // 2) + a

def dfs(size, time, idx) :
    global snowball

    if time > M :
        return

    else :
        snowball = max(snowball, size)

    if idx <= N - 1 :
        dfs(size + arr[idx + 1], time + 1, idx + 1)

    if idx <= N - 2 :
        dfs((size // 2) + arr[idx + 2], time + 1, idx + 2)

# N, M : 앞마당의 길이, 대회의 시간
N, M = map(int, input().split())

# 눈덩이 크기 a 총 길이 N + 1
arr = [1] + list(map(int, input().split()))

snowball = 0
dfs(1, 0, 0)
print(snowball)