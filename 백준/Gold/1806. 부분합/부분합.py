N, S = map(int, input().split())
lst = list(map(int,input().split()))

left, right = 0, 0
num = 0
mn_length = 1e9

while True :
    if S <= num :
        mn_length = min(mn_length, right - left)
        num -= lst[left]
        left += 1
    elif right == N :
        break
    else :
        num += lst[right]
        right += 1

if mn_length == 1e9 :
    print(0)
else :
    print(mn_length)