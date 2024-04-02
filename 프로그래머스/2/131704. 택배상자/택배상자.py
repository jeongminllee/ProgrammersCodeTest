def solution(order):
    answer = 0
    stack = []  
    curr = 1    # 택배 번호
    while curr != len(order) + 1 :  # 현재 택배 번호가 order 순서와 다르면
        stack.append(curr)
        while stack[-1] == order[answer] :  # 현재 내가 들고있는 물건이 트럭에 실어야 되는 택배면
            answer += 1 # 트럭에 싣는다.
            stack.pop() # 스택에서 뺀다.
        
            if not stack :  # 스택이 비었으면
                break
            
        curr += 1   # 다음 택배를 든다.

    return answer