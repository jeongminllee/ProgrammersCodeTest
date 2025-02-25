def valid(i, j) :
    return 0 <= i < 8 and 0 <= j < 8
def sol_1063() :
    move = {
        'R' : (1, 0), # 한 칸 오른쪽으로
        'L' : (-1, 0), # 한 칸 왼쪽으로
        'B' : (0, -1), # 한 칸 아래로
        'T' : (0, 1), # 한 칸 위로
        'RT' : (1, 1), # 오른쪽 위 대각선으로
        'LT' : (-1, 1), # 왼쪽 위 대각선으로
        'RB' : (1, -1), # 오른쪽 아래 대각선으로
        'LB' : (-1, -1) # 왼쪽 아래 대각선으로
    }

    king, stone, N = input().split()
    king = list(king)
    stone = list(stone)

    king[0] = ord(king[0]) - ord('A')
    king[1] = int(king[1]) - 1
    stone[0] = ord(stone[0]) - ord('A')
    stone[1] = int(stone[1]) - 1

    # print(ord('A')) # 65
    N = int(N)
    for _ in range(N) :
        moving = input().rstrip()
        
        ci, cj = king
        ni, nj = ci + move[moving][0], cj + move[moving][1]
        if valid(ni, nj) :
            if [ni, nj] == stone and valid(stone[0] + move[moving][0], stone[1] + move[moving][1]):
                king = [ni, nj]
                stone = [ni + move[moving][0], nj + move[moving][1]]
            elif [ni, nj] != stone :
                king = [ni, nj]
            
            elif not valid(stone[0] + 1, stone[1] + 1) :
                continue

    king = [chr(king[0] + 65), int(king[1]) + 1]
    stone = [chr(stone[0] + 65), int(stone[1]) + 1]
    print(''.join(map(str, king)))
    print(''.join(map(str, stone)))


sol_1063()