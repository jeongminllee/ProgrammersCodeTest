n = int(input())
lst = list(map(int, input().split()))
cluster = int(input())
cnt = 0
for i in range(n) :
    if lst[i] != 0 and lst[i] <= cluster :
        cnt += 1
    elif lst[i] == 0 :
        continue
    else :
        if lst[i] % cluster != 0 :
            cnt += (lst[i]//cluster) + 1
        else :
            cnt += (lst[i]//cluster)

print(cluster*cnt)