
def sol_1301() :
    N = int(input())
    remains = [int(input()) for _ in range(N)]

    dp = {}

    def dfs(remains, a, b) :
        # 현재 상태가 메모이제이션 되있으면 바로 불러오기
        state = (*remains, a, b)
        if state in dp :
            return dp[state]

        # 구슬을 다 썼으면 완성
        if sum(remains) == 0 :
            return 1

        # 현재 구슬 남아있고, 뒤에 두 개에 같은 색깔이 없으면 탐색
        answer = 0
        for x in range(N) :
            if remains[x] and x != a and x != b :
                remains[x] -= 1
                answer += dfs(remains, b, x)
                remains[x] += 1

        # 개수 저장
        dp[state] = answer
        return answer

    print(dfs(remains, -2, -1))
sol_1301()