def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]    # 인덱스 0 ~ 6 에 해당하는 일치하는 번호의 개수로 순위를 결정
    zero_cnt = lottos.count(0)  # 0의 개수
    match_cnt = len(set(lottos) & set(win_nums))    # lottos와 win_nums 간의 교집합의 원소 개수를 구하여 일치하는 번호의 개수 파악
    
    # 최고 순위와 최저 순위 계산
    max_rank = rank[match_cnt + zero_cnt]   # 최고 순위는 일치하는 번호의 개수 + 0의 개수
    min_rank = rank[match_cnt]  # 최저 순위는 일치하는 번호의 개수만 고려

    return [max_rank, min_rank]