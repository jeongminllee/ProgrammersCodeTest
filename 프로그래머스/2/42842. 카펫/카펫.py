def solution(brown, yellow) :
    w = (brown // 2) + 1
    h = 1
    while w >= h :
        if (w - 2) * (h - 2) == yellow :
            return [w, h]
        
        w -= 1
        h += 1

# def solution(brown, yellow) :
#     tile = brown + yellow
#     rows = [(tile) // c for c in range(3, (tile) // 3 + 1) if tile % c == 0]
#     for row in rows :
#         col = tile // row
#         if 2*(row + col - 2) == brown :
#             return [row, col]
            

# 가로 >= 세로
# brown + yellow 
# 48 -> [1, 2, 3, 4, 6, 8, 12, 16, 24, 48]
# 총 타일 -> 약수 -> 리스트화
# 브라운 = ([0] + [1] - 2) * 2
# 옐로우 = tile - 옐로우
# print(len([1, 2, 3, 4, 6, 8, 12, 16, 24, 48]))
#
# def solution(brown, yellow) :
#     for i in range(1, int(yellow**(1/2)) + 1) :
#         if yellow % i == 0 :
#             if 2*(i + yellow//i) == brown - 4 :
#                 return [yellow//i+2, i+2]