def solution(ingredient):
    # 1 : 빵, 2: 야채, 3: 고기
    # 빵 - 야채 - 고기 - 빵, 1 2 3 1 순으로 와야됨
    answer = 0
    stack = []
    for i in range(len(ingredient)) :
        stack.append(ingredient[i])
        if len(stack) >= 4 and ingredient[i] == 1 :
            if stack[-2] == 3 and stack[-3] == 2 and stack[-4] == 1 :
                for i in range(4) :
                    stack.pop()
                answer += 1
    return answer