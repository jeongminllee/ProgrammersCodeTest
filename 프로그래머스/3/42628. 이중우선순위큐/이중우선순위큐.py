import heapq
from collections import defaultdict

def solution(operations):
    max_heap = []
    min_heap = []
    num_cnt = defaultdict(int)
    
    for operation in operations :
        op, num = operation.split()
        num = int(num)
        
        if op == "I" :
            heapq.heappush(max_heap, (-num, num))
            heapq.heappush(min_heap, num)
            num_cnt[num] += 1

        else :
            if not min_heap :
                pass
            
            elif num == 1 :
                while max_heap and num_cnt[max_heap[0][1]] == 0 :
                    heapq.heappop(max_heap)
                if max_heap :
                    max_value = heapq.heappop(max_heap)[1]
                    num_cnt[max_value] -= 1
                    
            else :
                while min_heap and num_cnt[min_heap[0]] == 0:
                    heapq.heappop(min_heap)
                if min_heap :
                    min_value = heapq.heappop(min_heap)
                    num_cnt[min_value] -= 1
    
    while max_heap and num_cnt[max_heap[0][1]] == 0 :
        heapq.heappop(max_heap)
    while min_heap and num_cnt[min_heap[0]] == 0:
        heapq.heappop(min_heap)
        
    if not min_heap :
        return [0, 0]

    else :
        return [heapq.heappop(max_heap)[1], heapq.heappop(min_heap)]