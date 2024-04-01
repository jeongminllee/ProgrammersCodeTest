import heapq

def solution(operations):
    # 최소힙과 최대힙을 구하는 리스트 생성
    # 힙은 기본적으로 최소힙을 지향하기 때문에 최대힙을 따로 구현
    heap = []
    max_heap = []
    
    for operation in operations :
        op, num = operation.split()
        num = int(num)
        
        if op == "I" :  # op가 "I"이면
            # 최소힙, 최대힙 추가
            # 최대힙은 음수로 힙을 넣어서 구현
            heapq.heappush(heap, num)
            heapq.heappush(max_heap, (-num, num))
        else :  # op가 "D"
            if not heap :   # 힙이 비어있으면
                pass
            elif num == 1 : # "D 1"
                max_value = heapq.heappop(max_heap)[1]
                heap.remove(max_value)
            elif num == -1 :# "D -1"
                min_value = heapq.heappop(heap)
                max_heap.remove((-min_value, min_value))
                
    if heap :   # 힙에 남아있으면 [최대힙, 최소힙]
        return [heapq.heappop(max_heap)[1], heapq.heappop(heap)]
    else :  # 힙이 비어있으면
        return [0,0]