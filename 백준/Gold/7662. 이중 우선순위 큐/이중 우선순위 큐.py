import heapq
from collections import defaultdict

T = int(input())

for _ in range(T) :
    k = int(input())
    max_pq = []
    min_pq = []
    num_cnt = defaultdict(int)

    for _ in range(k) :
        cmd = list(input().split())
        if cmd[0] == 'I' :
            num = int(cmd[1])
            heapq.heappush(min_pq, num)     # 최소 힙에 추가
            heapq.heappush(max_pq, -num)    # 최대 힙에 -num으로 추가
            num_cnt[num] += 1

        else :
            if len(max_pq) == 0 and len(min_pq) == 0:
                continue

            elif cmd[1] == '1' :    # 최댓값 삭제
                # 유효하지 않은 값들 먼저 제거
                while max_pq and num_cnt[-max_pq[0]] == 0 :
                    heapq.heappop(max_pq)

                # 실제 최댓값 삭제
                if max_pq :
                    max_num = -heapq.heappop(max_pq)
                    num_cnt[max_num] -= 1

            else :  # 최솟값 삭제
                # 유효하지 않은 값들을 먼저 제거
                while min_pq and num_cnt[min_pq[0]] == 0 :
                    heapq.heappop(min_pq)

                # 실제 최솟값 삭제
                if min_pq :
                    min_num = heapq.heappop(min_pq)
                    num_cnt[min_num] -= 1

    # 남아있는 유효하지 않은 값들 제거
    while max_pq and num_cnt[-max_pq[0]] == 0 :
        heapq.heappop(max_pq)
    while min_pq and num_cnt[min_pq[0]] == 0 :
        heapq.heappop(min_pq)

    if len(max_pq) == 0 and len(min_pq) == 0:
        print("EMPTY")
    else :
        print(-max_pq[0], min_pq[0])