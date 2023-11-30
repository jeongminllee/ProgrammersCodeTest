def sum_lst(mx) :
    ans = 0
    for i in range(len(lst)) :
        if lst[i] > mx :
            ans += mx
        else :
            ans += lst[i]
    return ans

N = int(input())
lst = list(map(int, input().split()))
lmt = int(input())

answer = 0
if sum(lst) <= lmt :
    answer = max(lst)
else :
    cnt = 0
    left = 1
    right = max(lst)
    while left <= right :
        mid = (left + right) // 2
        if sum_lst(mid) > lmt :
            right = mid - 1
        else :
            left = mid + 1
            answer = mid
print(answer)