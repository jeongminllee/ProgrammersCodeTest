from collections import defaultdict

T = int(input())
for _ in range(T) :
    N = int(input())
    teams = list(map(int, input().split()))
    num_cnt = defaultdict(int)
    num_dict = defaultdict(list)

    for num in teams  :
        num_cnt[num] += 1

    num_list = [x for x in teams if num_cnt[x] == 6]
    for idx, num in enumerate(num_list) :
        num_dict[num].append(idx)

    res = list(num_dict.keys())
    res.sort(key=lambda x:(sum(num_dict[x][:4]), num_dict[x][4], num_dict[x][5]))
    print(res[0])