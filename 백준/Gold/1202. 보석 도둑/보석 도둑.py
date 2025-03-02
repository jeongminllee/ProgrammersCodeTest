import sys
input = sys.stdin.readline

import heapq

def sol_1202() :
    N, K = map(int, input().split())
    jewels = []
    bags = []

    for _ in range(N) :
        m, v = map(int, input().split())
        heapq.heappush(jewels, (m, v))  # 힙에 푸시

    for _ in range(K) :
        bags.append(int(input()))       # 가방 무게 정보
    bags.sort()

    total_val, capable_jewels = 0, []
    for bag in bags :
        while jewels and bag >= jewels[0][0] :  # bag의 무게가 jewels의 무게보다 더 클 경우
            m, v = heapq.heappop(jewels)        # 힙에 팝
            heapq.heappush(capable_jewels, -v)  # 힙에 푸시 (-로 함으로써 큰 값으로 정렬)
        if capable_jewels :
            total_val -= heapq.heappop(capable_jewels)  # total_val 갱신 (다시 - 함으로써 + 로 바꿔서 갱신)
        elif not jewels :
            break
            
    print(total_val)
    
sol_1202()