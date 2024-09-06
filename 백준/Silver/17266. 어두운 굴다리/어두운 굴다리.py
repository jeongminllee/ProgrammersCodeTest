def binary_search(arr, mid):
    # 첫 번째 가로등이 시작점을 충분히 비추는지 확인
    if arr[1] - arr[0] > mid:
        return False
    # 마지막 가로등이 끝점을 충분히 비추는지 확인
    if arr[-1] - arr[-2] > mid:
        return False
    # 중간의 모든 가로등들이 서로의 영역을 충분히 커버하는지 확인
    for i in range(1, len(arr) - 2):
        if (arr[i + 1] - arr[i]) / 2 > mid:
            return False
    return True

# 굴다리의 길이 N 입력
N = int(input())
# 가로등의 개수 M 입력 (사용되지 않음)
M = int(input())
# 가로등의 위치를 입력받고, 시작점(0)과 끝점(N)을 추가
arr = [0] + list(map(int, input().split())) + [N]

# 이진 탐색 시작
s, e = 0, N
ans = 0
while s <= e:
    # 중간값 계산 (현재 테스트할 가로등의 높이)
    mid = (s + e) // 2
    # 현재 높이로 모든 굴다리를 비출 수 있는지 확인
    if binary_search(arr, mid):
        # 가능하다면, 높이를 줄여서 다시 시도
        e = mid - 1
        ans = mid  # 현재 높이를 정답으로 저장
    else:
        # 불가능하다면, 높이를 높여서 다시 시도
        s = mid + 1

# 최소 높이 출력
print(ans)