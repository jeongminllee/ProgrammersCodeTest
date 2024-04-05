import heapq

def solution(n, k, enemy):
    heap = []   # 무적권을 사용할 라운드
    for i, e in enumerate(enemy) :  # 각 라운드와 그 라운드의 적들 수를 순회
        heapq.heappush(heap, e) # 현재 라운드 적의 수를 힙에 추가
        if len(heap) > k :  # 만약 힙의 크기가 무적권을 사용할 수 있는 횟수를 초과하면
            n -= heapq.heappop(heap)    # 힙에서 가장 작은 값을 꺼내와 현재 병사 수로 제거함
        if n < 0 :  # 그러나 그 라운드의 적의 수가 현 병사 수 보다 크다면
            return i    # 현 라운드를 반환
    return len(enemy)   # 전체를 다 돌면 전체 라운드 수를 반환