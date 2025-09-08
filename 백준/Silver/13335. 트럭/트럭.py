from collections import deque

n, w, l = map(int, input().split())
trucks = deque(map(int, input().split()))
bridge = deque([0] * w)

sec = 0

while bridge :
    sec += 1
    bridge.popleft()

    if trucks :
        if sum(bridge) + trucks[0] <= l :
            bridge.append(trucks.popleft())
        else :
            bridge.append(0)

print(sec)