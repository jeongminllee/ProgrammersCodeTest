def solution(food):
    food_str = []
    
    for i in range(1, len(food)) :
        mid = food[i] // 2
        food_str.extend([str(i)] * mid)
    
    answer = ''.join(food_str) + '0' + ''.join(reversed(food_str))
    
    return answer