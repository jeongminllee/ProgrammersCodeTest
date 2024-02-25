def count(mid):
    return sum(min(mid // i, n) for i in range(1, n + 1))

n = int(input())
k = int(input())
l, r = 1, k
while l <= r :
    mid = (l + r) // 2
    if count(mid) < k :
        l = mid + 1
    else :
        answer = mid
        r = mid - 1

print(answer)