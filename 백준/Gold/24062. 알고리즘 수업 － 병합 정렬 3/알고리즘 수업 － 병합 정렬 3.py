n = int(input())
arr = list(map(int, input().split()))
brr = list(map(int, input().split()))
cnt = 0

tmp = [0] * n

flag = (arr == brr)
for i, j in zip(arr, brr):
    if i == j:
        cnt += 1


def merge(arr, p, q, r):
    global cnt, flag
    i = p
    j = q + 1
    t = 0

    while i <= q and j <= r:
        if arr[i] <= arr[j]:
            tmp[t] = arr[i]
            i += 1
        else:
            tmp[t] = arr[j]
            j += 1
        t += 1
    while i <= q:
        tmp[t] = arr[i]
        t += 1
        i += 1
    while j <= r:
        tmp[t] = arr[j]
        t += 1
        j += 1
    i = p
    t = 0
    while i <= r:
        be = arr[i]
        arr[i] = tmp[t]
        if arr[i] == brr[i] and be != arr[i]:
            cnt += 1
        elif arr[i] != brr[i] and be == brr[i]:
            cnt -= 1
        if cnt == n :
            flag = True
        i += 1
        t += 1


def merge_sort(arr, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(arr, p, q)
        merge_sort(arr, q + 1, r)
        merge(arr, p, q, r)


merge_sort(arr, 0, n - 1)
if flag:
    print(1)
else:
    print(0)