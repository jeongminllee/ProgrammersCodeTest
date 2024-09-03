import math
H, W, N, M = map(int, input().split())
row = math.ceil(H/(N + 1))
col = math.ceil(W/(M + 1))

ans = row * col
print(ans)

'''
H, W, N, M = map(int, input().split())

row = H // (N + 1)
col = W // (M + 1)

if H % (N + 1) != 0 :
    row += 1
if W % (M + 1) != 0 :
    col += 1

ans = row * col
print(ans)
'''