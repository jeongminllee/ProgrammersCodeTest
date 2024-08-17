from collections import defaultdict

T = int(input())  # 테스트 케이스의 수를 입력받음

for _ in range(T):  # 각 테스트 케이스에 대해 반복
    N = int(input())  # 선수의 수를 입력받음
    teams = list(map(int, input().split()))  # 각 선수의 팀 번호를 리스트로 입력받음
    
    num_cnt = defaultdict(int)  # 각 팀 번호의 출현 횟수를 저장할 딕셔너리
    num_dict = defaultdict(list)  # 각 팀의 선수 인덱스를 저장할 딕셔너리

    for num in teams:
        num_cnt[num] += 1  # 각 팀 번호의 출현 횟수를 계산

    num_list = [x for x in teams if num_cnt[x] == 6]  # 정확히 6명의 선수가 있는 팀만 선택

    for idx, num in enumerate(num_list):
        num_dict[num].append(idx)  # 각 팀의 선수 인덱스를 저장

    res = list(num_dict.keys())  # 6명의 선수가 있는 팀 번호 리스트

    # 팀을 정렬:
    # 1. 상위 4명의 인덱스 합
    # 2. 5번째 선수의 인덱스
    # 3. 6번째 선수의 인덱스
    res.sort(key=lambda x: (sum(num_dict[x][:4]), num_dict[x][4], num_dict[x][5]))

    print(res[0])  # 정렬 후 가장 앞선 팀 번호 출력