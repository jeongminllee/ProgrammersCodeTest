import numpy as np
from collections import Counter

def solution(board):
    n = len(board)
    board_padded = np.pad(board, ((1, 1), (1, 1)), constant_values = -1)
    danger_array = np.pad(board, ((1, 1), (1, 1)), constant_values = -1)
    for i in range(1, n + 1) :
        for j in range(1, n + 1) :
            if board_padded[i][j] == 1 :
                for x in range(i-1, i+2) :
                    for y in range(j-1, j+2) :
                        danger_array[x][y] = 1
    danger_list = danger_array.reshape(1, -1).squeeze()
    answer = Counter(danger_list)[0]
    return answer


def solution(board) :
    n = len(board)
    danger = set()
    for i, row in enumerate(board) :
        for j, x in enumerate(row) :
            if not x :
                continue
            danger.update((i + di, j + dj) for di in [-1, 0, 1] for dj in [-1, 0, 1])
    return n * n - sum(0 <= i < n and 0 <= j < n for i, j in danger)