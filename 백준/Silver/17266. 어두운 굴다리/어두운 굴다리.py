def binary_search(arr, mid) :
    if arr[1] - arr[0] > mid :
        return False
    if arr[-1] - arr[-2] > mid :
        return False
    for i in range(1, len(arr) - 2) :
        if (arr[i + 1] - arr[i]) / 2 > mid :
            return False
    return True

N = int(input())
M = int(input())
arr = [0] + list(map(int, input().split())) + [N]

s, e = 0, N
ans = 0
while s <= e :
    mid = (s + e) // 2
    if binary_search(arr, mid) :
        e = mid - 1
        ans = mid
    else :
        s = mid + 1

print(ans)