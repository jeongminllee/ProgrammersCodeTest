def solution(cap, n, deliveries, pickups):
    # 배달과 수거 배열을 뒤집음 = 먼 위치부터 배달을 완료 해야 여러번 반복하지 않음
    deliveries.reverse()
    pickups.reverse()
    answer = 0  # 총 이동 거리

    # 현재까지 처리해야 할 배달 및 수거 상자의 수
    deli_cnt = 0
    pick_cnt = 0

    # 모든 집을 순회
    for i in range(n) :
        # i번째 집에서 배달할 상자의 수와 수거할 상자의 수를 누적
        deli_cnt += deliveries[i]
        pick_cnt += pickups[i]
    
    # 현재 집에서 처리해야 할 배달 또는 수거가 남아있는 경우
        while deli_cnt > 0 or pick_cnt > 0 :
            # 트럭의 용량만큼 배달 또는 수거를 처리
            # 처리할 수 있는 최대량을 초과하는 경우, 초과분은 다음 순회 때 처리
            deli_cnt -= cap
            pick_cnt -= cap
            # 물류창고에서 현재 위치까지 왕복 거리를 계산하여 총 이동 거리에 더함
            answer += (n - i) * 2

    return answer