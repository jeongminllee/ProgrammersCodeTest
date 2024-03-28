def solution(storey) :
    ans = 0
    while storey != 0 :
        cur = storey % 10
        next_ = (storey // 10) % 10

        if cur > 5 :
            ans += 10 - cur
            storey += 10

        elif cur < 5 :
            ans += cur
            
        else :  # cur = 5
            if next_ > 4 :
                storey += 10
            ans += cur

        storey //= 10
    return ans