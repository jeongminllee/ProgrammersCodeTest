from collections import defaultdict

T = int(input())    # 테스트 케이스
for _ in range(T) :
    N = int(input())    # 선수의 수
    teams = list(map(int, input().split())) # 각 선수의 팀 번호를 리스트로 입력받음

    team_cnt = defaultdict(int) # 각 팀 번호의 출현 횟수를 저장할 딕셔너리
    team_dict = defaultdict(list)   # 각 팀의 선수 인덱스를 저장할 딕셔너리

    for num in teams :
        team_cnt[num] += 1  # 각 팀의 번호를 출현 횟수를 계산

    # 정확히 6명의 선수가 있는 팀만 선택
    team_list = [x for x in teams if team_cnt[x] == 6]

    for idx, num in enumerate(team_list) :
        team_dict[num].append(idx)  # 각 팀의 선수 인덱스를 저장


    # 팀을 정렬 :
    # 1. 상위 4명의 인덱스 합
    # 2. 5번째 선수의 인덱스
    # 3. 6번째 선수의 인덱스
    res = list(team_dict.keys())
    res.sort(key=lambda x:(sum(team_dict[x][:4]), team_dict[x][4], team_dict[x][5]))
    print(res[0])