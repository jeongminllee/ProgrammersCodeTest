from itertools import combinations

def solution(n, q, ans):
    answer = 0
    q_set = [set(x) for x in q]
    
    for comb in combinations(range(1, n+1), 5) :
        s = set(comb)
        if all(len(s & qs)== a for qs, a in zip(q_set, ans)) :
            answer += 1
    
    return answer