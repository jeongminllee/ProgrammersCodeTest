'''
n개의 스테이지를 순서대로 모두 연결해야함. 
각 스테이지를 해결하기 위해서는 해결 비용이 필요, 힌트권을 많이 사용할수록 비용이 감소
- 힌트권에는 1-n 까지의 번호가 붙어있음
- i번 힌트권은 오직 i번 스테이지에서만 사용 가능
- 하나의 스테이지에서 사용할 수 있는 힌트권은 최대 n-1개임
- 초기에는 힌트권 없음.

마지막 스테이지를 제외한 각 스테이지에서는 해당 스테이지에서 판매하는 힌트 번들을 최대 1개 구매할 수 있음.
힌트 번들은 이후 스테이지의 힌트권을 제공 비용을 주고 사야함
- 스테이지마다 구매 가능한 힌트 번들의 종류와 판매 가격이 다를 수 있음
- 힌트 번들에는 힌트권이 총 k장 들어있으며, 같은 번호의 힌트권이 여러 장 포함될 수 있음
- i번 스테이지에서 판매하는 힌트 번들은 항상 i+1 이상의 번호를 가진 힌트권만 들어있음.

모든 스테이지를 해결하는데 필요한 최소 비용을 구해야함

스테이지 해결 비용 + 힌트 구매 비용  
'''
INF = 1<<32
def solution(cost, hint):
    min_total_cost = INF
    total_cases = 1 << (len(cost) - 1)
    
    for mask in range(total_cases) :
        hint_count = [0] * (len(cost)+1)
        curr_cost = 0
        
        for i in range(1, len(cost)) :
            if (mask & (1 << (i-1))) != 0 :
                curr_cost += hint[i - 1][0]
                
                for j in range(1, len(hint[i-1])) :
                    hint_count[hint[i-1][j]] += 1
                    
        for i in range(1, len(cost)+1) :
            mx_use = len(cost) - 1
            usable = min(hint_count[i], mx_use)
            
            curr_cost += cost[i-1][usable]
            
        min_total_cost = min(min_total_cost, curr_cost)
        
    return min_total_cost