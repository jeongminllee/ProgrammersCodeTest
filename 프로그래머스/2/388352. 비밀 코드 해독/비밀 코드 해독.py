from itertools import combinations

def query_count(q_set, ans, s, answer) :
    for qs, a in zip(q_set, ans) :
        if len(qs & s) != a :
            return False
        
    return True
def solution(n, q, ans):
    answer = 0
    q_set = [set(x) for x in q]
    # print(q_set)
    
    for comb in combinations(range(1, n+1), 5) :
        s = set(comb)
        answer += query_count(q_set, ans, s, answer)
            
        # if all(len(s & qs) == a for qs, a in zip(q_set, ans)) :
        #     answer += 1
    
    return answer