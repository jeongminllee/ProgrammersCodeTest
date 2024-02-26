def dfs(n, y, v1, v2, v3):
    ans = 0
    if y == n:  # N행까지 진행한 경우의 수 가능 : 성공
        ans += 1

    for j in range(n):
        if v1[j] == v2[y + j] == v3[y - j] == 0:  # 열 / 대각선 모두 Q 없음
            v1[j] = v2[y + j] = v3[y - j] = 1
            ans += dfs(n, y + 1, v1, v2, v3)
            v1[j] = v2[y + j] = v3[y - j] = 0

    return ans

def solution(n):
    v1 = [0] * n
    v2 = [0] * (2 * n)
    v3 = [0] * (2 * n)
    ans = dfs(n, 0, v1, v2, v3)
    return ans
