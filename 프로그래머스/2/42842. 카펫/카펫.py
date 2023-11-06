def solution(brown, yellow) :
    tile = brown + yellow
    rows = [(tile) // c for c in range(3, (tile) // 3 + 1) if tile % c == 0]
    for row in rows :
        col = tile // row
        if 2*(row + col - 2) == brown :
            return [row, col]
            

# 가로 >= 세로
# brown + yellow 
# 48 -> [1, 2, 3, 4, 6, 8, 12, 16, 24, 48]
# 총 타일 -> 약수 -> 리스트화
# 브라운 = ([0] + [1] - 2) * 2
# 옐로우 = tile - 옐로우
# print(len([1, 2, 3, 4, 6, 8, 12, 16, 24, 48]))
#
