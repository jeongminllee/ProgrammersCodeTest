import heapq

N, M, K = map(int, input().split())
lst = list(map(int, input().split()))

# 최대 힙을 구현하기 위해 음수로 변환
pq = []
sm = 0

for i in range(N) :
    # 현재 값을 더하고 최대힙에 추가 (음수로 변환하여 최대 힙을 구현)
    sm += lst[i]
    heapq.heappush(pq, -lst[i])

    if sm > M :
        # 합이 M을 초과하고 K가 남아있고 힙이 비어있지 않은 동안
        while sm > M and K > 0 and pq :
            # 가장 큰 값을 제거 (음수로 저장했으므로 -를 붙여서 원래 값으로 변환)
            sm += heapq.heappop(pq)
            K -= 1

        # 여전히 합이 M을 초과하면 현재 인덱스 출력
        if sm > M :
            print(i)
            exit()

# 모든 처리가 가능한 경우 N 출력
print(N)