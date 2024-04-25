def solution(cap, n, deliveries, pickups):
    answer = 0
    deliveries.reverse()
    pickups.reverse()
    
    cnt_de = 0
    cnt_pick = 0
    
    for i in range(n) :
        cnt_de += deliveries[i]
        cnt_pick += pickups[i]
        
        while cnt_de > 0 or cnt_pick > 0 :
            cnt_de -= cap
            cnt_pick -= cap
            answer += (n - i) * 2
    return answer