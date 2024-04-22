def solution(citations):
    citations.sort(reverse=True) # 인용 횟수를 내림차순으로 정렬
    # 각 논문에 대해, 인덱스와 인용 횟수 중 더 작은 값을 선택하고, 그 중 최댓값을 H-index로 결정
    answer = max(map(min, enumerate(citations, start=1)))
    return answer # 계산된 H-index 반환
