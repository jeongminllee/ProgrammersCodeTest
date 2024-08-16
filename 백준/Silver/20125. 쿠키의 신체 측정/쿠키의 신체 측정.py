# 머리 위치 찾기
def head_idx(arr) :
    for i in range(N) :
        for j in range(N) :
            if arr[i][j] == '*' :
                return i, j

# 왼팔 길이
def dhls_hand(y, x) :
    cnt = 0
    for i in range(x-1, -1, -1) :
        cnt += 1
        if arr[y][i] == '_' :
            return cnt - 1
    return cnt

# 오른쪽 팔길이
def dh_hand(y, x) :
    cnt = 0
    for i in range(x + 1, N):
        cnt += 1
        if arr[y][i] == '_' :
            return cnt - 1
    return cnt

# 허리 길이
def waist(y, x) :
    cnt = 0
    for i in range(y, N) :
        cnt += 1
        if arr[i][x] == '_' :
            break
    return cnt - 1

# 다리 길이
def leg(y, x) :
    cnt = 1
    for i in range(y, N) :
        if arr[i][x] == '_' :
            break
        cnt += 1
    return cnt - 1

N = int(input())
arr = []
for _ in range(N) :
    row = input()
    arr.append(list(row))

y, x = head_idx(arr)
print(y + 2, x + 1) # 심장
print(dhls_hand(y+1, x), end=' ')   # 왼팔 길이
print(dh_hand(y+1, x), end=' ')     # 오른팔 길이
waist_cnt = waist(y+2, x)
print(waist_cnt, end=' ')   # 허리
print(leg(y+waist_cnt+2, x-1), end=' ') # 왼다리
print(leg(y+waist_cnt+2, x+1), end=' ') # 오른다리