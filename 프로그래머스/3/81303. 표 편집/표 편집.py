def solution(n, k, cmd):
    answer = ['O' for _ in range(n)]
    deleted = []
    up = [i-1 for i in range(n + 2)]
    down = [i+1 for i in range(n + 1)]
    
    for c in cmd:
        if c[0] == 'U':
            for _ in range(int(c[2:])):
                if up[k] == -1: # 최상단일 경우
                    break
                k = up[k]
        elif c[0] == 'D':
            for _ in range(int(c[2:])):
                if down[k] == n: # 최하단일 경우
                    break
                k = down[k]
        elif c[0] == 'C':
            deleted.append(k)
            answer[k] = 'X'
            if up[k] != -1:
                down[up[k]] = down[k]
            if down[k] != n:
                up[down[k]] = up[k]
            k = down[k] if down[k] != n else up[k]
        else: # 'Z'
            z = deleted.pop()
            answer[z] = 'O'
            if up[z] != -1:
                down[up[z]] = z
            if down[z] != n:
                up[down[z]] = z
                
    return ''.join(answer)