def solution(n, k, cmd):
    answer = ['O' for _ in range(n)]
    # 1. 삭제된 행의 인덱스를 저장하는 리스트
    deleted = []

    # 2. 링크드 리스트에서 각 행 위 아래의 행의 인덱스를 저장하는 리스트
    up = [i-1 for i in range(n + 2)]
    down = [i+1 for i in range(n + 1)]
    
    for c in cmd:
        if c.startswith('C') :
            deleted.append(k)
            up[down[k]] = up[k]
            down[up[k]] = down[k]
            k = down[k] if down[k] != n else up[k]

        elif c.startswith('Z') :
            z = deleted.pop()
            down[up[z]] = z
            up[down[z]] = z

        else :
            action, num = c.split()
            if action == 'U' :
                for _ in range(int(num)) :
                    k = up[k]

            else :
                for _ in range(int(num)) :
                    k = down[k]

    for i in deleted :
        answer[i] = 'X'
    return ''.join(answer)