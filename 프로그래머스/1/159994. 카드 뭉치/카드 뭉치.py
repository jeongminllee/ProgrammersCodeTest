from collections import deque

def solution(cards1, cards2, goal):
    # deque를 사용해서 먼저 입력된 데이터부터 꺼낼 수 있도록 세팅
    cards1, cards2, goal = deque(cards1), deque(cards2), deque(goal)
    
    # goal 을 돌면서 
    while goal :
        # cards1 과 goal이 같으면 pop하는 식으로 goal을 제거함
        if cards1 and cards1[0] == goal[0] :
            cards1.popleft()
            goal.popleft()
        elif cards2 and cards2[0] == goal[0] :
            cards2.popleft()
            goal.popleft()
        else :
            break
    
    # goal이 비었으면 'Yes', 아니라면 'No'
    return 'Yes' if not goal else 'No'