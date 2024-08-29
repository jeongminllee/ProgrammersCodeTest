N = int(input())
lst = list(map(int,input().split()))
lst.sort()
cnt = 0

for i in range(N) :
    target = lst[i]
    left, right = 0, N - 1
    while left < right :
        num = lst[left] + lst[right]
        if num == target :
            if left == i :
                left += 1
            elif right == i :
                right -= 1
            else :
                cnt += 1
                break

        elif num > target :
            right -= 1

        elif num < target :
            left += 1
print(cnt)