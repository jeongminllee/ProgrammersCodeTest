N, X = map(int, input().split())
lst = list(map(int, input().split()))

curr_sum = sum(lst[:X])
max_sum = curr_sum
cnt = 1

for i in range(1, N-X+1) :
    curr_sum = curr_sum - lst[i-1] + lst[i+X-1]

    if curr_sum > max_sum :
        max_sum = curr_sum
        cnt = 1
    elif curr_sum == max_sum :
        cnt += 1

if max_sum == 0 :
    print("SAD")
else :
    print(max_sum)
    print(cnt)