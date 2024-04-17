import sys
sys.setrecursionlimit(10**6)
from collections import deque
def bfs(si, sj, num, w, move, board, diagonal) :
    q = deque()
    q.append((si, sj, num, 0))
    w[num][num] = 1

    while q :
        curr = q.popleft()

        for d in range(4) : # 상하좌우 이동
            ni = curr[0] + move[d][0]
            nj = curr[1] + move[d][1]

            if check(ni, nj) == 1 and board[ni][nj] != "*" and board[ni][nj] != "#" \
                and w[num][int(board[ni][nj])] > curr[3] + 2 :
                w[num][int(board[ni][nj])] = curr[3] + 2
                w[int(board[ni][nj])][num] = curr[3] + 2
                q.append((ni, nj , int(board[ni][nj]), curr[3] + 2))

        for d in range(4) : # 대각 이동
            ni = curr[0] + diagonal[d][0]
            nj = curr[1] + diagonal[d][1]

            if check(ni, nj) == 1 and board[ni][nj] != "*" and board[ni][nj] != "#" \
                    and w[num][int(board[ni][nj])] > curr[3] + 3:
                w[num][int(board[ni][nj])] = curr[3] + 3
                w[int(board[ni][nj])][num] = curr[3] + 3
                q.append((ni, nj, int(board[ni][nj]), curr[3] + 3))

def check(r, c):
    if 0 <= r < 4 and 0 <= c < 3 :
        return True
    return False

def getMinTime(idx, left, right, n, dp, INF, number, w) :
    if idx == n :
        return 0

    if dp[idx][left][right] == INF :
        first = INF
        second = INF
        if right != number[idx] :
            first = w[left][number[idx]] + getMinTime(idx + 1, number[idx], right, n, dp, INF, number, w)
        if left != number[idx] :
            second = w[right][number[idx]] + getMinTime(idx + 1, number[idx], left, n, dp, INF, number, w)

        dp[idx][left][right] = min(first, second)

    return dp[idx][left][right]

def solution(numbers):
    INF = float('inf')
    n = len(numbers)
    number = [int(num) for num in numbers]
    dp = [[[INF] * 10 for _ in range(10)] for _ in range(n)]
    move = [(-1, 0), (1,0), (0,-1),(0,1)]
    diagonal = [(-1,-1), (1,-1), (-1,1), (1,1)]
    board = [['1','2','3'],
             ['4','5','6'],
             ['7','8','9'],
             ['*','0','#']]
    w = [[100] * 10 for _ in range(10)]
    for i in range(4) :
        for j in range(3) :
            if board[i][j] != '*' and board[i][j] != '#' :
                bfs(i, j, int(board[i][j]), w, move, board, diagonal)

    return getMinTime(0, 4, 6, n, dp, INF, number, w)