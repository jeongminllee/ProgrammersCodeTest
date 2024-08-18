T = int(input())
for _ in range(T):
    n, k, t, m = map(int, input().split())  # 팀의 개수 n, 문제의 개수 k, 당신 팀의 ID t, 로그 엔트리의 개수 m
    scores = [[0] * (k + 1) for _ in range(n + 1)]  # 각 팀별 점수
    teams = [0] * (n + 1)                           # 팀별 제출 횟수
    last_sub = [0] * (n + 1)                        # 마지막으로 제출한 팀 체크
    res = []

    for a in range(m):
        i, j, s = map(int, input().split())  # 팀 ID i, 문제 번호 j, 획득한 점수 s
        scores[i][j] = max(scores[i][j], s)  # 어차피 초기값은 0이니까
        teams[i] += 1  # 제출 횟수 확인
        last_sub[i] = a  # 마지막 제출 확인

    for i in range(n+1):
        # 최종 점수, 제출 횟수, 마지막 제출, 팀 ID
        res.append([sum(scores[i]), teams[i], last_sub[i], i])

    res.sort(key=lambda x: (-x[0], x[1], x[2]))
    for rank in range(n + 1):
        if res[rank][3] == t:
            print(rank + 1)