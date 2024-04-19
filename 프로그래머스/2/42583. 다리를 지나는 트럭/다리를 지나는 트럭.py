from collections import deque

def solution(bridge_length, weight, truck_weights) :
    answer = 0
    bridge = deque([0] * bridge_length) # 다리 상태를 나타내는 deque
    truck_weights = deque(truck_weights)

    currentWeight = 0   # 현재 다리 위의 트럭 무게 합

    while len(truck_weights) != 0 : # truck_weights 가 비어있지 않다면
        answer += 1
        # 다리를 건너고 있는 첫 번째 트럭이 다리를 벗어남 => 다리 위의 트럭 무게 합 감소
        currentWeight -= bridge.popleft()

        if currentWeight + truck_weights[0] <= weight : # 다음 트럭이 다리 위에 올라갈 수 있는 경우
            currentWeight += truck_weights[0]   # 다음 트럭을 현재 다리 무게에 합함.
            bridge.append(truck_weights.popleft())  # 다음 트럭을 현재 다리 위에 올림
        else :
            bridge.append(0)    # 다음 트럭이 올라갈 수 없는 경우, 다리에 0을 추가해 공간을 만듦.

    answer += bridge_length # 다리 길이 만큼 answer에 합함.

    return answer