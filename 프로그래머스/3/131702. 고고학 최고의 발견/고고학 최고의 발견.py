def solution(clockHands):
    answer = float('inf')

    # 회전을 구현한 함수
    def plus(r, c, num):
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                newclockHands[nr][nc] = (newclockHands[nr][nc] + num) % 4
        return

    n = len(clockHands)
    for i in range(1 << (2 * n)):
        newclockHands = [clockHands[i][:] for i in range(n)]
        cnt = 0
        for c in range(n):
            a = '1' if i & (1 << 2 * c) else '0'
            b = '1' if i & (1 << 2 * c + 1) else '0'
            plus(0, c, int(b + a, base=2))
            cnt += int(b + a, base=2)

        for line in range(1, n):
            if cnt >= answer:
                break

            for c in range(n):
                num = newclockHands[line - 1][c]
                if num:
                    plus(line, c, 4 - num)
                    cnt += 4 - num

        if newclockHands[-1] == ([0] * n):
            if cnt < answer:
                answer = cnt

    return answer