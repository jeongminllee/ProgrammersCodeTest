def dfs(dist_limit, split_limit, w, d, s, leaves) :
    best = leaves

    if d == dist_limit :
        return best
    
    for k in (2, 3) :
        if s * k > split_limit :
            continue
        a = min(w, dist_limit-d)
        curr = dfs(dist_limit, split_limit, a*k, d+a, s*k, leaves + a * (k-1))
        best = max(best, curr)

    return best
def solution(dist_limit, split_limit):
    answer = 1
    best = dfs(dist_limit, split_limit, 1, 0, 1, 1)
    answer = max(answer, best)
    return answer