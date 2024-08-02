def solution(info, edges):
    answer = 0
    v = [0] * len(info)
    
    def dfs(sheep, wolf) :
        nonlocal answer
        if sheep > wolf :
            answer = max(answer, sheep)
        else :
            return
        
        for prev, curr in edges :
            if v[prev] and not v[curr] :
                v[curr] = 1
                if info[curr] == 0 :
                    dfs(sheep + 1, wolf)
                else :
                    dfs(sheep, wolf + 1)
                v[curr] = 0
    
    v[0] = 1
    dfs(1, 0)
    return answer