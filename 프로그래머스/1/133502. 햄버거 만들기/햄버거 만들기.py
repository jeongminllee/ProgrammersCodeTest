def solution(ingredient):
    # 1 : 빵, 2: 야채, 3: 고기
    # 빵 - 야채 - 고기 - 빵, 1 2 3 1 순으로 와야됨
    answer = 0
    stack = []
    for i in ingredient :
        stack.append(i)
        if stack[-4:] == [1,2,3,1] :
            answer += 1
            for _ in range(4) :
                stack.pop()

    return answer