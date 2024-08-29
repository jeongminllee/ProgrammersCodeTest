N = int(input())
lst = list(map(int, input().split()))

res = 0
left, right = 0, 0
ch = [0] * 100001

while left != N and right != N :
    if not ch[lst[right]] :
        ch[lst[right]] = 1
        right += 1
        res += right - left

    else :
        while ch[lst[right]] :
            ch[lst[left]] = 0
            left += 1

print(res)