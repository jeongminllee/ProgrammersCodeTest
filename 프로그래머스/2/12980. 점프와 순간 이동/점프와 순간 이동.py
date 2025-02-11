def solution(n):
    ans = 0
    # 시작은 0 -> 1 ans = 1
    # 1 => 2 
    # 2 => 4
    # 4 => 5 ans = 2
    
    # 0 -> 1 ans = 1
    # 1 => 2
    # 2 => 3 ans = 2
    # 3 => 6 
    
    # 역으로 반으로 줄여나가자
    while n > 0 :
        if n % 2 == 0 :
            n //= 2
        else :
            n -= 1
            ans += 1
    
    return ans